from Question import Question
import random
import sys

question_prompts = [
    "What is the name of a lead singer of Queen?\n(a) Freddie Mercury\n(b) Brian May\n(c) Roger Taylor\n\nYour answer: ",
    "Who plays the lead guitar in Queen?\n(a) Freddie Mercury\n(b) John Deacon\n(c) Brian May\n\nYour answer: ",
    "Who plays the bass guitar in Queen?\n(a) Roger Taylor\n(b) John Deacon\n(c) Brian May\n\nYour answer: ",
    "When was the Bohemian Rhapsody released?\n(a) 1974\n(b) 1975\n(c) 1976\n\nYour answer: ",
    "Which album was illustrated with a giant robot?\n(a) News of the world\n(b) Innuendo\n(c) The Game\n\nYour answer: ",
    "Who was Queen engineer in 1975?\n(a) Queen themselves\n(b) Reinhold Mack\n(c) Roy Thomas Baker\n\nYour answer: ",
    "\"(...) and I advertise a soul for sale or rent...\" is lyrics from:\n(a) Save me\n(b) It's a hard life\n(c) Love of my life\n\nYour answer: ",
    "He was the quiet one and turned to be our secret weapon. Who was it?\n(a) Roger Taylor\n(b) Brian May\n(c) John Deacon\n\nYour answer: ",
    "Freddie was born in:\n(a) London, UK\n(b) Zanzibar\n(c) Bombay, India\n\nYour answer: ",
    "Brian May built his own guitar using parts of:\n(a) a fireplace\n(b) a motorcycle springs\n(c) both\n\nYour answer: ",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "a"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "a"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "c"),
]

random.shuffle(questions)


def my_print(text):
    sys.stdout.write(str(text))
    sys.stdout.flush()


def run_test(questions):
    i = 1
    score = 0
    score_perc = 0
    for x in questions:
        my_print(i)
        my_print(". ")
        answer = input(x.prompt)
        if answer == x.answer:
            score += 1
            print("Correct!\n")
        else:
            print("Wrong!\n")
        i += 1
    score_perc = 100 * (score / len(questions))
    print("You got " + str(score) + "/" + str(len(questions)) +
          " correct. This is " + format(score_perc, '.2f') + "%.")
    if score_perc < 30:
        print("Oh dear, that's miserable...")
    elif score_perc < 50:
        print("Darling, you need to learn a lot more...")
    elif score_perc < 65:
        print("You know something, but need to learn more, darling...")
    elif score_perc < 80:
        print("Not bad, keep going, dear!")
    elif score_perc < 90:
        print("Almost there, my dear!")
    elif score_perc >= 90 and score_perc < 100:
        print("Almost perfect, dear!")
    elif score_perc == 100:
        print("You nailed it, darling!")


run_test(questions)
