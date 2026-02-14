class B:
    def __init__(self):
        self.val=0
    def __next__(self):
        self.val=self.val+1
        return self.val
class A:
    def __init__(self):
        self.val=5

    def __call__(self):
        print("I am called")
        print("Hahahahahahah")
    def __iter__(self):
        print("iter has been called")
        return self
    def __next__(self):
        self.val=self.val-1
        return self.val
       
a=A()

