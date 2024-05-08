class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, que_ans):
        if que_ans.lower() == user_answer.lower():
            print("You got it right!!")
            self.score += 1
        else:
            print("You got it Wrong!!")

        print(f"The correct answer is {que_ans}.")


    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}:- {current_question.question} (True / False)?: ")
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is {self.score} / {self.question_number}.")
        print("\n")