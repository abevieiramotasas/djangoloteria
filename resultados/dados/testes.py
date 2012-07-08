import re

dot = re.compile(r'.')
if dot.match('a'):
	print(" . matches a")
if dot.match('ab'):
	print(" . matches ab")

only_dot = re.compile(r'^.$')
if only_dot.match('a'):
	print(" ^.$ matches a")
if not only_dot.match('ab'):
	print(" ^.$ doesnt matches ab")

# adicionando ? apos algum dos caracteres +, *, ? indica que o match deve ser realizado na menor substring
# ex: <.*> para a string <h1>oi</h1> ira capturar toda a string
# ex: <.*?> para a string <h1>oi</h1> ira capturar <h1> e </h1>

# quantificadores
# {n} exato
# {m,n} entre inclusive m e n, {,n} no maximo n, {m,} no minimo m
# {...}? realiza o menor numero de matches possiveis
# exemplo: a{3,5} captura em aaaa toda a string
# ja a{3,5}? captura apenas o substring aaa

# [] utilizado para informar conjunto de caracteres
# intervalo de caracteres sao informados com [ini-fim]
# ex: [0-9]
# [^a] indica que deve ser aceito qualquer caractere a menos de a

# | indica OU para regex
# A|B aceita uma string que seja aceita ou por A ou por B

# (regex) aceita uma string aceita por regex e a inclui em um grupo
# permitindo que a string seja recuperada apos o match
# (?<name>regex) informa um name(deve ser unico na regex toda) de forma que
# o valor que for capturado pode ser acessado por (?P=name)
# (?=regex) se aceita a string, nao captura
# ex: Isaac (?=Asimov) vai aceitar Isaac apenas se for seguido de Asimov
# (?!regex) eh a versao negativa de (?=regex)
# (?<=regex1)regex2 aceita a string que contenha substring aceita por regex1 e antecedida por string aceita por regex2, nao capturando esta
# (?<!regex1)regex2 eh a versao negativa do anterior

# \number aceita a string que foi aceita no grupo na posicao number, em ordem comecando em 1 da esquerda pra direita na regex

