def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    the_sequence=[0,1]
    for i in range(2,n):
        next_number=the_sequence[-1]+the_sequence[-2]
        the_sequence.append(next_number)
    return the_sequence
number=fibonacci(15)
print(number)

