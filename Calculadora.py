print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Insira uma opção: "))
n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

match op:
    case 1:
        Resultado = n1 + n2
        print(f"O resultado é: {Resultado}")

    case 2:
        Resultado = n1 - n2
        print(f"O resultado é: {Resultado}")

    case 3:
        Resultado = n1 * n2
        print(f"O resultado é: {Resultado}") 

    case 4:
        Resultado = n1 / n2
        print(f"O resultado é: {Resultado}")        