'''
Docstring do Algoritmo do CPF:

a - Cálculo do primeiro dígito

É separado os primeiros 9 dígitos do CPF (111.444.777) e multiplicado cada um dos números, da esquerda para a direita do índice 10 até o 2

1	1	1	4	4	4	7	7	7   CPF
10	9	8	7	6	5	4	3	2   Índice
10	9	8	28	24	20	28	21	14  Resultados

É multiplicado cada número do CPF por seu respectivo índice e posteriormente é somado os resultados encontrados: 10+9+8+28+24+20+28+21+14 = 162

Pega-se o resultado e multiplique-o por 10 e posteriormente divide-o por 11
Exemplo: 162 * 10 = 1620 
         1620 % 11 = 3

- Se o resto da divisão for maior que 9, então o dígito é igual a 0 (Zero).
- Se o resto da divisão for menor ou igual a 9, então o dígito verificador é igual ao resto

o resto equivale a 3, então o primeiro dígito é 3 (um número menor do que 9)

b - Cálculo do segundo dígito

É usado o primeiro dígito já calculado, porém, o índice irá variar de 11 a 2 da esquerda para a direita, visto que tem um dígito a mais

1	1	1	4	4	4	7	7	7	3   CPF
11	10	9	8	7	6	5	4	3	2   Índice
11	10	9	32	28	24	35	28	21	6   Resultados

É efetuada a soma dos resultados: 11+10+9+32+28+24+35+28+21+6 = 204

Pega-se o resultado e multiplique-o por 10 e posteriormente divide-o por 11

Exemplo: 204 * 10 = 2040
         2040 % 11 = 5

- Se o resto da divisão for maior que 9, então o dígito é igual a 0 (Zero).
- Se o resto da divisão for menor ou igual a 9, então o dígito verificador é igual ao resto

o resto equivale a 5, então o segundo dígito é 5 (um número menor do que 9

Logo o CPF inteiramente será igual a : 111.444.777-35.
'''



cpf = input('Digite seu CPF: ') \
    .replace('.', '') \
    .replace(' ', '') \
    .replace('-', '') # Ferramenta para o usuário digitar o CPF 
contador_1 = 10 # Contador que será usado como fator multiplicativo dos números do CPF
primeiros_nove_digitos = cpf[:9] # Pega os nove primeiros dígitos do CPF e aplica o algoritmo do CPF

if len(cpf) == 11 and cpf.isdigit():
        if len(primeiros_nove_digitos) == 9: # Quantidade de caracteres nos primeiros nove digitos do CPF devem ser igual a 9
            soma = 0 # Soma igual a 0 para ser adicionada conforme a progressão do loop for
            for indice_1, numero_1 in enumerate(primeiros_nove_digitos): # indica o indice e número na variável dos primeiros nove dígitos
                numeros_1 = contador_1 - indice_1 # Variavél usada para definir o multiplicador de determinado número, dependendo de sua posição (10 - índice)
                soma += int(numero_1) * numeros_1 # Soma mais soma é igual aos números multiplicados dos primeiros nove dígitos, variando entre 10 e 2 de acordo com o loop for
            numeros_multiplicados_1 = soma * 10 # Multiplica os números encontrados na soma por 10
            resto = numeros_multiplicados_1 % 11 # Calcula o resto dos números multiplicados (divide por 11 e define o resto da divisão)
        
            digito_1 = resto if resto <= 9 else 0 # Digito 1 do CPF escolhido - Equivale ao resto se o resto for menor ou igual a 9, se não for será igual a 0
            
            soma = 0 # Soma zerada para calcular o segundo dígito
            contador_2 = 11
            
            if len(primeiros_nove_digitos) + len(str(digito_1)) == 10: # Quantidade de caracteres nos primeiros nove digitos mais digito_1 devem ser igual a 10
                primeiros_dez_digitos = primeiros_nove_digitos + str(digito_1) # Primeiros_dez_digitos é igual aos primeiros_nove_digitos (xxxxxxxxx) + digito_1 (x)
                for indice_2, numero_2 in enumerate(primeiros_dez_digitos): # Indica o índice e número na variável dos primeiros dez digitos
                    numeros_2 = contador_2 - indice_2 # Variável para determinar o multiplicador de determinado número (11 - índice - pois foi adicionado um número a mais)
                    soma += int(numero_2) * numeros_2 # Soma mais soma é igual aos números multiplicados dos primeiros dez dígitos, variando entre 11 e 2 de acordo com o loop for
                numeros_multiplicados_2 = soma * 10 # Multiplica os números encontrados na soma por 10
                resto_2 = numeros_multiplicados_2 % 11 # Calcula o resto dos números multiplicados (divide por 11 e define seu resto)

                digito_2 = resto_2 if resto_2 <= 9 else 0 # Digito 2 do CPF escolhido - Equivale ao resto se o resto for menor ou igual a 9, se não for será igual a 0
                print(f'Os dois últimos dígitos do CPF são: {digito_1} e {digito_2}') # Printa "Os dois últimos dígitos do CPF são: x (digito_1), x (digito_2)"
                
                if primeiros_nove_digitos + str(digito_1) + str(digito_2) == cpf: # Se os dígitos encontrados equivalerem ao CPF, a condição é verdadeira
                    print('CPF é válido')
                
                else: # Por outro lado, é falsa, pois o CPF será inválido 
                    print('CPF é inválido')
                        
elif not cpf.isdigit(): # Se o usuário digitar letras (não sendo 11 caracteres especificamente) o programa vai pra essa linha de código
    print('Digite caracteres válidos') # Printa "Digite caracteres válidos"

else: # Se o usuário digitar números e não forem onze caracteres em específico, a linha de código vai parar aqui
    print('Digite onze números') # Printa "Digite onze números"









