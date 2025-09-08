import d2l
import wavedrom
from wave_utils.wave_utils import *

pool = d2l.QuestionPool("Examine Timing Diagram", "examine.csv")

for delay in range(4): # 0 to 3

    A = make_random_signal(20)
    B = make_random_signal(20)

    not_A = wavedrom_gate("not", A)
