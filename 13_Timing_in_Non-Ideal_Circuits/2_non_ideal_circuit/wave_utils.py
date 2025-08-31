import random
import urllib.parse

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
        # Otherwise preserve the 1 or 0 and update what was last seen
        else:
            wavedrom += i
            signal_value = i

    return wavedrom

def wavedrom_gate(gate, a, b="", delay=0):
    """
    Puts two wavedrom signals of same length through a logic gate
    a, b: two wavedrom format signals (1..0.1..)
    gate: can be "or", "and", "not", "xor", "xnor", "nand", "nor", or "buf"
    delay: delay in ns to shift output
    """
    
    length = len(a)

    # Convert wavedrom signal to binary format
    a = wavedrom_to_binary(a)
    # Turn binary string into number (base 2)
    a = int(a, 2)

    # Do the same with b if specified
    if b:
        b = wavedrom_to_binary(b)
        b = int(b, 2)

    # Use bitwise logic to get the result
    if gate == "or":
        out = a | b
    elif gate == "and":
        out = a & b
    elif gate == "not":
        out = ~a
    elif gate == "nor":
        out = ~(a|b)
    elif gate == "xor":
        out = (a ^ b)
    elif gate == "xnor":
        out = ~(a ^ b)
    elif gate == "nand":
        out = ~(a & b)
    else:
        out = a

    # Bit mask to make it unsigned
    out = out & int("1" * length, 2)

    # Turn output back to string
    out = f"{out:0{length}b}"

    # Apply gate delay and put x (unknown) at the beginning
    out = ("x" * delay) + out[0:(length - delay)]

    # Convert back to wavedrom format
    out = binary_to_wavedrom(out)

    return out


def make_question_link(title, sig_names, gen_sigs, fill_sig_names, link_text = "WaveDrom Link"):
    """
    Generates wavedrom related question link in HTML

    Args:
        title (str): String to label timing diagram like "Question 2"
        sig_names (list): List of input signal names like ["a", "b"]
        gen_sigs (list): List of generated signals corresponding to sig_names
        fill_sig_names (list): List of signal names to hold space for
        students to complete -> ["a'","b'","ab'","F"]
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

def to_regex(name, signal):
    """
    name: name of output signal like "f"
    signal: output wavedrom signal like "0...1..0."
    """

    # Escape the silly dots
    signal = signal.replace(".", "\.")

    # Case insensitive, "name", name, "wave", signal, with anything in between
    regex_ans = f"(?i).*name.*{name}.*wave.*{signal}.*"
    return regex_ans
