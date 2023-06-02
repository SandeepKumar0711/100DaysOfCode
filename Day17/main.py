from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random

question_bank = []

for data in question_data:
    question = Question(data['question'], data['correct_answer'])
    question_bank.append(question)

quiz_start = QuizBrain(random.choices(question_bank, k=10))

while quiz_start.still_has_question():
    quiz_start.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz_start.score}/{quiz_start.question_number}")