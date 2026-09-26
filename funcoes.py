"""
--- Collatz Code v1.2 -> funcoes.py ---
O que temos nesse Arquivo? Aqui tem as principais funções de comandos que serão chamados após o parser.py validar a síntaxe.
Os passos de collatz começam em 1 nesse código, pois conta o próprio número como passo.
"""
# 1. Funções de retorno
def return_steps(num):
	print(num, end=", ")
	passos = 1
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		passos += 1
		print(num, end=", ")
	print("Quantidade de passos: ", passos)
	return passos

def return_accum(num):
	acumulo = num
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		acumulo += num
	print("Soma Acumulativa de Collatz: ", acumulo)
	return acumulo
	
def silent_steps(num):
	passos = 1
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		passos += 1
	return passos

def silent_accum(num):
	acumulo = num
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		acumulo += num
	return acumulo
		
# 2. Funções que não retornam
def collatz(num):
	print(num)
	passos = 1
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		passos += 1
		print(num)
	print("Quantidade de passos: ", passos)
	
def accum(num):
	acumulo = num
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		acumulo += num
	print("Soma Acumulativa de Collatz: ", acumulo)
	
def sep(num, text):
	text = " " + text + " "
	print(num, end=text)
	passos = 1
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		passos += 1
		print(num, end=text)
	print("Quantidade de passos: ", passos)
	
def comp(num1, num2):
	if num1 == num2:
		print("ComparationError: Os números não podem ser os mesmos!")		
	else:	
		ponto1 = 0
		ponto2 = 0
		print("1. PASSOS")
		passo1 = return_steps(num1)
		passo2 = return_steps(num2)
		if passo1 > passo2:
			print(f"O NÚMERO {num1} GANHOU!")
			ponto1 += 1
		elif passo2 > passo1:
			print(f"O NÚMERO {num2} GANHOU!")
			ponto2 += 1
		else:
			print(f"Empate... vamos ver a outra!")
		print("2. SOMA ACUMULATIVA")
		accum1 = return_accum(num1)
		accum2 = return_accum(num2)
		if accum1 > accum2:
			print(f"O NÚMERO {num1} GANHOU!")
			ponto1 += 1
		elif accum2 > accum1:
			print(f"O NÚMERO {num2} GANHOU!")
			ponto2 += 1
		else:
			print(f"Empate... Vamos ver os pontos!")
		print("3. RESULTADO FINAL")
		print(f"Pontos do número {num1}: {ponto1}")
		print(f"Pontos do número {num2}: {ponto2}")
		if ponto1 > ponto2:
			print(f"O NÚMERO {num1} GANHOU ESTA RODADA!")
		elif ponto2 > ponto1:
			print(f"O NÚMERO {num2} GANHOU ESTA RODADA!")
		else:
			print("Empate nessa rodada! Eles são GÊMEOS DE COLLATZ!")

def steps(num):
	passos = 1
	while num > 1:
		if num % 2 != 0:
			num = (3 * num) + 1
		else:
			num //= 2
		passos += 1
	print("Quantidade de passos: ", passos) 
	
def num(n):
	passos = 1
	print(f"{passos}. {n}")
	while n > 1:
		if n % 2 != 0:
			n = (3 * n) + 1
		else:
			n //= 2
		passos += 1
		print(f"{passos}. {n}")
	print("Quantidade de passos: ", passos)
	
def mean(num):
	accum = silent_accum(num)
	steps = silent_steps(num)
	mean = accum / steps
	print(f"Média de Collatz: {mean}")
	
def help():
	print("""
			COMANDOS DISPONÍVEIS da v1.2:
			[collatz n] - Calcula a sequência de Collatz de n até chegar no número 1.
			[accum n] - Calcula a soma acumulativa, ou seja, soma todos os números da sequência do n e mostra o resultado.
			[exit] - Sai do programa.
			[colbuddy] - Abre o chat do assistente CollatzBuddy
			[choose x y] - O CollatzBuddy escolhe um número entre x e y e o investiga pelo passos e soma acumulativa.
			[sep n "text"] - Calcula a sequência de Collatz de n, só que adiciona o texto entre os números.
			[comp x y] - Compara os números pelo maior número de passos e a maior soma acumulativa.
			[steps n] - Calcula apenas os passos de Collatz de n
			[num n] - Calcula a sequência de Collatz de n, só que tem o número da posição dos passos
			[help] ou [?] - Mostra todos os comandos disponíveis e suas regras
			[c "Comentário"] - É um comentário, ou seja, serve para guiar outros desenvolvedores e o parser ignora.
			[mean n] - Calcula a média de collatz de n, ou seja, divide a soma acumulativa pelos passos de n.
	""")
