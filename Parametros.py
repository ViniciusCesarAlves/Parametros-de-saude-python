import time, math
nome = str(input('Olá! Qual o seu nome? '))
peso = float(input('{}, qual o seu peso atual em Kg? '.format(nome)))
altura = float(input('Qual é a sua altura em cm, {}?'.format(nome)))
altura = altura / 100
foco = str(input('O seu foco é em emagrecer ou ganhar massa múscular? [emagrecer ou massa]'))
imc = peso/altura**2
print('Processando os seus dados.')
print('AGUARDE...')
time.sleep(3)
print('Aqui estão os seus parametros para uma vida mais saudável!')
time.sleep(1)
if imc < 17:
    print('Você está muito abaixo do peso! Recomenda-se procurar um profissíonal de nutrição e educador físico!')
elif 17 <= imc <= 18.4:
    print('Você está abaixo do peso, {}! Recomenda-se buscar um profissíonal da área de nutrição para auxilia-lo'.format(nome))
elif 18.5 <= imc <= 24.9:
    print('Você está no peso ideal, {}. Parabéns!'.format(nome))
elif 25 <= imc <= 29.9:
    print('Você está acima do peso, {}! Recomenda-se procurar um nutricionista e um educador físico.')
elif 30 <= imc <= 34.9:
    print('Cuidado, {}! Você está em obesidade grau I! Procure um nutricionsta e um educador físico!'.format(nome))
elif 35 <= imc <= 40:
    print('Cuidado, {}! Voce está em obesidade grau II! Procure um nutricionista e ducador físico!'.format(nome))
else:
    print('Você está em obesidade grau III, {}! Muito cuidado! Procure um clínico geral, nutricionsta e educador físico urgente!'.format(nome))
