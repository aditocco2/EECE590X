import random
import urllib.parse

def randomize_sig():
    num_transitions = random.choice([2,3,4,5])
    trans_index = random.sample(range(1,20), num_transitions)
    wave = []
    first = True
    first_trans = random.choice(['h','l'])
    wave.append(first_trans)
    letter = ''

    for i in range(19):
        if i in trans_index:
            if first:
                letter = 'h' if first_trans == 'l' else 'l'
                first = False
            else:
                letter = 'h' if letter == 'l' else 'l'
            wave.append(letter)

        else:
            wave.append('.')
    return(''.join(wave))


def generate_wavedrom(head_text, gen_sigs, fill_sigs = ["F"]):
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
        gen_wave = randomize_sig()
        line = f"{{name: \"{sig}\", wave: \"{gen_wave}\"}},"
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
