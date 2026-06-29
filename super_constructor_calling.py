class A:
    def __init__(self):
        print("This is class A Constructor")

class B(A):
    def __init__(self):
        super().__init__()
        print("This is class B Constructor")

class C(B):
    def __init__(self):
        super().__init__() #call parent class constructor
        print("This is class C Constructor")


c=C()