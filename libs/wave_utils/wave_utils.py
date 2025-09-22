import random
import urllib.parse
import wavedrom

def make_random_signal(length):

    """
    Makes a random wavedrom signal of length length and puts it in the form
    1...0..1.0...
    """

    signal = []

    # Pick random points for the signal to toggle
    num_toggles = random.choice([2,3,4,5])
    toggle_pts = random.sample(range(1,length), num_toggles)

    signal_value = random.choice([0, 1])
    signal.append(signal_value)

    # Generate the signals
    for i in range(length - 1):
        # If it's time to toggle, toggle the signal
        if i in toggle_pts:
            signal_value = 1 - signal_value
            # When toggling, put the 0 or 1 in the wavedrom signal
            signal.append(signal_value)
        # Otherwise put . in the wavedrom signal
        else:
            signal.append(".")

    # Turn list into string
    signal = [str(i) for i in signal]
    signal = "".join(signal)

    return signal

def make_clock(length, period=10, first_rising_edge=5):
    """
    Makes a wavedrom signal representing a clock
    length: length of the signal in ns
    period: clock period in ns, must be even, default 10
    first_rising_edge: position of first rising edge, default 0
    """

    if period % 2 != 0:
        raise Exception("Clock period must be even")

    signal = []
    signal_value = 0

    # Generate a longer clock signal so a portion of it can be taken later
    for i in range(length + period):
        # Toggle the signal on multiples of half the period
        if i % (period/2) == 0:
            signal_value = 1 - signal_value
            # Put the 0 or 1 there
            signal.append(signal_value)
        else:
            # Put the . there if not a 0 or 1
            signal.append(".")
    
    # Turn list into string
    signal = [str(i) for i in signal]
    signal = "".join(signal)

    # Find out which portion to take to align the first rising edge
    start = period - first_rising_edge
    end = start + length
    signal = signal[start:end]

    return signal

def wavedrom_to_binary(wavedrom):

    """
    Turns a wavedrom signal (1..0..1.) into binary (11100011)
    """
    
    binary = ""
    signal_value = ""

    # Iterate through every character in the wavedrom signal
    for i in wavedrom:
        # Turn dots into 1 or 0 depending on what was last seen
        if i == ".":
            binary += signal_value
        # Preserve 1s and 0s while noting what was last seen
        else:
            binary += i
            signal_value = i

    return binary

def binary_to_wavedrom(binary):
    """
    Turns a binary signal (11100011) into wavedrom form (1..0..1.)
    """

    wavedrom = ""
    signal_value = ""

    for i in binary:
        # If the character is a repeat, replace it with a dot
        if i == signal_value:
            wavedrom += "."
        # Otherwise preserve the 1 or 0 (or x) and update what was last seen
        else:
            wavedrom += i
            signal_value = i

    return wavedrom

def wavedrom_gate(gate, a, b="", delay=0):
    """
    Puts two wavedrom signals of same length through a logic gate
    a: first wavedrom format signal (1..0.1..)
    b: second wavedrom format signal if need be
    gate: can be "or", "and", "not", "xor", "xnor", "nand", "nor", or "buf"
    delay: delay in ns to shift output
    """
    
    length = len(a)
    gate = gate.lower()

    # Convert wavedrom signal to binary format
    a = wavedrom_to_binary(a)
    a = a.lower()

    # Do the same with b if specified
    if b:
        b = wavedrom_to_binary(b)
        b = b.lower()

    out = ""

    # Apply bit logic individually to each bit in a and b
    for i in range(len(a)):

        
        a_bit = int(a[i]) if a[i].isdigit() else a[i]

        if b:
            b_bit = int(b[i]) if b[i].isdigit() else b[i]

        # Unknown going into a gate always outputs an unknown
        if a[i] == "x" or (b and b[i] == "x"):
            out_bit = "x"
        
        elif gate == "buf":
            out_bit = a_bit
        elif gate == "not":
            out_bit = ~a_bit
        elif gate == "or":
            out_bit = a_bit | b_bit
        elif gate == "and":
            out_bit = a_bit & b_bit
        elif gate == "xor":
            out_bit = a_bit ^ b_bit
        elif gate == "nor":
            out_bit = ~(a_bit | b_bit)
        elif gate == "nand":
            out_bit = ~(a_bit & b_bit)
        elif gate == "xnor":
            out_bit = ~(a_bit ^ b_bit)
        else:
            raise Exception("Invalid gate name")

        # Isolate LSB and avoid weird python integer jank
        if out_bit != "x":
            out_bit &= 1

        out += str(out_bit)

    # Apply gate delay and put x (unknown) at the beginning
    out = ("x" * delay) + out[0:(length - delay)]

    # Convert back to wavedrom format
    out = binary_to_wavedrom(out)

    return out

