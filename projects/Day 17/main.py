from quiz_brain import QuizBrain
from question_model import Question
from data import question_data



if __name__ == '__main__':
    question_bank = []
    for qs in question_data:
        question_bank.append(Question(qs['text'], qs['answer']))

    quizBrain = QuizBrain(question_bank)

    while quizBrain.still_has_question():
        quizBrain.next_question()

    if quizBrain.question_number + 2 > len(quizBrain.questions_list):
        print(f"You've completed the quiz.\nYour final score was {quizBrain.score}/{len(quizBrain.questions_list)}")
