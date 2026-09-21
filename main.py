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

print("--- Collatz Code v1.1 (Novo) ---")
print("( Criado por Yudhi Gerson. Todos os direitos reservados. 100% Humano. )")

while True:
    cmd = input("Digite um comando (Aperte Enter para continuar, [ajuda] para comandos): ").lower().strip()
    
    if cmd == "[sair]":
        print("Até mais, pequeno matemático!")
        break
    elif cmd == "[collatz]":
        # função de collatz
        pass
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
        [comparar3]: Compara três números pela soma acumulativa e passos no Collatz
        [passos]: Foca exclusivamente nos passos
        [numerar]: Enumera os passos do Collatz
        """)
    elif cmd == "[acumulo]":
        # função de acúmulo
        pass
    elif cmd == "[colbuddy]":
        # função de CollatzBuddy
        pass
    elif cmd == "[escolher]":
        # função de escolher
        pass
    elif cmd == "[separador]":
        # função do separador
        pass
    elif cmd == "[comparar]":
        # função de comparar 2 números
        pass
    elif cmd == "[comparar3]":
        # função de comparar 3 números
        pass
    elif cmd == "[passos]":
        # função de passos
        pass
    elif cmd == "[numerar]":
        # função de numerar
        pass
    else:
        print("ERRO: Comando não reconhecido. Digite [ajuda] para comandos disponíveis.")
