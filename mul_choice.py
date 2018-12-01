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
    "Song \"Sheer Heart Attack\" was released on the album:\n(a) Queen II\n(b) Sheer Heart Attack\n(c) News of the world\n\nYour answer: ",
    "Which Queen album has the \'White side\' and the \'Black side\'?\n(a) Queen II\n(b) Sheer Heart Attack\n(c) Queen I\n\nYour answer: ",
    "What was the last song recorded by Freddie Mercury?\n(a) The Show Must Go On\n(b) Mother Love\n(c) Made in Heaven\n\nYour answer: ",
    "Which member of Queen has a Ph.D. in astrophysics?\n(a) Roger Taylor\n(b) Brian May\n(c) John Deacon\n\nYour answer: ",
    "It's a kind of magic was written for the movie:\n(a) Metropolis\n(b) Iron Eagle\n(c) Highlander\n\nYour answer: ",
    "Number 1 hit sigle in the USA was:\n(a) Another one bites the dust\n(b) We are the champions\n(c) Bohemian Rhapsody\n\nYour answer: ",
    "Innuendo Spanish guitar solo was played by:\n(a) Al di Meola\n(b) Brian May\n(c) Steve Howe\n\nYour answer: ",
    "Queen was officially established in:\n(a) 1968\n(b) 1970\n(c) 1973\n\nYour answer: ",
    "The band in which May and Taylor started to play together was:\n(a) Smile\n(b) Humpy Bong\n(c) The Hectics\n\nYour answer: ",
    "Queen at Live Aid concert was considered the best rock performance ever. It was in:\n(a) 1984\n(b) 1985\n(c) 1986\n\nYour answer: ",
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
    Question(question_prompts[10], "c"),
    Question(question_prompts[11], "a"),
    Question(question_prompts[12], "b"),
    Question(question_prompts[13], "b"),
    Question(question_prompts[14], "c"),
    Question(question_prompts[15], "a"),
    Question(question_prompts[16], "c"),
    Question(question_prompts[17], "b"),
    Question(question_prompts[18], "a"),
    Question(question_prompts[19], "b"),
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
        print("Impressive, my dear!")
    elif score_perc >= 90 and score_perc < 100:
        print("Almost perfect, dear!")
    elif score_perc == 100:
        print("You nailed it, darling! You are a true fan of Queen!")


run_test(questions)
