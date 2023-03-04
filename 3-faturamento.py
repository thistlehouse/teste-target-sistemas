import json

with open('dados.json') as arquivoFaturamento:   
	faturamento = arquivoFaturamento.read()
        
faturamentoMensal = json.loads(faturamento)

def exlcuiValoresZerados(arr):
    newArr = []

    for i in range(0, len(arr)):
        if arr[i]['valor'] > 0:
            newArr.append(arr[i])

    return newArr

def bubbleSort(arr):    
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):                
            if arr[j+1]['valor'] < arr[j]['valor']:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

def totalFaturamentoMensal(faturamentoMensal):
    total = 0
    
    for i in range(0, len(faturamentoMensal)-1): 
        total = total + faturamentoMensal[i]['valor']
    
    return round(total, 2)

def mediaFaturamentoMensal(faturamentoMensal, totalFaturamento):
    mediaFaturamento = 0 
    totalFaturamento = totalFaturamento
    mediaFaturamento = totalFaturamento / len(faturamentoMensal)

    return round(mediaFaturamento, 2)

def diasSuperioresMediaMensal(faturamentoMensal, totalFaturamento):
    diasSuperiores = []
    mediaFaturamento = mediaFaturamentoMensal(faturamentoMensal, totalFaturamento)

    for i in range(0, len(faturamentoMensal)-1):
        if faturamentoMensal[i]['valor'] > mediaFaturamento:
            diasSuperiores.append(faturamentoMensal[i])
    print(len(diasSuperiores))
    return diasSuperiores

def mostrarValoresSuperiores(faturamentoMensalSuperior):
    print("Números de dias onde o faturamento foi superior a média: ", len(faturamentoMensalSuperior))
    for i in range(0, len(faturamentoMensalSuperior)):
        print(faturamentoMensalSuperior[i])
    
faturamentoMensalSemZeros = exlcuiValoresZerados(faturamentoMensal)
totalFaturamento = totalFaturamentoMensal(faturamentoMensalSemZeros)
diasSuperiores = diasSuperioresMediaMensal(faturamentoMensalSemZeros, totalFaturamento)
mostrarValoresSuperiores(diasSuperiores)

faturamentoMensalOrdenado = bubbleSort(faturamentoMensalSemZeros)
menorFaturamento = faturamentoMensalOrdenado[0]
maiorFaturamento = faturamentoMensalOrdenado[len(faturamentoMensalOrdenado)-1]

print("Menor faturamento do mês: ", menorFaturamento)
print("Maior faturamento do mês: ", maiorFaturamento)