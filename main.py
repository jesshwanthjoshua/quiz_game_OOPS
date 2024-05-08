from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for n in range(0, len(question_data)):
    que = question_data[n]['question']
    ans = question_data[n]['correct_answer']
    new_question = Question(que, ans)
    question_bank.append(new_question)

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz successfully.")
print(f"Your final score is {quiz.score} / {quiz.question_number}.")