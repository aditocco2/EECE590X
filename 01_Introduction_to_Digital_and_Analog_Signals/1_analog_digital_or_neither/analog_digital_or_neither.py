import d2l
import random

pool = d2l.QuestionPool( "Determine signal type", "pool.csv" )
sig_type = {
        #It is important that the answers are all exactly the same (analog != Analog)
        "The exact amount of time left until the 9th of August" : "Analog",
        "The exact temperature outside of the University Union" : "Analog",
        "The rhythm of your pulse as it varies with each heartbeat" : "Analog",
        "The rate of rainfall during a thunderstorm" : "Analog",
        "The volume of a song on the radio" : "Analog",
        "Wind speed on the top of a mountain" : "Analog",
        "The pitch of an opera singer during their debut" : "Analog",
        "How far a steering wheel has been turned" : "Analog",
        "The height of a growing sapling over a decade" : "Analog",
        "Blood oxygen levels of a boxer during a match" : "Analog",
        "The amount of water coming out of the end of a water slide" : "Analog",
        "Body temperature during a night's sleep in a hotel bed" : "Analog",
        "The intensity of sunlight coming through your dorm window during the sunrise" : "Analog",
        "The pressure in your tires over the course of a New York winter" : "Analog",
        "The temperature of your coffee over the course of your digital logic class" : "Analog",
        "The pressure of your fingers on your phone screen as you type an email" : "Analog",
        "The the exact distance from the ground of a falling leaf" : "Analog",
        "The number of sunrises left until the the 9th of August" : "Digital",
        "The number of days in February" : "Digital",
        "The number of hairs in your head" : "Digital",
        "The seated position of a light switch" : "Digital",
        "The amount of cans in a vending machine" : "Digital",
        "The seconds left on a basketball shot clock" : "Digital",
        "The tv channel number as your friend flips through" : "Digital",
        "The state of a motion activated light" : "Digital",
        "The state of a traffic light" : "Digital",
        "The number of USB devices that are correctly plugged into your laptop right now" : "Digital",
        "The reading of barcode scanner" : "Digital",
        "How many teeth you've had in your life" : "Digital",
        "The amount of US Dollars in someone's bank account" : "Digital",
        "The state of your connection to a vpn" : "Digital",
        "The number of pencils in your bag" : "Digital",
        "The exact number of fingers you are currently using": "Digital",
        "The number of cookies in a cookie jar": "Digital",
        "The exact number of degrees per single radian": "Not a signal",
        "The number of days in August" : "Not a signal",
        "The value of Pi" : "Not a signal",
        "The amount of letters in the word 'combination'" : "Not a signal",
        "Your social security number" : "Not a signal",
        "The barcode on your favorite box of cereal" : "Not a signal",
        "The speed of light" : "Not a signal",
        "Acceleration due to gravity" : "Not a signal",
        "Your birthdate" : "Not a signal",
        "The exact number of days in a week" : "Not a signal",
        "Your legal name" : "Not a signal",
        "The weight of a kilogram" : "Not a signal",
        "The number of seconds in a minute" : "Not a signal",
        "The time zone that Washington DC is in" : "Not a signal",
        "Your blood type" : "Not a signal",
        "The day Star Wars was released" : "Not a signal",
        "The value of the smallest prime number" : "Not a signal"
        }

for i in range(51):
    choices = random.sample( sorted(sig_type) , 9)

    qtext = "For each of the descriptions below, determine whether the" \
           " description refers to an analog signal, digital signal," \
           " or is not a signal."

    question = d2l.MQuestion( text=qtext, points=10, shuffle=False )

    for sig in choices:
        question.add_answer( sig, sig_type[sig])
    pool.add_question( question )

#pool.dump()
pool.package()
