"""
--- Collatz Code v1.1 -> funcoes.py ---
- O que temos nesse arquivo?
Nesse arquivo mora o céreio do Collatz Vode, que permite que o computador faça quando ver algum comando
"""
def collatz(num):
	# O próprio número é contado como um passo também
	print(num)
	passos = 1
	while num > 1:
		if num % 2 == 0:
			num //= 2
			print(num)
			passos += 1
		else:
			num = (num * 3) + 1
			print(num)
			passos += 1
	print("Quantidade de passos: ", passos)
	
def acumular(num):
	soma = 0
	soma += num
	while num > 1:
		if num % 2 == 0:
			num //= 2
			soma += num
		else:
			num = (num * 3) + 1
			soma += num
	print("Soma Acumulativa de Collatz: ", soma)
	
def separar(s, n):
	print(n, end=s)
	passos = 1
	while n > 1:
		if n % 2 == 0:
			n //= 2
			print(n, end=s)
			passos += 1
		else:
			n = (n * 3) + 1
			print(n, end=s)
			passos += 1
	print("Quantidade de passos: ", passos)
	
def comparar(num1, num2):
	print("1. Número de passos")
	num1_orig = num1
	num2_orig = num2
	num1_acum = num1
	num2_acum = num2
	passos1 = 1
	passos2 = 1
	ponto1 = 0
	ponto2 = 0
	while num1 > 1:
		if num1 % 2 == 0:
			num1 //= 2
			passos1 += 1
		else:
			num1 = (num1 * 3) + 1
			passos1 += 1
	while num2 > 1:
		if num2 % 2 == 0:
			num2 //= 2
			passos2 += 1
		else:
			num2 = (num2 * 3) + 1
			passos2 += 1
	print("Resultado: ")
	print(f"Quantidade de passos do {num1_orig}: {passos1}")
	print(f"Quantidade de passos de {num2_orig}: {passos2}")
	if passos1 > passos2:
		print(f"O número {num1_orig} ganhou!")
		ponto1 += 1
	elif passos1 == passos2:
		print("Empate técnico...")
	else:
		print(f"O número {num2_orig} ganhou!")
		ponto2 += 1
	print("2. Soma Acumulativa")
	soma1 = 0
	soma1 += num1_acum
	while num1_acum > 1:
		if num1_acum % 2 == 0:
			num1_acum //= 2
			soma1 += num1_acum
		else:
			num1_acum = (num1_acum * 3) + 1
			soma1 += num1_acum
	soma2 = 0
	soma2 += num2_acum
	while num2_acum > 1:
		if num2_acum % 2 == 0:
			num2_acum //= 2
			soma2 += num2_acum
		else:
			num2_acum = (num2_acum * 3) + 1
			soma2 += num2_acum
	print("Resultado: ")
	print(f"Soma Acumulativa de {num1_orig}: {soma1}")
	print(f"Soma Acumulativa de {num2_orig}: {soma2}")
	if soma1 > soma2:
		print(f"O número {num1_orig} ganhou!")
		ponto1 += 1
	elif soma1 == soma2:
		print("Empate técnico...")
	else:
		print(f"O número {num2_orig} ganhou!")
		ponto2 += 1
	print("Resultado final: ")
	print(f"Pontos de {num1_orig}: {ponto1}")
	print(f"Pontos de {num2_orig}: {ponto2}")
	if ponto1 > ponto2:
		print(f"O NÚMERO {num1_orig} GANHOU!")
	elif ponto1 == ponto2 and num1_orig == num2_orig:
		print("ERRO: Você inseriu números iguais! Desconfio...")
	elif ponto1 == ponto2 and num1_orig != num2_orig:
		print("É um empate técnico! Os dois números são Gêmeos de Collatz!")
	else:
		print(f"O NÚMERO {num2_orig} GANHOU!")
		
def passos(num):
	passos = 1
	while num > 1:
		if num % 2 == 0:
			num //= 2
			passos += 1
		else:
			num = (num * 3) + 1
			passos += 1	
	print("Quantidade de passos: ", passos)
	
def numerar(num):
	# O próprio número é contado como um passo também
	passos = 1
	print(f"{passos}. {num}")
	while num > 1:
		if num % 2 == 0:
			num //= 2
			passos += 1
			print(f"{passos}. {num}")
		else:
			num = (num * 3) + 1
			passos += 1
			print(f"{passos}. {num}")
	print("Quantidade de passos: ", passos)
