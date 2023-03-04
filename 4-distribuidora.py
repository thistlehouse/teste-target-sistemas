SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
OUTROS = 19849.53

totalFaturamento = SP+RJ+MG+ES+OUTROS

perPorEstado = {}

perPorEstado['sp'] = round(SP / totalFaturamento, 4)*100
perPorEstado['rj'] = round(RJ / totalFaturamento, 4)*100
perPorEstado['mg'] = round(MG / totalFaturamento, 4)*100
perPorEstado['es'] = round(ES / totalFaturamento, 4)*100
perPorEstado['outros'] = round(OUTROS / totalFaturamento, 3)*100

display = "SP: {0}%\nRJ: {1}%\nMG: {2}%\nES: {3}%\nOutros: {4}%"\
    .format(
        perPorEstado['sp'], 
        perPorEstado['rj'], 
        perPorEstado['mg'],
        perPorEstado['es'],
        perPorEstado['outros']
    )

print(display)

