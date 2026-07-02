"""


"""

print("\nmodulo04 - Estruturas de dados - Dicionários \n")
print("-" * 40)

# 1. DICIONÁRIO (Coleção de itens em pares de chave-valor)
cardapio_da_semana = {
    "segunda-feira": "Arroz com feijão",
    "terça-feira": "Panquecas",
    "quarta-feira": "Feijoada",
    "quinta-feira": "Sopa de legumes",
    "sexta-feira": "Peixe grelhado",
    "sábado": "Pizza",
    "domingo": "Macarrão",
}

cardapio_da_semana["quarta-feira"] = "Feijoada Especial com Couve"

print("Bem-vindo ao programa de verificação de cardápio! \n")


dia_escolhido = input("Digite um dia da semana para saber o menu: ").lower().strip()


if dia_escolhido in cardapio_da_semana:
    comida = cardapio_da_semana[dia_escolhido]
    print(f"No {dia_escolhido}, o prato do dia é: {comida}!")

    
else:
    print(
        f'Desculpe, "{dia_escolhido}" não é um dia válido no nosso cardápio. Tente usar o hífen (ex: segunda-feira).'
   "break" )

    