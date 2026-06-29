class Theroy:
    def get_theory_marks(self):
        print("This is theory Marks")

class Sessional:
    def get_sessional_marks(self):
        print("This is Sessional Marks")

class Result(Theroy,Sessional):
    pass

s=Result()
s.get_sessional_marks()
s.get_theory_marks()