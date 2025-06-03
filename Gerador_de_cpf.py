import random

primeiros_nove_digitos = ''
for i in range(9): # For usado para gerar números até o índice 8 
    primeiros_nove_digitos += str(random.randint(0, 9)) # De acordo com o loop do índice, o programa irá gerar um inteiro de 0 a 9 aleatório

contador_1 = 10 # Contador que será usado como fator multiplicativo dos números do CPF

soma = 0 # Soma igual a 0 para ser adicionada conforme a progressão do loop for
for indice_1, numero_1 in enumerate(primeiros_nove_digitos): # indica o indice e número na variável dos primeiros nove dígitos
    numeros_1 = contador_1 - indice_1 # Variavél usada para definir o multiplicador de determinado número, dependendo de sua posição (10 - índice)
    soma += int(numero_1) * numeros_1 # Soma mais soma é igual aos números multiplicados dos primeiros nove dígitos, variando entre 10 e 2 de acordo com o loop for
    numeros_multiplicados_1 = soma * 10 # Multiplica os números encontrados na soma por 10
    resto = numeros_multiplicados_1 % 11 # Calcula o resto dos números multiplicados (divide por 11 e define o resto da divisão)

digito_1 = resto if resto <= 9 else 0 # Digito 1 do CPF escolhido - Equivale ao resto se o resto for menor ou igual a 9, se não for será igual a 0

soma = 0 # Soma zerada para calcular o segundo dígito
contador_2 = 11

primeiros_dez_digitos = primeiros_nove_digitos + str(digito_1) # Primeiros_dez_digitos é igual aos primeiros_nove_digitos (xxxxxxxxx) + digito_1 (x)
for indice_2, numero_2 in enumerate(primeiros_dez_digitos): # Indica o índice e número na variável dos primeiros dez digitos
    numeros_2 = contador_2 - indice_2 # Variável para determinar o multiplicador de determinado número (11 - índice - pois foi adicionado um número a mais)
    soma += int(numero_2) * numeros_2 # Soma mais soma é igual aos números multiplicados dos primeiros dez dígitos, variando entre 11 e 2 de acordo com o loop for
    numeros_multiplicados_2 = soma * 10 # Multiplica os números encontrados na soma por 10
    resto_2 = numeros_multiplicados_2 % 11 # Calcula o resto dos números multiplicados (divide por 11 e define seu resto)

digito_2 = resto_2 if resto_2 <= 9 else 0 # Digito 2 do CPF escolhido - Equivale ao resto se o resto for menor ou igual a 9, se não for será igual a 0

cpf_gerado = f'{primeiros_nove_digitos}{digito_1}{digito_2}' # Uma variavél que contém o CPF com os nove dígitos gerados aleatorimaente (no primeiro loop for) e os dígitos posteriores encontrados através do código (dos outros loops for)
print(cpf_gerado) # Irá printar um CPF aleatório de 9 números juntamente a seus dois dígitos (ex: xxxxxxxxxXX)
