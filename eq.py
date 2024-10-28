import sys

def obter_resposta(prompt):
    while True:
        resposta = input(prompt).strip().lower()
        if resposta in ["sim", "não"]:
            return resposta
        print("Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

resposta = "S"


print(" === Olá, seja bem vindo a loja de ferramentas e equipamentos do Pietro")
resposta=obter_resposta("Para começar, Você deseja entrar na Loja?, (sim/não): ")

if resposta == "não":
    print("Você não quis entrar na loja.")
    sys.exit()

print("Você escolheu entrar na loja, muito bem!")

equipamento=[]
valor=[]
numeroS=[]
departamento=[]


while True:

 equipamento.append(input("Digite o nome do equipamento desejado : "))
 valor.append(input("Digite o valor do equipamento : "))
 numeroS.append(input("Digite o Numero Serial do equipamento : "))
 departamento.append(input("Perfeito, agora para finalizar a busca do seu produto, Digite o departamento/empresa : "))
 resposta = input("Produto encontrado na Prateleira de Numero 30. Deseja continuar? \"S\"para continuar : ").upper()

 if resposta != "S":
        break
 
for indice in range(len(equipamento)):
    print("\nEquipamento . . : ", (indice + 1))
    print("Nome . . . . . . : ", equipamento[indice])
    print("Valor . . . . . . : ", valor[indice])
    print("Número S . . . . : ", numeroS[indice])
    print("Departamento . . . : ", departamento[indice])

print("\nBusca finalizada.")
 