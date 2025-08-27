
import d2l
import random

pool = d2l.QuestionPool( "Examples of encoding", "pool.csv" )
enc_ex = {
        #It is important that the answers are all exactly the same
        "Writing the length and width of a room into a written representation on a" \
                "piece of paper" : 0,
        "Interpreting a number on a cash register as the price of " \
                "an item, in dollars" : 0,
        "Representing an arbitrary piece of information as a short unique " \
                "sequence of decimal numbers" : 1,#
        "Representing the color of a paint in a can using a six-digit number" \
                : 1,
        "Copying a six-digit number from one piece of paper to another" \
                : 0,
        "Assigning numerical codes to books (ISBN)" : 1,
        "Using ASL rather than spoken language" \
                : 1,
        "Reading a book out loud so it can be transcribed on another " \
                "piece of paper" : 0,
        "Typing a message on a keyboard" : 0,
        "Putting an item on a shelf at the grocery store" : 0, 
        "Counting how many students are in a class" : 0,
        "Representing a melody using sheet music" : 1,
        "Assigning a unique code to every item at the grocery store" : 1, 
        "Representing a website URL as a scannable QR code" : 1,
        "Assigning a distinctive account number to every bank account" \
                : 1,
        "Labeling each apartment in a building with its own number" : 1,
        "Representing web pages as unique URLs" : 1,
        "Copying excerpts of a web page into Microsoft Word" : 0,
        "Copying a passage from a book into a notebook" : 0,
        "Referring to a student by their BNumber in an online " \
                "administrative system, rather than their name" : 1, # 12 true, 8 false
        "Using an emoji to express an emotion in a text message" \
                : 0, #
        "Dialing a number to call someone on the phone, rather than " \
                "their name" : 1,
        "Referring to the location of a given building as a combination " \
                "of a street name and number, rather than coordinates on" \
                " a map" : 1,
        "Copying and pasting a paragraph from a PDF into a submission box" \
                : 0,
        "Assigning a student to a class" : 0,
        "Pasting a clickable URL into a Microsoft Word document" : 0
        } # make false examples of things that aren't countable; 

for i in range(50):
    choices = random.sample( sorted(enc_ex) , 5)

    qtext = f"<p>Which of the following are examples of encoding? " \
            f"<i>Select all that apply.</i></p>"

    question = d2l.MSQuestion( qtext )

    for example in choices:
        question.add_answer( f"{example}", is_correct = (enc_ex[example]))
    pool.add_question( question )

pool.dump()
pool.package()
