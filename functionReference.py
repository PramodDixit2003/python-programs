def taker(val):
    def bigwork(function):
        def work():
            for i in range(val):
                    print(i+1)
                    print("----------Start---------------")
                    function()
                    print("----------Stop-----------------")
        return work
    return bigwork
@taker(5)
def function():
    print("I am being called!")
function()


