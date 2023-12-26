def create_counter():
    flag = True
    n = 0

    def increment():
        nonlocal n
        n += 1
    
    def decrement():
        nonlocal n
        n -= 1

    def get_counter_value():
        return n

    while flag:
        inc_dec = str(input(">>> "))
        if inc_dec == "+":
            increment()
        elif inc_dec == "-":
            decrement()
        elif inc_dec == "stop":
            flag = False

        
        print(get_counter_value())
        
    return get_counter_value()

print(create_counter())
