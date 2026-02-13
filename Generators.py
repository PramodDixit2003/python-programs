def gen_num(start,end):
    for i in range(start,end+1):
        yield i    # It throws a value and pauses the execution of the function
for num in gen_num(10,15):
    print(num)