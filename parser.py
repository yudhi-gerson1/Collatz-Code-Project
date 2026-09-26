"""
--- Collatz Code v1.2 -> parser.py (novo) ---
O que temos nesse Arquivo? Esse arquivo tem a validação de síntaxe de comandos de Collatz Code. Se tudo der certo, ele entrega os dados para o Collatz.
"""
import funcoes as f
import colbuddy as cb

def analisar_collatz(cmd):
	try:
		cmd = cmd.replace("collatz ", "").split()
		if len(cmd) != 1:
			print("ArgumentError: O comando [collatz] houve mais/menos argumentos que o esperado. (necessário 1 argumento)")
		else:
			num = int(cmd[0])
			if num < 1:
				print("CollatzError: O comando [collatz] espera números maiores que 0.")
			else:
				f.collatz(num)
	except ValueError:
		print("TypeError: O collatz apenas aceita números inteiros maiores que 0.")
		
def analisar_exit(cmd):
	cmd = cmd.replace("exit", "").strip().split()
	if len(cmd) > 0:
		print("ArgumentError: O comando [exit] não tem argumentos, é um comando vazio!")
		return False
	else:
		print("Até mais, pequeno matemático!")
		return True
		
def analisar_accum(cmd):
	try:
		cmd = cmd.replace("accum ", "").split()
		if len(cmd) != 1:
			print("ArgumentError: O comando [accum] houve mais/menos argumentos que o esperado. (necessário 1 argumento)")
		else:
			num = int(cmd[0])
			if num < 1:
				print("CollatzError: O comando [accum] espera números maiores que 0.")
			else:
				f.accum(num)
	except ValueError:
		print("TypeError: O collatz apenas aceita números inteiros maiores que 0.")
		
def analisar_sep(cmd):
	try:
		cmd = cmd.replace("sep ", "").split()
		if len(cmd) != 2:
			print("ArgumentError: O comando [sep] houve mais/menos argumentos que o esperado. (necessário 2 argumentos)")
		else:
			num = int(cmd[0])
			text = cmd[1]
			if text.startswith('"') or text.endswith('"'):
				text = text.removesuffix('"').removeprefix('"')
				if num < 0:
					print("CollatzError: O comando [sep] espera números maiores que 0 no argumento [0].")
				else:
					f.sep(num, text)
			else:
				print("SyntaxError: O texto em argumento [1] tem que estar entre aspas duplas.")
	except ValueError:
		print("TypeError: O argumento [0] não parece ser um número.")
		
def analisar_comp(cmd):
	try:
		cmd = cmd.replace("comp ", "").split()
		if len(cmd) != 2:
			print("ArgumentError: O comando [comp] houve mais/menos argumentos que o esperado. (necessário 2 argumentos)")
		else:
			num1 = int(cmd[0])
			num2 = int(cmd[1])
			if num1 < 1 or num2 < 1:
				print("CollatzError: O comando [comp] espera números maiores que 0 em ambos os argumentos.")
			else:
				f.comp(num1, num2)
	except ValueError:
		print("TypeError: Um dos argumentos em [comp] não parece ser um número.")
		
def analisar_steps(cmd):
	try:
		cmd = cmd.replace("steps ", "").split()
		if len(cmd) != 1:
			print("ArgumentError: O comando [steps] houve mais/menos argumentos que o esperado. (necessário 1 argumento)")
		else:
			num = int(cmd[0])
			if num < 1:
				print("CollatzError: O comando [steps] espera números maiores que 0.")
			else:
				f.steps(num)
	except ValueError:
		print("TypeError: O collatz apenas aceita números inteiros maiores que 0.")
		
def analisar_num(cmd):
	try:
		cmd = cmd.replace("num ", "").split()
		if len(cmd) != 1:
			print("ArgumentError: O comando [num] houve mais/menos argumentos que o esperado. (necessário 1 argumento)")
		else:
			num = int(cmd[0])
			if num < 1:
				print("CollatzError: O comando [num] espera números maiores que 0.")
			else:
				f.num(num)
	except ValueError:
		print("TypeError: O collatz apenas aceita números inteiros maiores que 0.")

def analisar_colbuddy(cmd):
	cmd = cmd.replace("colbuddy", "").strip().split()
	if len(cmd) > 0:
		print("ArgumentError: O comando [colbuddy] não tem argumentos, é um comando vazio!")
	else:
		cb.colbuddy()
		
def analisar_choose(cmd):
	try:
		cmd = cmd.replace("choose ", "").split()
		if len(cmd) != 2:
			print("ArgumentError: O comando [choose] houve mais/menos argumentos que o esperado. (necessário 2 argumentos)")
		else:
			num1 = int(cmd[0])
			num2 = int(cmd[1])
			if num1 < 1 or num2 < 1:
				print("CollatzError: O comando [comp] espera números maiores que 0 em ambos os argumentos.")
			elif num2 <= num1:
				print("ChooseError: Não foi possível escolher um número válido (argumento [0] tem que ser menor que argumento [1])")
			else:
				cb.choose(num1, num2)
	except ValueError:
		print("TypeError: Um dos argumentos em [comp] não parece ser um número.")

def analisar_help(cmd):
	cmd = cmd.replace("help", "").strip().split()
	if len(cmd) > 0:
		print("ArgumentError: O comando [help] não tem argumentos, é um comando vazio!")
	else:
		f.help()
		
def analisar_quesmark(cmd):
	cmd = cmd.replace("?", "").strip().split()
	if len(cmd) > 0:
		print("ArgumentError: O comando [?] não tem argumentos, é um comando vazio!")
	else:
		f.help()
		
def analisar_c(cmd):
	cmd = cmd.replace("c ", "").replace(" ", "")
	if cmd.startswith('"') and cmd.endswith('"'):
		print("Success: Comentário reconhecido sem erros.")
	else:
		if cmd.startswith('"'):
			cmd = cmd.removeprefix('"')
			if '"' not in cmd:
				print("SyntaxError: As aspas duplas não foram fechadas corretamente")
			else:
				cmd = cmd.split()
				if len(cmd) != 1:
					print("ArgumentError: O comando [c] houve mais/menos argumentos que o esperado. (necessário 1 argumento)")
				else:
					print("SyntaxError: Não pode ter caracteres extras além do ] após as aspas duplas.")
		else:
			print("SyntaxError: O texto do comentário tem que começar com uma aspa dupla.")
			
def analisar_mean(cmd):
	try:
		cmd = cmd.replace("mean ", "").split()
		if len(cmd) != 1:
			print("ArgumentError: O comando [mean] houve mais/menos argumentos que o esperado. (necessário 1 argumento)")
		else:
			num = int(cmd[0])
			if num < 1:
				print("CollatzError: O comando [mean] espera números maiores que 0.")
			else:
				f.mean(num)
	except ValueError:
		print("TypeError: O collatz apenas aceita números inteiros maiores que 0.")
