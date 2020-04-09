"""
Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C
int numero = 42

Exemplo em Java:
int numero = 42;
"""

numero = 42 # Exemplo de variável global
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

nao_existo = 'oi'
print(nao_existo)

numero = 42
# novo = 0

if numero > 10:
    novo = numero + 10 # A variável 'novo' está declarada localmente
# dentro do bloco if. Portanto é local.
    print(novo)
    
print(novo)
