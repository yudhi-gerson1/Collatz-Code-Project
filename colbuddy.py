"""
--- Collatz Code v1.2 -> colbuddy.py ---
O que temos nesse arquivo? É onde fica o cérebro do assistente virtual CollatzBuddy, que tem as funções dele.
"""
import funcoes as f, random as r

nome = "CollatzBuddy"

def colbuddy():
	print("--- CollatzBuddy em v1.2 ---")
	print(f"{nome}: Seja muito bem-vindo! Aqui eu posso te ajudar a fazer várias coisas no collatz! Digite 'ajuda' para saber quais dúvidas eu posso responder!")
	while True:
		entrada = input(f"Converse com o {nome}: ").lower().strip()
		if "sair" in entrada or "tchau" in entrada:
			print(f"{nome}: Até mais, pequeno matemático!")
			break
		elif "oi" in entrada:
			print(f"{nome}: Olá! Como posso te ajudar no collatz?")
		elif "collatz" in entrada or "3n+1" in entrada:
			print(f"{nome}: O Collatz (ou o 3n + 1) é uma sequência para os números naturais maiores que 0. Se for impar, multiplique por 3 e adicione 1, Se for par, divida por 2. O final sempre é 4-2-1 nos números testados.")
		elif "soma" in entrada:
			print(f"{nome}: A Soma Acumulativa de Collatz é a soma de todos os passos do número até chegar em 1. Nem sempre o maior passo tem a maior soma acumulativa ")
		elif not entrada:
			print(f"{nome}: Por favor, Digite algo para conversarmos.")
		elif "gêmeos" in entrada or "gemeos" in entrada:
			print(f"{nome}: Os Números Gêmeos de Collatz é o fenômeno matemático onde dois números tem os mesmos passos e a mesma soma acumulativa, mesmo sendo diferentes.")
		elif "média" in entrada or "media" in entrada:
			print(f"{nome}: A Média de Collatz é um termo de Collatz Code que diz a média dos passos de um número dividindo a soma acumulativa pelo número de passos.")
		elif "afiado" in entrada:
			print(f"{nome}: O Número Afiado é quando a soma acumulativa de um número é um quadrado perfeito! Exemplo: o 5 é afiado porque 5+16+8+4+2+1 = 36, e 36 é um número quadrado e a raíz dele é 6!")
		elif "mistério" in entrada or "misterio" in entrada:
			print(f"{nome}: Existem vários mistérios matemáticos que nenhum matemático conseguiu resolver até agora. Um dos exemplos mais fascinantes é o Collatz. Se quiser que eu explique, digite a sua dúvida!")
		elif "ia" in entrada:
			print(f"{nome}: Sim, eu sou uma IA que segue regras que o Yudhi Gerson programou, mas não sou treinada e nem tenho data center, mas tenho apenas um arquivo python para conversar contigo!")
		elif "python" in entrada:
			print(f"{nome}: Ora, ora, se não é a linguagem mais preferida para IAs! O Python é conhecido pela sua simplicidade máxima para projetos complexos!")
		elif "ajuda" in entrada or entrada == "?":
			print("""
			Palavras que entendo e explico na hora:
			- oi, sair, tchau, collatz, 3n+1, soma acumulativa, números gêmeos de collatz, média de collatz, números afiados, mistérios, IAs e Python!
			Isso é o meu vocabulário pythônico! Mantenha a conversa respeitosa, e seguimos em frente!
			""")
		else:
			ofensivas = ["merda", "mrd", "puta", "pqp", "caralho", "crlh", "bosta", "cagar", "buceta", "bct", "pau", "cu ", "porra", "estupro", "matar", "assassinar", "crime", "sexo", "fuder", "foda", "droga", "porno"]
			if any(o in entrada for o in ofensivas):
				print(f"{nome}: Vamos manter a conversa respeitosa e sem xingamentos ou temas pesados. Então, como posso ajudar?")
			else:
				print(f"{nome}: Não consegui identificar qual é a sua dúvida! Verifique a grafia e mande a mensagem!")
				
def choose(x, y):
	investigar = r.randint(x, y)
	print(f"{nome}: Eu escolhi o número {investigar}. Vamos investigá-lo!")
	print("1. COLLATZ")
	f.collatz(investigar)
	print("2. SOMA ACUMULATIVA")
	f.accum(investigar)
	print("3. MÉDIA DE COLLATZ")
	f.mean(investigar)
	print("INVESTIGAÇÃO PRONTA!")
