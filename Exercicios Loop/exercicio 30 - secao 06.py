"""
30 - Faça programas para calcular as seguintes sequencias:
1 + 2 + 3 + 4 + 5 +... + n
1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
1 + 3 + 5 + 7 + ... + (2n - 1)
"""
n = 0
soma = 0
soma1 = 0
soma2 = 0

n = int(input('Digite um número: '))
for i in range(1, n + 1):
    soma += i
    soma1 = ((n * (n - 1) // 2) * (2 * n - 1) // 3)
    soma2 = ((n * (n + 1) // 2) * (2 * n + 1) // 3)

print(f'A sequancia (1 + 2 + 3 + 4 + 5 +... + n) do número {n} é {soma}')
print(f'A sequancia (1 - 2 + 3 - 4 + 5 + ... + (2n - 1)) do número {n} é {soma1}')
print(f'A sequancia (1 + 3 + 5 + 7 + ... + (2n - 1)) do número {n} é {soma2}')
