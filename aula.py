nome=input("Digite o nome do paciente : ")
idade=int(input("Digite a idade do Paciente : "))

if idade >= 65:
 print("O paciente "+ nome + " possui atendimento prioritário.")
else:
 print("O paciente "+ nome +" NÃO possui atendimento prioritário.")
print("Atendimento Finalizado.")