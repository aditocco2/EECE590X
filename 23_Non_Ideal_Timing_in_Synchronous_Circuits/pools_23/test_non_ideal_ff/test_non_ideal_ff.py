import wave_utils.wave_utils as wu
import image_utils.image_utils as img

setup = 3
hold = 2
c2q = 6

clk = wu.make_clock(30)

#clk=000001111100000111110000011111
a = "001111111000000000011111111111" # setup time edge case, should still be valid
b = "000000011111111111111100000000" # hold time edge case, should still be valid
c = "000111111000000000011110000000" # setup time violations
d = "000000111111111111111000000000" # hold time violations
e = "011111110000000000111111111111" # no violations or edge cases

sigs = [a, b, c, d, e]

names = "abcde"

for sig, name in zip(sigs, names):

    Q = wu.wavedrom_d_flip_flop(clk, sig, setup_time=setup, hold_time=hold, delay=c2q)

    wu.make_wavedrom_image("", ["clk", name, "Q"], [clk, sig, Q], out_filename=f"test_{name}.svg")
    img.svg2png(f"test_{name}.svg", f"test_{name}.png")
