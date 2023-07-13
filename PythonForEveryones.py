# Página 24 - P1.1 Write a program that prints a greeting
# of your choice, perhaps in a language other than English.
print("**************** Exercício 1 ****************")
mensagem = "Seja bem vindo!"
print(mensagem)

# Página 24 - P1.2 Write a program that prints the sum of 
# the first ten positive integers, 1 + 2 + … + 10.
print("**************** Exercício 2 ****************")
soma = 0
for i in range(11):
    soma = i + soma
print("A soma dos nº de 1 a 10 são: ", soma)

# Página 24 - P1.3 Write a program that prints the product
# of the first ten positive integers, 1 × 2 × … ×
print("**************** Exercício 3 ****************")
produto = 1
for i in range(1,10,1):
    produto = i * produto
print("A multiplicação dos nº de 1 a 10 são: ", produto)

# Página 24 - P1.4 Write a program that prints the balance of 
# an account after # the first, second, and third year. The 
# account has an initial balance of $1,000 and earns 5 percent
# interest per year.
print("**************** Exercício 4 ****************")
saldo_inicial = 1000
saldo_01 = saldo_inicial * 1.05
saldo_02 = saldo_01 * 1.05
saldo_03 = saldo_02 * 1.05
print("Saldo inicial: ", saldo_inicial)
print("Saldo primeiro ano: ", saldo_01)
print("Saldo segundo ano: ", saldo_02)
print("Saldo terceiro ano: ", saldo_03)

# Write a program that displays your name inside a box on the 
# screen, like this: Manoel Do your best to approximate lines 
# with characters such as | - +.
# I used this ascii caracteres for the best presentation:
# 124 | 196 ─ 191 ┐ 192 └ 217 ┘ 218 ┌
print("**************** Exercício 5 ****************")
print("┌────────┐")
print("| Manoel |")
print("└────────┘")

# 6 Write a program that prints your name in large letters
print("**************** Exercício 6 ****************")

print("*       * * * * * * *       * * * * * * * * * * * *         ")
print("* *   * * *       * * *     * *       * *         *         ")
print("*   *   * * * * * * *   *   * *       * * * *     *         ")
print("*       * *       * *     * * *       * *         *         ")
print("*       * *       * *       * * * * * * * * * * * * * * * * ")

# 7 Write a program that prints a face similar to the following:
print("**************** Exercício 7 ****************")
print("!!!!!!!")
print("+'''''+")
print("([o o])")
print("|  ^  |")
print("| '-' |")
print("+-----+")




