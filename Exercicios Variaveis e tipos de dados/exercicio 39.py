"""
39 - A importância de R$ 780.000,00 será dividida em três ganhos de um concurso.
Sendo que da quantia total:

a - o primeiro ganhador receberá 46%
b - o segundo ganhador receberá 32%
c - o terceiro ganhador receberá o restante.

Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

premio = float(input("Digite o valor do premio R$: "))

primeiro_ganhador = premio - (premio * 46 / 100)
segundo_ganhador = premio - (premio * 32 / 100)
terceiro_ganhador = premio - (premio * 22 / 100)

print(f"O prêmio de {premio} o primeiro ganhador receberá {primeiro_ganhador}, o segundo {segundo_ganhador} e o terceiro {terceiro_ganhador}.")


"""
Professor como eu faço para formatar, quando for colocar o numero
ele sair desse forma 780.000,00? formatadinho, bonitinho?

nessa parte --> premio = float(input("Digite o valor do premio R$: "))
Porque no output ele sai todo bagunçado, quero dizer ruim para entender.
Olha ai o oputput fica horíivel.
"""
"""
Olá Cristina,

As resoluções dos exercícios 35, 36, 37, 38 e 39 estão de acordo com o enunciado.

Sobre a formatação de moeda da sua dúvida na questão 39, de forma geral fazemos o seguinte:

import locale
 
locate.setlocale(locale.LC_MONETARY, 'pt_BR.UTF8')
valor = 780000
print(locale.currency(valor, grouping=True, symbol=None)

O problema é que você está usando um sistema operacional que não segue as convenções da computação e por isso não é indicado para uso profissional, então
pode ser que não funcione desta forma e então você precisará ver os formatos compatíveis em[1]

[1]https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/a9eac961-e77d-41a6-90a5-ce1a8b0cdb9c

Abraço!
"""
