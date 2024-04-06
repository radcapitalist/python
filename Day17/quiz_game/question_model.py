
class Question:
    def __init__(self, question, answer):
        self._question = question
        self._answer = bool(eval(answer))

    __slots__ = ['_question', '_answer']

    def __repr__(self):
        return f"Question('{self.question}', '{self.answer}')"

    @property
    def question(self):
        return self._question
    
    @property
    def answer(self):
        return self._answer
    