def wavedrom_sr_latch(s, r, delay=0, initial_value = "x"):
    """
    Emulates an SR latch with WaveDrom signals
    s (str): set signal in wavedrom format
    r (str): reset signal in wavedrom format
    delay (int): delay in ns (assumes the latch as a whole has a delay)
    initial_value (str): "x" for unknown by default, can also be "0" or "1"
    """

    length = len(s)

    # Check S and R don't go low at the same time (undefined behavior)
    # Note that having them START both low is fine, that just results
    # in unknown output (x)
    for i in range(1, length):
        if s[i] == "0" and r[i] == "0":
            raise Exception("S and R can't go low at the same time")

    # THEN convert to binary form
    s = wavedrom_to_binary(s)
    r = wavedrom_to_binary(r)

    out = ""

    signal_value = initial_value

    # Process using the SR latch logic
    for i in range(length):

        # Look for set
        if s[i] == "1":
            signal_value = "1"
        # Look for reset
        if r[i] == "1":
            signal_value = "0"
        # Else don't change output value

        # If set and reset are high at the same time, it resets
        
        out += signal_value
    
    # Apply gate delay and put x (unknown) at the beginning
    out = ("x" * delay) + out[0:(length - delay)]

    # Convert back to wavedrom format
    out = binary_to_wavedrom(out)

    return out

def wavedrom_d_latch(d, e, delay=0, initial_value = "x"):
    """
    Emulates a D latch with WaveDrom signals
    D (str): data signal in wavedrom format
    E (str): enable signal in wavedrom format
    delay (int): delay in ns (assumes the latch as a whole has a delay)
    initial_value (str): "x" for unknown by default, can also be "0" or "1"
    """

    length = len(d)

    # Make sure a transition doesn't occur while D goes low
    for i in range(1, length):
        if e[i] == "0" and (d[i] == "0" or d[i] == "1"):
            raise Exception("E can't go low at the same time as a transition")

    # THEN convert to binary form
    d = wavedrom_to_binary(d)
    e = wavedrom_to_binary(e)

    out = ""

    signal_value = initial_value

    # Process using the D latch logic
    for i in range(length):

        # Take current d value if e is high
        if e[i] == "1":
            signal_value = d[i]
        # Else don't change output value
        
        out += signal_value
    
    # Apply gate delay and put x (unknown) at the beginning
    out = ("x" * delay) + out[0:(length - delay)]

    # Convert back to wavedrom format
    out = binary_to_wavedrom(out)

    return out

# def wavedrom_d_flip_flop(clk, d, q, en="", delay=0):
#     # Not done yet
#     pass

def make_wavedrom_link(title, sig_names, gen_sigs, fill_sig_names, link_text = "WaveDrom Link"):
    """
    Generates wavedrom related question or answer link in HTML

    Args:
        title (str): String to label timing diagram like "Question 2"
        sig_names (list): List of input signal names like ["a", "b"]
        gen_sigs (list): List of generated signals corresponding to sig_names 
        (in wavedrom format)
        fill_sig_names (list): List of signal names to hold space for
        students to complete -> ["a'","b'","ab'","F"]
        link_text (str): text for the link to appear as
        alternate (bool): whether to use GitHub (true) or Watson Wiki (false)
    """

    title_html = title.replace(' ','%20')
    
    lines_url = []
    for sig_name, sig in zip(sig_names, gen_sigs):
        line = f"{{name: \"{sig_name}\", wave: \"{sig}\"}},"
        lines_url.append(line)
    for sig_name in fill_sig_names:
        line = f"{{name: \"{sig_name}\", wave: ''}},"
        lines_url.append(line)

    url_gen = urllib.parse.quote("".join(lines_url))
    
    link = f"https://watsonwiki.binghamton.edu/wavedrom/editor.html?%7B%20head%3A%7Btext%3A%27{title_html}%27%7D%2C%0Asignal%3A%0A%5B%0A{url_gen}%5D%2C%0A%20%20foot%3A%7Btock%3A1%7D%0A%7D"

    # Convert to HTML link and make it open in new tab
    link_html = f"<a href=\"{link}\" target=\"_blank\">{link_text}</a>"

    return link_html

def to_alternate(link):

    """Converts Watson Wiki WaveDrom Link to GitHub Link"""

    link = link.replace("watsonwiki.binghamton.edu", "dougsummerville.github.io")
    link = link.replace("</a>", " (Alternate)</a>")

    return link


def make_wavedrom_image(title, sig_names, gen_sigs, fill_sig_names=[], out_filename="image.svg"):
    """
    Generates wavedrom image of specified signals
    Args:
        title (str): String to label timing diagram like "Question 2"
        sig_names (list): List of input signal names like ["a", "b"]
        gen_sigs (list): List of generated signals corresponding to sig_names
        fill_sig_names (list): List of signal names to hold space for
        students to complete -> ["a'","b'","ab'","F"]. Empty if not specified
        out_filename (str): SVG output file
    """


    lines = []
    for sig_name, sig in zip(sig_names, gen_sigs):
        # Force sharp edges by replacing 1 and 0 with h and l
        sig = sig.replace("1", "h")
        sig = sig.replace("0", "l")
        
        line = f"{{name: \"{sig_name}\", wave: \"{sig}\"}},"
        lines.append(line)
    for sig_name in fill_sig_names:
        line = f"{{name: \"{sig_name}\", wave: ''}},"
        lines.append(line)

    code = " ".join(lines)

    code = '{signal: [ ' + code + '],  foot:{"tock":1},}'

    img = wavedrom.render(code)
    img.saveas(out_filename)
    

def to_regex(name, signal):
    """
    name: name of output signal like "f"
    signal: output wavedrom signal like "0...1..0."
    """

    # Escape the silly dots
    signal = signal.replace(".", "\\.")

    # Super-ultra-mega-monster regex, shoutout to the man himself Doug for this one
    regex_ans = f"""(?i:name\\s*:\\s*['"]{name}['"]\\s*,\\s*wave\\s*:\\s*['"]{signal}['"])"""
    return regex_ans
