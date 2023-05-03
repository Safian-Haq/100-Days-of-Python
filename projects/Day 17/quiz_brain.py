class QuizBrain:

    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q. {self.question_number}: {self.questions_list[self.question_number].text} (True/False):")
        self.check_answer(user_answer)
        self.question_number += 1

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer):
        correct_answer = self.questions_list[self.question_number].answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Correct')
        else:
            print('Incorrect')
        print(f'Correct answer was: {correct_answer}')
        print(f'Current score : {self.score}\n')
