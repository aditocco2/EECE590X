#!/bin/python3

import d2l
import random

pool = d2l.QuestionPool("Determine which encoding is correct","encodings.csv")


def html_table_by_column(headings, rows, columns):
    retval="<table><tr>"
    for h in headings:
        retval = retval + "<th>"+h+"</th>"
    retval = retval + "</tr>"
    for row in range(0,len(rows)):
        retval = retval + "<tr>"
        retval = retval + "<td>" + rows[row] + "</td>"
        for col in range(0,len(columns)):
            retval = retval + "<td>" + columns[col][row] + "</td>"
        retval = retval + "</tr>"
    retval = retval + "</table>"
    return retval


tasks = {
        "digital clock that displays the date and time" : (
            "months of the year",
            ["Jan","Feb","Mar","Apr","May","Jun",
             "Jul","Aug","Sep","Oct","Nov","Dec"]
        ),
        "digital Hebrew calendar that displays months" : (
            "months of the Hebrew calendar",
            ["Nisan","Iyar","Sivan","Tammuz","Av","Elul","Tishrei",
             "Heshvan","Kislev","Tevet","Shevat","Adar"]
        ),
        "digital astronomy clock that tracks the phases of the moon." : (
            "phases of the moon",
            ["new", "waxing crescent", "first quarter",
             "waxing gibbous", "full" , "waning gibbous",
             "last quarter", "waning crescent"
            ]
        ),
        "digital astrology device that shows the current zodiac sign" : (
            "zodiac signs",
            ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Sagittarius", "Capricorn"
            ]
        ),
        "digital fingerprinting device" : (
            "five fingers on two hands",
            ["Left Thumb", "Left Index", "Left Middle", "Left Ring",
             "Left Pinkie", "Right Thumb", "Right Index", "Right Middle",
             "Right Ring", "Right Pinkie"
            ]
        ),
        "digital astronomy device that to track the major and dwarf planets": (
            "major and dwarf planets",
            ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn",
             "Uranus", "Neptune","Ceres", "Pluto", "Haumea", "Makemake",
             "Eris"]
        ),
        "healthy fruit vending machine that will serve only fresh fruit": (
            "types of fruit the machine will sell",
            ["Apple", "Banana", "Orange", "Grape", "Pear", "Pineapple",
             "Strawberry", "Mango", "Watermelon", "Cherry"]
        ),
        "candy vending machine": (
            "types of candy the machine will sell",
            [ "Snickers","Hershey Chocolate Bar","Reese's Peanut Butter Cup",
            "Twix","Airheads","Sour Patch Kids","M&Ms","Nerds","Starbursts",
             "Skittles"
             ]
        ),
        "digital piano": (
            "musical notes",
            ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"
             ]
        ),
        "digital trivia device": (
            "U.S. states that star with the letter M",
            ["Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
             "Mississippi", "Missouri", "Montana", "Nebraska", "New Mexico" 
             ]
        ),
        "digital medical device": (
            "major organs in the human body",
            ["Brain","Heart","Lungs","Liver","Kidneys","Stomach","Pancreas",
             "Spleen","Gallbladde","Adrenal glands","Thyroid glands"
            ]
        ),
        "digital paint color device": (
            "colors on a color wheel",
            ["Red","Orange","Yellow","Green","Blue","Indigo","Violet",
             "Magenta","Cyan","Lime","Brown"
            ]
        ),
        "digital produce scale": (
            "common vegetables available for sale",
            ["Carrot","Broccoli","Celery","Tomato","Potato","Onion",
             "Pepper","Cucumber","Zucchini","Eggplant","Cauliflower"
            ]
        ),
        "digital trivia device": (
            "U.S. colonies in 1776",
            ["Connecticut","Delaware","Georgia","Maryland","Massachusetts",
             "New Hampshire","New Jersey","New York","North Carolina",
             "Pennsylvania","Rhode Island","South Carolina","Virginia"
             ]
        ),
        "digital trivia device": (
            "player positions in a baseball game",
            ["pitcher","catcher","first baseman","second baseman",
             "third baseman","shortstop","left fielder","center fielder",
             "right fielder"
             ]
        ),
        "soda vending machine": (
            "types of soda the machine will sell",
            [ "Coca-Cola","Pepsi","Dr Pepper","Sprite","Mountain Dew","Diet Coke","Diet Pepsi","Fanta","A&W Root Beer","Coke Zero"
             ]
        )
        }
codes = [f"{i:04b}" for i in range(0,16)]
encodings = [ 
             codes, #straight binary
             codes[::-1], #backwards
             [ i for i in codes[1:15]+codes[0:1]], #starting at 1
             [ i for i in codes[8:15]+codes[0:8]], #starting at 8
             [ i[::-1] for i in codes ], #bitwise reversed
             [ "0000","0001","0011","0010","0110","0111","0101","0100" ,
               "1100","1101","1111","1110","1010","1011","1001","1000"]#Gray
            ]

for task in tasks:
    for i in range(2): #two version of each question
        encoding = random.sample( encodings, 3 )
        #randomize one encoding
        encoding[random.randint(0,2)] = random.sample(encodings[0],16)
        is_correct = random.choices([True, False],k=3)
        for i in range(3):
            if is_correct[i] == False:
                idx1,idx2 = random.sample(range(len(tasks[task][1])),2)
                encoding[i][idx1] = encoding[i][idx2]
        qtext = (
            f"<p>A team of engineers is designing a {task}."
             " Three engineers were each tasked with designing a method for"
             " encoding the"
            f" {tasks[task][0]}: "
            )
        for item in tasks[task][1]:
           qtext = qtext + item + ", "
        qtext = qtext[:-2]
        qtext = qtext + ( 
          ". The encodings they came up with are shown"
          " in the table below.</p>"
            )
        qtext = qtext + html_table_by_column(
            ["Item to be Encoded","Engineer A's Encoding",
             "Engineer B's Encoding", "Engineer C's Encoding"],
            tasks[task][1],
            encoding
            )
        qtext = qtext + "<p>Which of the engineers' codes are correct?"
        qtext = qtext + " Select all that apply.</p>"
        question = d2l.MSQuestion(qtext, shuffle=False)
        engineers = ["A", "B", "C"]
        for i in range(3):
            points = 0
            if is_correct[i]:
                points=100
            question.add_answer("Engineer "+engineers[i],  points)
        pool.add_question(question)
pool.dump()
pool.package()
