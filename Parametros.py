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
    print('Você está \033[31mmuito abaixo do peso!\033[m Recomenda-se procurar um profissíonal de nutrição e educador físico!')
elif 17 <= imc <= 18.4:
    print('Você está \033[33mabaixo do peso\033[m, {}! Recomenda-se buscar um profissíonal da área de nutrição para auxilia-lo'.format(nome))
elif 18.5 <= imc <= 24.9:
    print('Você está no \033[32mpeso ideal\033[m, {}. Parabéns!'.format(nome))
elif 25 <= imc <= 29.9:
    print('Você está \033[33macima do peso\033[m, {}! Recomenda-se procurar um nutricionista e um educador físico.'.format(nome))
elif 30 <= imc <= 34.9:
    print('Cuidado, {}! Você está em \033[31mobesidade grau I\033[m ! Procure um nutricionsta e um educador físico!'.format(nome))
elif 35 <= imc <= 40:
    print('Cuidado, {}! Voce está em \033[31mobesidade grau II!\033[m Procure um nutricionista e ducador físico!'.format(nome))
else:
    print('Você está em \033[31mobesidade grau III\033[m, {}! Muito cuidado! Procure um clínico geral, nutricionsta e educador físico urgente!'.format(nome))
