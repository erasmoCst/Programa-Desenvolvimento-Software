# A partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua
# classe eleitoral, sabendo que menores de 16 não votam (não votante), que o voto é
# obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que o voto é opcional
# para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo).

idade = int(input("Informe a idade: "))

if idade < 16:
    print("Não votante.")
elif idade >= 18 and idade < 65:
    print("Eleitor obrigatório!")
else:
    print("Eleitor facultativo!")
