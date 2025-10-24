import d2l
import wave_utils.wave_utils as wu
import image_utils.image_utils as img

pool = d2l.QuestionPool("SR Flip Flop Timing Diagram")

for _ in range(50):

    S = wu.make_random_signal(30, 6)
    R = wu.make_random_signal(30, 6)
    D = wu.make_random_signal(30)
    clk = wu.make_clock(30, 4, 2)

    Q = wu.wavedrom_d_flip_flop(clk, D, s=S, r=R)

    regex_ans = wu.to_regex("Q", Q)

    q_link = wu.make_wavedrom_link("SR Flip Flop Timing Diagram",
                                   ["S", "R", "D", "clk"],
                                   [S, R, D, clk], 
                                   ["Q"])
    
    a_link = wu.make_wavedrom_link("SR Flip Flop Timing Diagram Answer",
                                   ["S", "R", "D", "clk", "Q"],
                                   [S, R, D, clk, Q], 
                                   [])
    
    image_link = "/imagepools/quantumbeef/sr_ff_with_logic.png"

    q_text = f"<p>The diagram above shows a flip-flop  \
    with extra logic added in front to incorporate synchronous set and reset \
    signals. Click on the link below to open the problem in WaveDrom. Complete the timing \
    diagram, and paste <b>all</b> your code into the answer box.</p> \
    <p>{q_link}</p>"
    

    hint = 'Your wave for Q should have 30 characters and look \
    something like "xx0000111111110000000011111111".'

    feedback = f"<p>Here was the right answer: {a_link}</p>"

    question = d2l.SAQuestion(q_text)
    question.add_image(image_link)
    question.add_answer(regex_ans, is_regex=True)
    question.add_hint(hint)
    question.add_feedback(feedback)

    pool.add_question(question)

pool.package()