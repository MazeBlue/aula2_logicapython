###Faça um programa, com:
# - uma função que necessite de
# - três argumentos, e 
# - a soma desses três argumentos.

def soma(a, b, c): # função soma com os argumentos a, b, c que serão somados ao serem chamados
    return a + b + c # return indica quye a função deve retornar o resultado da expressão

### linha 10 à 13: o sistema solicita ao usuário valores, mas por ser input, é armazenado como string
# Portanto, faz-se a conversão de tipo string para inteiro
a= int(input("Informe o primeiro valor: "))
b= int(input("Informe o segundo valor: "))
c= int(input("Informe o terceiro valor: "))

# 16: a função soma é chamada com os valores armazenados nas variaveis a, b, c informadas pelo usuário
#e o resultado é armazenado na variavel resultado
resultado= soma(a, b, c)

#20: mostra o resultado final
print("O resultado de", a, "+", b, "+", c, "=", resultado)