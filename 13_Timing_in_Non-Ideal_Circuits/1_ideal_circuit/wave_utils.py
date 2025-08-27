import random
import urllib.parse

def make_random_signal(length):

    """
    Returns a randomized binary signal in both binary form (00011000)
    and wavedrom form (0..1.0..)
    The binary signal is returned as an int
    """

    binary = []
    wavedrom = []

    # Pick random points for the signal to toggle
    num_toggles = random.choice([2,3,4,5])
    toggle_pts = random.sample(range(1,length), num_toggles)

    signal_value = random.choice([0, 1])
    binary.append(signal_value)
    wavedrom.append(signal_value)

    # Generate the signals
    for i in range(length - 1):
        # If it's time to toggle, toggle the signal
        if i in toggle_pts:
            signal_value = 1 - signal_value
            # When toggling, put the 0 or 1 in the wavedrom signal
            wavedrom.append(signal_value)
        # Otherwise put . in the wavedrom signal
        else:
            wavedrom.append(".")
        # Either way put the 0 or 1 in the binary signal
        binary.append(signal_value)

    # Turn lists into strings
    binary = [str(i) for i in binary]
    binary = "".join(binary)
    wavedrom = [str(i) for i in wavedrom]
    wavedrom = "".join(wavedrom)

    # Turn binary string into number (base 2)
    binary = int(binary, 2)

    return binary, wavedrom


def generate_wavedrom(head_text, sig_names, gen_sigs, fill_sigs = ["F"]):
    """
    Generates wavedrom related question text: copy & paste manual 
    wavedrom, url, and wiki url 

    Args:
        head_text (str): String to label timing diagram "EECE 251 HW 3 Question 2"
        gen_sigs (list): List of signal names that need generated exs -> ["a", "b"]
        fill_sigs (list): List of signal names to hold space for
        students to complete -> ["a'","b'","ab'","F"] (default output signal 'F')
    """
    head_text_html = head_text.replace(' ','%20')
    
    lines_url = []
    for sig in gen_sigs:
        line = f"{{name: \"{sig}\", wave: \"{sig}\"}},"
        lines_url.append(line)
    for sig in fill_sigs:
        line = f"{{name: \"{sig}\", wave: ''}},"
        lines_url.append(line)

    url_gen = urllib.parse.quote("".join(lines_url))
    
    lines_text = []
    for sig in gen_sigs:
        gen_wave = randomize_sig()
        line = f"{{name: \"{sig}\", wave: \"{gen_wave}\"}},"
        lines_text.append(line)
    for sig in fill_sigs:
        line = f"{{name: \"{sig}\", wave: ''}},"
        lines_text.append(line)
    text_gen = "<br/>    ".join(lines_text)
   
    return(f"<a rel=\"noopener\" href='https://watsonwiki.binghamton.edu/wavedrom/editor.html?%7B%20head%3A%7Btext%3A%27{head_text_html}%27%7D%2C%0Asignal%3A%0A%5B%0A{url_gen}%5D%2C%0A%20%20foot%3A%7Btock%3A1%7D%0A%7D' target=\"_blank\">"+\
           f"<pre>{{\nhead:{{text:\"{head_text}\"}},<br/>signal:[<br/>   {text_gen}<br/>],  foot:{{tock:1}}}}</pre></a>")

def make_question_text(title, sig_names, gen_sigs, fill_sig_names):
    """
    Generates wavedrom related question text: copy & paste manual 
    wavedrom, url, and wiki url 

    Args:
        title (str): String to label timing diagram "EECE 251 HW 3 Question 2"
        sig_names (list): List of signal names that need generated exs -> ["a", "b"]
        gen_sigs (list): List of generated signals corresponding to sig_names
        fill_sig_names (list): List of signal names to hold space for
        students to complete -> ["a'","b'","ab'","F"] (default output signal 'F')
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
    
    full_link = f"https://watsonwiki.binghamton.edu/wavedrom/editor.html?%7B%20head%3A%7Btext%3A%27{title_html}%27%7D%2C%0Asignal%3A%0A%5B%0A{url_gen}%5D%2C%0A%20%20foot%3A%7Btock%3A1%7D%0A%7D"

    # lines_text = []
    # for sig_name, sig in sig_names, gen_sigs:
    #     line = f"{{name: \"{sig_name}\", wave: \"{sig}\"}},"
    #     lines_text.append(line)
    # for sig_name in fill_sig_names:
    #     line = f"{{name: \"{sig_name}\", wave: ''}},"
    #     lines_text.append(line)
    # text_gen = "<br/>    ".join(lines_text)
   
    #return(f"<a rel=\"noopener\" href='https://watsonwiki.binghamton.edu/wavedrom/editor.html?%7B%20head%3A%7Btext%3A%27{title_html}%27%7D%2C%0Asignal%3A%0A%5B%0A{url_gen}%5D%2C%0A%20%20foot%3A%7Btock%3A1%7D%0A%7D' target=\"_blank\">"+\
    #       f"<pre>{{\nhead:{{text:\"{title}\"}},<br/>signal:[<br/>   {text_gen}<br/>],  foot:{{tock:1}}}}</pre></a>")

    return full_link