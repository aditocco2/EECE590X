from wave_utils.wave_utils import *


# Actually just a test of the wavedrom DFF for now
clk = make_clock(20, 6, 2)
d = make_random_signal(20)

q = wavedrom_d_flip_flop(clk, d)

clk, d, q = [to_dotless(sig) for sig in [clk, d, q]]

for sig in [clk, d, q]:
    print(sig)