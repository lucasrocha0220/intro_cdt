"""
"""

print("\nmodulo04 - Estruturas de dados - Listas \n")
print("🍒" * 40)
print("Bem-vindo ao sistema de Lista de Frutas Favoritas \n")
print("🍒" * 40)

# 1. LISTA (Coleção ordenada e mutável)
frutas_favoritas = [
    "banana",
    "morango",
    "abacaxi",
    "maça",
    "abacate",
    "uva",
    "mango",
    "kiwi",
    "pessego",
    "cereja",
    "pitaya",
]


fruta_escolhida = input("Digite o nome da fruta que deseja colocar: ").lower().strip()


if fruta_escolhida in frutas_favoritas:
    # Se a fruta JÁ ESTIVER na lista, executa este bloco
    print(f'\nAviso: A fruta "{fruta_escolhida}" já está na sua lista de favoritas!')
else:
    
    frutas_favoritas.append(fruta_escolhida)
    print(f'\nFruta "{fruta_escolhida}" adicionada com sucesso!')


print(f"A lista atualizada de frutas favoritas é: {frutas_favoritas}")