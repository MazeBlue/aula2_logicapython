###faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
# ou em galões de 3,6 litros, que custam R$ 25,00.
# 1- Informe ao usuário as quantidades de tinta a serem compradas - em litros ok
# e os respectivos preços em 3 situações:
# 2- comprar apenas latas de 18 litros;
# 3- comprar apenas galões de 3,6 litros;
# 4- misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
# considere latas cheias.

loja= "Re-paginada 2!"
print("Olá, bem-vindx a", loja, "Possuimos uma variedade de tintas para repaginar seu espaço, nessa atualização informaremos a quantidade correta de litros, entre latas e galões, para você evitar desperdicio!")

cobertura_tinta= 1/6
litro_lata= 18
preco_lata= 80.00
galao_tinta= 3.6
preco_galao= 25.00
extra= 0.10


mt_quadrado= float(input("Informe o tamanho do metro quadrado a ser pintado:"))
qtd_tinta_mtqd= int((mt_quadrado * cobertura_tinta) * (1 + extra) + 0.5)

qtd_latas= int((qtd_tinta_mtqd/litro_lata)*(1+extra) + 0.5)
qtd_galao= int((qtd_tinta_mtqd/galao_tinta)*(1+extra) + 0.5)


valor_total_lata= qtd_latas * preco_lata
print("Esse é o valor total lata", valor_total_lata)
valor_total_galao= qtd_galao * preco_galao
print("Esse é o valor total galao", valor_total_galao)


sobra_tinta_lata_litro= (qtd_latas * litro_lata) - qtd_tinta_mtqd
print("Essa é a sobra de lata", sobra_tinta_lata_litro)
sobra_tinta_galao_litro= int((qtd_galao * galao_tinta) - qtd_tinta_mtqd)
print("Essa é a sobra de galao", sobra_tinta_galao_litro)

melhor_opcao_compra= qtd_tinta_mtqd 

preco_total_combinacao = ((qtd_latas * preco_lata) + (qtd_galao * preco_galao))
litros_economizados = ((qtd_latas * litro_lata + qtd_galao * galao_tinta) - qtd_tinta_mtqd)
economia_total = ((qtd_latas * preco_lata + qtd_galao * preco_galao) - preco_total_combinacao)


print("1- A quantidade de tinta em litros necessária para pintar", mt_quadrado,"m² é: ", qtd_tinta_mtqd,"Litros")
print("2- A quantidade de latas de tinta de 18L para pintar o m² informado é: ", qtd_latas, "latas de tinta e gastará R$", valor_total_lata, "reais")
print("3- A quantidade de galões de tinta com 3.6L para pintar o m² informado é: ", qtd_galao, "galão de tinta e gastará R$", valor_total_galao, "reais")
print("4- Dos", mt_quadrado, "m² informados, temos a sobra de:\n-",sobra_tinta_lata_litro,"Litros na lata de tinta.\n-", sobra_tinta_galao_litro, "litros no galão de tinta")
print("5- O valor total economizado é, ", economia_total)
print("6- O valor total é de ", economia_total, "reais.")
print("Obrigada por escolher a", loja, "Volte sempre! <3")