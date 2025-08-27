#!/bin/python -B
import d2l
import random

pool = d2l.QuestionPool(
        "min_bits_to_encode",
        "mypool.csv"
        )

encoded_bits = {
        "The number of miles between your current position and any" \
                " point on the earth? The circumference of the earth" \
                " is approximately 24,902 miles." : "14",
        "Which day of the month is today" : "5",
        "The current state of a switch that is either pressed or" \
                " unpressed" : "1",
        "2017 unique values": "11",
        "The letters of the english alphabet": "5",
        "The possible percentage of engineers in a room" : "7",
        "The corners on the front side of a standard piece" \
                " of paper" : "2",
        "The number of bowling pins you knock down on your" \
                " first throw of a match" : "4",
        "The remaining score of a darts game to 301" : "9",
        "The minutes elapsed in the current hour" : "6",
        "The amount of paper remaining in a package of 250" \
                " sheets" : "8",
        "The names of 1000 dogs in a doggy day care" : "10",
        "The face value of a die after being rolled" : "3",
        "The result of a coin flip" : "1",
        "The number of unoccupied seats in a theater that" \
                " can fit 4,012 attendees" : "12",
        "The remaining parking spots in a 8063 capacity" \
                " garage" : "13",
        "The number of seats occupied in a 16,000 capacity" \
                " stadium" : "15",
        "The outcome after 16 coin flips" : "16",
        "The open parking spaces in a 300 car garage" : "9"
        }

for key in encoded_bits:
    question_text="<p>Enter the <i>minimum number</i> of bits required to </p>" \
            " encode the following information: " + key
    question = d2l.SAQuestion( question_text )
    question.add_answer(encoded_bits[key])
    question.add_feedback(str(encoded_bits[key]))

    pool.add_question(question)

pool.dump()
pool.package()
