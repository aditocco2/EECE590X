import d2l
import random

pool = d2l.QuestionPool("Basic Absorption Question MAT", "pool.csv")

number_questions = 50

X_expressions = ["bc", "bd", "b'c", "b'd", "bc'", "bd'",
                     "(b+c)", "(b+d)", "(b'+c)", "(b'+d)", "(b+c')", "(b+d')",
                     "b'c'd'", "b'c'd", "b'cd'", "b'cd", "bc'd'", "bc'd", "bcd'", "bcd",
                     "(b'+c'+d')", "(b'+c'+d)", "(b'+c+d')", "(b'+c+d)",
                     "(b+c'+d')", "(b+c'+d)", "(b+c+d')", "(b+c+d)"]


for i in range(number_questions):
    abs1_or = {"a + aX" : "a",
               "a' + a'X" : "a'"}
    abs1_and = {"a(a + X)" : "a",
                "a'(a' + X)" : "a'"}
    abs2_or = {"a + a'X" : "a + X",
               "a' + aX" : "a' + X"}
    abs2_and = {"a(a' + X)" : "aX",
                "a'(a + X)" : "a'X"}
  
    match_list = [random.choice(list(abs1_or)), random.choice(list(abs1_and)),
                  random.choice(list(abs2_or)), random.choice(list(abs2_and))]

    X_substitution = random.choice(X_expressions)

    choice_list = [abs1_or[match_list[0]], abs1_and[match_list[1]],
                   abs2_or[match_list[2]], abs2_and[match_list[3]]]
    
    question_text = "Match each of the following expressions with its reduced form."


    question = d2l.MQuestion(question_text)

    question.add_answer("", "a")
    question.add_answer("", "a'")
    question.add_answer("", f"a + {X_substitution}")
    question.add_answer("", f"a' + {X_substitution}")
    question.add_answer("", f"a{X_substitution}")
    question.add_answer("", f"a'{X_substitution}")

    for j in range(4):
        match_list[j] = match_list[j].replace("X", X_substitution)
        choice_list[j] = choice_list[j].replace("X", X_substitution)

        question.add_answer(match_list[j], choice_list[j])

    pool.add_question(question)

pool.dump()
pool.package()
