"""
--- Collatz Code v1.1 -> colbuddy.py ---
- O que temos nesse arquivo?
É onde fica a mente por trás do assistente virtual CollatzBuddy, sua IA para investigações de collatz
"""
import random, funcoes

nome = "CollatzBuddy"

def conversar():
	print("--- CollatzBuddy Init ---")
	print(f"{nome}: Seja muito bem-vindo! Aqui eu posso te ajudar a fazer várias coisas no collatz!")
	while True:
		entrada = input(f"Converse com o {nome}: ").lower().strip()
		if "sair" in entrada or "tchau" in entrada:
			print(f"{nome}: Até mais, pequeno matemático!")
			break
		elif "oi" in entrada:
			print(f"{nome}: Olá! Como posso te ajudar no collatz")
		elif "collatz" in entrada or "3n+1" in entrada:
			print(f"{nome}: O Collatz (ou o 3n + 1) é uma sequência para os números naturais maiores que 0. Se for impar, multiplique por 3 e adicione 1, Se for par, divida por 2. O final sempre é 4-2-1 nos números testados.")
		elif "soma" in entrada:
			print(f"{nome}: A Soma Acumulativa de Collatz é a soma de todos os passos do número até chegar em 1. Nem sempre o maior passo tem a maior soma acumulativa ")
		elif " " in entrada:
			print(f"{nome}: Por favor, Digite algo para conversarmos.")
		elif "gêmeos" in entrada:
			print(f"{nome}: Os números gêmeos de collatz é o fenômeno matemático onde dois números tem os mesmos passos e a mesma soma acumulativa, mesmo sendo diferentes. Exemplo: 3 e 20")
		else:
			print(f"{nome}: Eu não entendi o que você disse, pode ser essas 3 coisas")
			print("1. Você digitou errado: Confira se está gramaticalmente correta antes de enviar.")
			print("2. Fora do assunto: Sempre diga coisas que tenha a ver com o Collatz Code! Eu NÃO dou receitas ou NÃO sei qual foi a data da independência do Brasil, mas eu sei o que é collatz ou números gêmeos de collatz.")
			print("3. Aleatoriedade: Eu não sei o que é rgyvdhd6hdyg, cara.")
			
def escolher(n1, n2):
	num = random.randint(n1, n2)
	print(f"{nome}: Escolhi o número {num}")
	funcoes.collatz(num)
	funcoes.acumular(num)
