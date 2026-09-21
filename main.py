print("--- Collatz Code v1.0 ---")
print("( Criado por Yudhi Gerson. Todos os direitos reservados. 100% Humano. )")

def collatz(num):
	print(num)
	passos = 1
	while num > 1:
		if num % 2 == 0:
			num = num // 2
			print(num)
			passos += 1
		else:
			num = (3 * num) + 1
			print(num)
			passos += 1
	return passos
	
def acumular(num):
		acumulado = 0
		acumulado += num
		while num > 1:
			if num % 2 == 0:
				num = num // 2
				acumulado += num
			else:
				num = (3 * num) + 1
				acumulado += num
		return acumulado
while True:
    try:
    	numero = int(input("Digite o número para o collatz: "))
    	total_passos = collatz(numero)
    	print("Número de passos: ", total_passos)
    	cmd = input("Digite um comando (Aperte Enter para continuar, [ajuda] para comandos): ").lower()
    	if cmd == "[sair]":
    		print("Até mais, pequeno matemático!")
    		break
    	elif cmd == "":
    		continue
    	elif cmd == "[ajuda]":
    		print("""
    		[sair]: Sair do projeto
    		[ajuda]: Dizer os comandos
    		[acumulo]: Dizer o total dos números da Sequência de Collatz (inserir o número)
    		Enter: Continuar
    		Dica: Se não quiser esperar, digite números rápidos como 1 ou 0
    		""")
    	elif cmd == "[acumulo]":
    		numeroParaAcumulo = int(input("Digite um númeto para acumular todos da Sequência de Collatz dele: "))
    		acumulo = acumular(numeroParaAcumulo)
    		print("Resultado do Acúmulo: ", acumulo)
    except ValueError:
        print("Não é um número inteiro!")
