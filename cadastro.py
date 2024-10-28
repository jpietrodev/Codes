print(" == Olá, Por favor digite o seu nome de usuario ==")

nome = input("Seu nome de usuario : ")
print(nome)


senha = input("Perfeito agora digite uma senha segura")
print(senha)


confirmarsenha = input("Confirme sua senha")
print(confirmarsenha)

if confirmarsenha == senha:
 print("Senha confirmada.")
else:
 print("As senhas não concidem")