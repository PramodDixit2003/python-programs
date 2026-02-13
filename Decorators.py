import time
def execute(function):
    def work():
        start_time=time.time()
        function()
        end_time=time.time()
        final_time=end_time-start_time
        print(f"execution time of {function.__name__} : {final_time:.6f}")
    return work
@ execute
def loop():
    for i in range(1,5000):
        ...
@ execute
def fun():
    print("hello world")
    print("Hi kaise ho" ,"")
loop()
fun()
def foodready(cooking):
    def work():
        print("bought vegetables")
        print("washing vegetables")
        cooking()
        print("food is ready")
    return work

@foodready
def cooking ():
    print("we are cooking something ")
cooking()
