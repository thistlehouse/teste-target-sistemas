faturamentoMensal = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

def ExlcuiValoresZerados(arr):
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
    
faturamentoMensalSemZeros = ExlcuiValoresZerados(faturamentoMensal)
totalFaturamento = totalFaturamentoMensal(faturamentoMensalSemZeros)
diasSuperiores = diasSuperioresMediaMensal(faturamentoMensalSemZeros, totalFaturamento)
mostrarValoresSuperiores(diasSuperiores)

faturamentoMensalOrdenado = bubbleSort(faturamentoMensalSemZeros)
menorFaturamento = faturamentoMensalOrdenado[0]
maiorFaturamento = faturamentoMensalOrdenado[len(faturamentoMensalOrdenado)-1]

print("Menor faturamento do mês: ", menorFaturamento)
print("Maior faturamento do mês: ", maiorFaturamento)