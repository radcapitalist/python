
class QuizBrain:
    def __init__(self, questions):
        self._questions = questions
        self._question_number = 0
        self._n_correct = 0
        self._n_incorrect = 0

    def _next_question(self):
        q = None
        if self._question_number <= len(self._questions):
            q = self._questions[self._question_number - 1]
        if q:
            str_answer = input(f'\nQ.{self._question_number}: {q.question} True or False? ').lower()
            if str_answer == 'false':
                answer = False
            else:
                answer = True
            print(f'Your answer was: {answer}')
            if answer == q.answer:
                print("Correct!")
                return True
            else:
                print("Incorrect!")
                return False

    def give_quiz(self):
        while self._question_number < len(self._questions):
            self._question_number += 1
            result = self._next_question()
            if result:
                self._n_correct += 1
            else:
                self._n_incorrect += 1

        print(f'You got {self._n_correct} correct and {self._n_incorrect} wrong.')

