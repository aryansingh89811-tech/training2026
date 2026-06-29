class A:
    def __init__(self):
        print("This is class A Constructor")

class B(A):
    pass
    # def __init__(self):
    #     print("This is class B Constructor")

class C(B):
    # def __init__(self):
    #     print("This is class C Constructor")
    pass

c=C()