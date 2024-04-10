MENU = """
+=====-DIO BANK-=====+

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
4
=> """

SALDO_INICIAL = 0
LIMITE_SAQUES = 3
LIMITE_SALDO = 500

saldo = SALDO_INICIAL
extrato = ""
numero_saques = 0

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
    else:
        print("Operação inválida, tente novamente!")

def sacar(valor):
    global saldo, extrato, numero_saques
    excedeu_saldo = valor > saldo
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação inválida, tente novamente!")
    elif excedeu_saques:
        print("Operação inválida, tente novamente!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação inválida, tente novamente!")

while True:
    MENU = """
+=====-DIO BANK-=====+
    
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Saldo: R$ {:.2f}

=> """.format(saldo)

    opcao = input(MENU)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        depositar(valor)
    
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        sacar(valor)
    
    elif opcao == "3":
        print("     Extrato")
        print("====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================")
    
    elif opcao == "4":
        break
    
    else:
        print("Operação inválida, tente novamente!")