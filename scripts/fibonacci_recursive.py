import matplotlib.pyplot as plt

def fibonacci(position):
    fibo = 0
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        fibo = fibonacci(position-1) + fibonacci(position-2)
        return fibo
    return -1

#TEST
#Fibonacci series
s=" "
m=[]
for val in range(20):
    n=fibonacci(val)
    s+=("{}, ".format(str(n)))
    m.append(n)
print(s)

plt.plot(range(20),m,'bo')
plt.show()
