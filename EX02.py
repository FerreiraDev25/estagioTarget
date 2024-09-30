a = 0
b = 1
pertence = False
num = int(input("Digite um número: "))

while a <= num:
    if a == num:
        pertence = True
        break
    a, b = b, a + b
if pertence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")