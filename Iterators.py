# This is a program for iterators
class counter:
    def __init__(self,val):
        self.val=val
    def __iter__(self):
        print("I just passed an iterator")
        return counter(3)
    def __next__(self):
        if self.val<=10:
            v=self.val
            self.val+=1
            return v
        else:
            raise StopIteration
for num in counter(1):
    print(num)