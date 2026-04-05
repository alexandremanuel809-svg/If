nome = input("Digite seu nome: ")
print(f"Como estás {nome}")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

Resultado = n1 + n2
print(f"O resultado é: {Resultado}")

if Resultado % 2 == 0:
    print("O número é par")
else:
    print("O número é impar")