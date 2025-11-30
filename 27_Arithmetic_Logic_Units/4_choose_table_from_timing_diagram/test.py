import wave_utils.wave_utils as wu
import image_utils.image_utils as img

opcodes = ["00", "01", "10", "11"]
operations = ["F = A", "F = B", "F = A + B", "F = A - B"]

A = wu.make_random_buses(20, 4)
B = wu.make_random_buses(20, 4)
op = wu.make_random_timing_of_buses(opcodes, 20)

F = wu.wavedrom_alu(A, B, op, opcodes, operations)

print(A)
print(B)
print(op)
print(F)

wu.make_wavedrom_image_with_buses("test", ["A", "B", "opcode", "F"],
                                  [A, B, op, F], "test.svg")
img.svg2png("test.svg", "test.png")