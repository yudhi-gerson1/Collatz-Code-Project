
"""
--- Collatz Code v1.2 -> Correções e Adições ---
1. CORREÇÕES:
- Agora, os comandos de Collatz Code foram substituídos pelas suas versões inglesas abreviadas.
[collatz] permanece com a mesma síntaxe
[sair] -> [exit]
[acumulo] -> [accum]
[colbuddy] permanece igual
[escolher] -> [choose]
[separador] -> [sep]
[comparar] -> [comp]
[passos] -> [steps]
[numerar] -> [num]
[ajuda] -> [help] ou [?] para testes rápidos
- Agora, se o usuário não digitar nada, o programa apenas dá um aviso, sem tratar isso como um erro.
2. ADIÇÕES:
Diga olá aos argumentos: Ao invés de digitar o comando e digitar o input dos números, você pode fazer diretamente no input do cmd. Cada argumento é separado por espaço. Exemplo de Síntaxe:
[comparar 5 6].
O comando que não tiver argumento é chamado de Comandos Vazios. Veja:
[help], [?], [exit] e [colbuddy] -> Comandos vazios
[collatz], [accum], [steps], [num] -> apenas 1 argumento
[comp], [sep], [choose] -> 2 argumentos
Existem também os comandos irregulares, onde o tipo de valor dos parâmetros não são iguais. Um exemplo disso é o [sep], que segue obrigatoriamente essa Síntaxe:
[sep int str]
int - Para o collatz
str - O separador
- Novos arquivos: parser.py, parser_metodos.py e funcao_metodos
parser.py: Esse é o novo arquivo de Collatz Code v1.2. Ele serve como um arquivo intermediário que analisa a Síntaxe dos comando e pelos tratamentos de erros. Se tudo der certo, chama a funcoes.py para receber os dados.
pars_metodos.py: Faz a mesma coisa que o parser.py, só que com suporte a métodos nativos de Collatz Code. Ela é responsável por verificar se o método é compatível, e fazer o parser deles.
func_metodos.py: É um arquivo que é uma divisão de funcoes.py, que é responsável pelos comandos com métodos. É reponsável por fazer as funções comandos seguirem a regra que os metodos adicionaram.
- Novo tratamento de erros
Ao invés daquele tratamento fixo de "ERRO: Mensagem de Erro", agora, cada erro tem o seu próprio nome. Temos o SyntaxError, CollatzError, ArgumentError, CommandError, TypeError e MethodError.
- Novos Comandos:
1. [comp3 x y z]: Compara três números pela soma acumulativa e o número de dados e entrega o número vencedor.
2. Método .breakAt(n): Para a Contagem de Collatz se chegar até o n. Disponível para [collatz], [accum], [steps] e [num], exemplo de uso:
[collatz 3].breakAt(5)
3. Método .step(n): Checa o enésimo passo de collatz do número, disponível para [collatz] e [num].
[collatz 27].step(100)
4. Comentários: Agora chegou os comentários! Serve para quando quiser copiar e colar o output, explicar personalizadamente o que fez nos testes. Ex:
[c "Eu estou num comentário?"]
5. [mean n]: Calcula a media aproximada dos passos de um número, ex:
[mean 5]
5
16
8
4
2
1
5 + 16 + 8 + 4 + 2 + 1 = 36
36 / 6 passos = 6
- A Divisão de v1.2:
v1.2.0 - Focado em trazer os novos comandos, mudar para o inglês e os no os tratamentos de erros
v1.2.1 - Comandos como [methodMode], [comp3] e os novos arquivos de métodos. É a parte difícil da v1.2 de CollatzCode.
- Então, foram isso as adições, até mais! 
100% Humano e sem IA no código. Yudhi Gerson.
"""
import parser as p
print("""   O     O
   |     |
[''''''''''']
|  [''''''  |  
|  |        | 
|  |        | 
|  [......  |
[...........]""")
print("--- Collatz Code v1.2.0 (NOVO) ---")
print("( Criado por Yudhi Gerson, sem IA e 100% humano. )")

while True:
	cmd = input("Digite um comando (Ou [?] para os comandos disponíveis): ").strip()
	
	if cmd.startswith("[") and cmd.endswith("]"):
		cmd = cmd.removesuffix("]").removeprefix("[").strip()
		if cmd.startswith("collatz "):
			p.analisar_collatz(cmd)
		elif cmd.startswith("accum "):
			p.analisar_accum(cmd)
		elif cmd.startswith("sep "):
			p.analisar_sep(cmd)
		elif cmd.startswith("comp "):
			p.analisar_comp(cmd)
		elif cmd.startswith("steps "):
			p.analisar_steps(cmd)
		elif cmd.startswith("num "):
			p.analisar_num(cmd)
		elif cmd.startswith("colbuddy"):
			p.analisar_colbuddy(cmd)
		elif cmd.startswith("choose "):
			p.analisar_choose(cmd)
		elif cmd.startswith("help"):
			p.analisar_help(cmd)
		elif cmd.startswith("?"):
			p.analisar_quesmark(cmd)
		elif cmd.startswith("c "):
			p.analisar_c(cmd)
		elif cmd.startswith("mean "):
			p.analisar_mean(cmd)
		elif cmd.startswith("exit"):
			if p.analisar_exit(cmd):
				break
		elif cmd.startswith("[") or cmd.endswith("]"):
			print("SyntaxError: Não pode ter colcletes repetidos no comando!")
		else:
			print("CommandError: Comando inexistente ou indisponível: ", "[", cmd, "]")
	elif cmd == "":
		print("Alert: Por favor, Digite um comando ou digite [ajuda] ou [?] para comandos.")
	else:
		print("SyntaxError: Um comando tem que começar com [ e termirar com ].")
