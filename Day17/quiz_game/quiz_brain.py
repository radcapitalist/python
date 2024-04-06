
class QuizBrain:
    def __init__(self, questions):
        self._questions = questions
        self._question_number = 0
        self._n_correct = 0
        self._n_incorrect = 0

    def _get_curr_question(self):
        return self._questions[self._question_number - 1]
    
    def _is_answer_correct(self, str_answer, correct_answer):
        al = str_answer.lower()
        b_answer = True
        if al == "false" or al == "f":
            b_answer = False
        correct = b_answer == correct_answer
        if correct:
            print(f'{b_answer} is correct!')
        else:
            print(f'{b_answer} is incorrect!')
        return correct


    def _next_question(self):
        q = self._get_curr_question()
        str_answer = input(f'\nQ.{self._question_number}: {q.question} True or False? ')
        return self._is_answer_correct(str_answer, q.answer)

    def give_quiz(self):
        while self._question_number < len(self._questions):
            self._question_number += 1
            result = self._next_question()
            if result:
                self._n_correct += 1
            else:
                self._n_incorrect += 1
            print(f'Current score is: {self._n_correct}/{self._n_correct + self._n_incorrect}')

        print(f'\nYou got {self._n_correct} correct and {self._n_incorrect} wrong.')

