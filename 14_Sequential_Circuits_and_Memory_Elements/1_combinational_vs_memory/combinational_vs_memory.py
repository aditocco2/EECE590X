# WIP
import d2l
import random

pool = d2l.QuestionPool("Combinational vs. Memory (Matching)")

# Case matters!!!1
matches = [
    # 13 here
    ("Detecting whether the number of high inputs is even or odd", "Combinational"),
    ("Adding two binary numbers together", "Combinational"),
    ("Subtracting two binary numbers", "Combinational"),
    ("Finding the remainder when a number is divided by 8", "Combinational"),
    ("Turning on a light when your seatbelt is not fastened", "Combinational"),
    ("Implementing a Boolean sum of minterms", "Combinational"),
    ("Implementing a Boolean product of maxterms", "Combinational"),
    ("Showing a binary number as a hex digit on a 7-segment display", "Combinational"),
    ("Determining whether two binary numbers are equal", "Combinational"),
    ("Turning on a light when the fridge door is open", "Combinational"),
    ("Turning on the A/C when the temperature is above 72 degrees", "Combinational"),
    ("Turning an LED on when a button is pressed down", "Combinational"),
    ("Using a knob to set the heat on the stove", "Combinational"),

    # And 13 here
    ("Sounding an alarm if a door is propped open for too long", "Memory"),
    ("Beeping every few seconds if a device is low on battery", "Memory"),
    ("Repeatedly adding 1 to a number", "Memory"),
    ("Detecting someone's pulse", "Memory"),
    ("Setting a timer on the microwave", "Memory"),
    ("Having an LED stay on when you let go of a button", "Memory"),
    ("Keeping track of your maximum MPG on a road trip", "Memory"),
    ("Keeping a traffic light yellow for 5 seconds", "Memory"),
    ("Toggling case with the Caps Lock key", "Memory"),
    ("Reading a stream of bits sent through a USB cable", "Memory"),
    ("Updating the total cost as you scan each item at the store", "Memory"),
    ("Keeping a 7-day average of new cases of a disease", "Memory"),
    ("Turning off the screen when you leave for 15 minutes", "Memory")
]

for i in range(15):

    question = d2l.MQuestion("Choose whether each scenario below is best represented" \
                            " by a combinational circuit or a memory circuit.")

    random.shuffle(matches)
    rows = random.sample(matches, 10)
    
    for row in rows:
        question.add_answer(row[0], row[1])
    
    pool.add_question(question)

pool.dump()
pool.package()