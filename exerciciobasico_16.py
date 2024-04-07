### 16. Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

loja= "Re-paginada!"
print("Olá, bem-vindx a", loja, "Possuimos uma variedade de tintas para a repaginada do seu espaço, informe os dados que o sistema pedirá e terá a quantidade necessária para pintar seu espaço ;)")

cobertura_tinta= 1/3
litro_lata= 18
preco_lata= 80.00


mt_quadrado= float(input("Informe o tamanho do metro quadrado a ser pintado:"))
qtd_tinta_mtqd= int((mt_quadrado * cobertura_tinta) + 0.5)
print("1- A quantidade de litros necessária para pintar", mt_quadrado,"m² é: ", qtd_tinta_mtqd,"Litros")

qtd_latas= int((qtd_tinta_mtqd/litro_lata) + 0.5)
print("2- A quantidade de latas de tinta para pintar o m² informado é: ", qtd_latas, "latas de tinta")

valor_total_lata= qtd_latas * preco_lata
print("3- Você precisa comprar", qtd_latas, "latas de tinta e gastará R$", valor_total_lata, "reais")

print("Obrigada por escolher a", loja, "Volte sempre! <3")