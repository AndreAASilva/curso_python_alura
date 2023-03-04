def cria_conta(numero, titular, saldo, limite):
    conta = {"nemuro": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def desposita_conta(conta, valor):
    conta["saldo"] += valor

def saca_conta(conta, valor):
    conta["saldo"] -= valor

def extrato_conta(conta):
    print("Saldo é {}". format(conta["saldo"]))
   
