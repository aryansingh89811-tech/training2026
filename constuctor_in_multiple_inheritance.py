class Theroy:
    def __init__(self):
        print("This is theory constructor")

class Sessional:
    def __init__(self):
        print("This is Sessional constructor")
# MRO Method Resolution Order (MRO)
class Result(Sessional,Theroy):
    pass

s=Result()
