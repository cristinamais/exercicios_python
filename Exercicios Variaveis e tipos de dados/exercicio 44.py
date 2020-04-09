"""
44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja
alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá
subir para atingir o seu objetivo.
"""

altura_degrau = int(input("Quantos degraus você já subiu? "))
altura_objetivo =  int(input("Quantos degraus você quer subir? "))

objetivo = altura_objetivo - altura_degrau

print(f"Você já subiu {altura_degrau} degrau(s), falatam {objetivo}, para você alcançar o seu objetivo.")
