
from question_model import Question
from data import question_data
from random import randint
from quiz_brain import QuizBrain

# Create our question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))

print(dir(QuizBrain))

qb = QuizBrain(question_bank)
qb.give_quiz()
