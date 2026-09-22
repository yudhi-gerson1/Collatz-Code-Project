"""
( Criado por desenvolvedor indie Yudhi Gerson. 100% Humano. )
--- Collatz Code v1.1: Correções e adições ---
1. Correções
- Separado arquivos de Collatz Code
main.py: O arquivo principal
funcoes.py: O arquivo das funções do Collatz
colbuddy: funções do assistente CollatzBuddy
- Agora, o cmd que vem primeiro, não a função collatz
- Melhorado a experiência do usuário. Agora, para ter o Collatz, basta digitar [collatz]
2. Adições
CollatzBuddy: Seu assistente virtual para investigar, analisar e reagir a sequências de Collatz. Digite [colbuddy] para conversar diretamente com ele. Digite [escolher] para o CollatzBuddy escolher um número entre o primeiro número e o segundo número para investigar os passos, a sequência, a reação e a soma acumulativa.
[separador]: Ao digitar esse comando, vai ter um input pedindo para personalizar o separador. Exemplo: 5, 16, 8, 4, 2, 1.
Comparação: Agora é possivel comparar dois números (pela soma acumulativa e passos). basta digitar [comparar] (ou [comparar3] para três números).
[passos]: Apenas diz os passos de Collatz dos números, contando silenciosamente
[numerar]: Diz a posição dos passos junto com o número no collatz, assim:
1. 5
2. 16
3. 8
4. 4
5. 2
6. 1
Então, foi isso, aproveite o código!
"""
import funcoes as f
import colbuddy as cb

print("--- Collatz Code v1.1 (Novo) ---")
print("( Criado por Yudhi Gerson. Todos os direitos reservados. 100% Humano. )")

while True:
    cmd = input("Digite um comando (Aperte Enter para continuar, [ajuda] para comandos): ").lower().strip()
    
    if cmd == "[sair]":
        print("Até mais, pequeno matemático!")
        break
    elif cmd == "[collatz]":
        try:	
        	entradaCollatz = int(input("Digite um número para entrada: "))
        	if entradaCollatz <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		f.collatz(entradaCollatz)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
    elif cmd == "[ajuda]":
        print("""
        --- Comandos de Collatz Code v1.1 ---
        [collatz]: Executa a sequência padrão de Collatz
        [sair]: Sair do projeto
        [ajuda]: Dizer os comandos
        [acumulo]: Dizer o total dos números da Sequência de Collatz (inserir o número)
        [colbuddy]: Conversar com o CollatzBuddy, o seu assistente
        [escolher]: Digitar 2 números e analisar um número entre eles no Collatz
        [separador]: Modifica o separador temporariamente
        Enter: Continuar
        [comparar]: Compara dois números pela soma acumulativa e passos no Collatz
        [comparar3]: Compara três números pela soma acumulativa e passos no Collatz (Obs: foi adiado para a versão 1.2)
        [passos]: Foca exclusivamente nos passos
        [numerar]: Enumera os passos do Collatz
        """)
    elif cmd == "[acumulo]":
        try:	
        	entradaAcumulo= int(input("Digite um número para acumulo: "))
        	if entradaAcumulo <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		f.acumular(entradaAcumulo)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
    elif cmd == "[colbuddy]":
        cb.conversar()
        pass
    elif cmd == "[escolher]":
        try:
        	n1_esc = int(input("Digite o número 1: "))
        	n2_esc = int(input("Digite o número 2: "))
        	if n1_esc <= 0 or n2_esc <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		cb.escolher(n1_esc, n2_esc)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
        pass
    elif cmd == "[separador]":
        separador = input("Digite o Separador: ")
        try:	
        	entradaSeparar = int(input("Digite um número para separar no Collatz: "))
        	if entradaSeparar <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		f.separar(separador, entradaSeparar)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
    elif cmd == "[comparar]":
        try:
        	n1 = int(input("Digite o número 1: "))
        	n2 = int(input("Digite o número 2: "))
        	if n1 <= 0 or n2 <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		f.comparar(n1, n2)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
    elif cmd == "[comparar3]":
        print("ERRO: O Comando foi adiado para v1.2. Digite [ajuda] para outros comandos.")
    elif cmd == "[passos]":
        try:	
        	entradaPassos = int(input("Digite um número para contar os passos: "))
        	if entradaPassos <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		f.passos(entradaPassos)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
    elif cmd == "[numerar]":
        try:	
        	entradaNumerar = int(input("Digite um número para numerar os passos: "))
        	if entradaNumerar <= 0:
        		print("ERRO: O collatz apenas é para números naturais")
        	else:
        		f.numerar(entradaNumerar)
        except ValueError:
        	print("ERRO: Você inseriu um texto ou um decimal. O collatz só aceita naturais na matemática.")
    else:
        print("ERRO: Comando não reconhecido. Digite [ajuda] para comandos disponíveis.")
