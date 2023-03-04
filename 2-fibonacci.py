def fibonacci(n):
    if n < 0:
        print("n deve ser maior que 0")
    elif n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def imprimeSequecia(n):
    for i in range(0, n):
        print(fibonacci(i))

# teste
imprimeSequecia(9)

# imprimeSequecia(9)
# resultado:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21