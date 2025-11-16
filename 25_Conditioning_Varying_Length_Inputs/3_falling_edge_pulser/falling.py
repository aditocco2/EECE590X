import d2l
import image_utils.image_utils as im

pool = d2l.QuestionPool("Falling Edge Pulser")

patterns = ["00", "01", "10", "11"]

# Coords go from bottom up cause right FF is older input
not_coords = [(1020, 150), (1020, 90)]

q_text = "<p> Suppose that you wanted a pulse to be sent out when you <i>let go</i> of the button \
    rather than when you first press it down. Would the design above be correct? </p>"

for pattern in patterns:
    
    image_name = f"pattern_{pattern}.png"

    if pattern != "11":
        # Create a new list of coords based on where the sequence has 0s
        coords_to_paste = [not_coords[i] for i in range(len(not_coords)) if pattern[i] == "0"]
        # Put NOT gates in the appropriate spots
        im.paste_images("pattern_11.png", image_name, "NOT.png", coords_to_paste, 0.3)

    question = d2l.MCQuestion(q_text, shuffle=False)
    question.add_image(f"/imagepools/quantumbeef/{image_name}")

    if pattern == "10":
        question.add_answer("Yes", 100)
        question.add_answer("No", 0)
    else:
        question.add_answer("Yes", 0)
        question.add_answer("No", 100)

    pool.add_question(question)

pool.package()

