def fibonacci(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    
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