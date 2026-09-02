usuario_correto = "admin"
senha_correta = "python123"

for tentativa in range(3):
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        print("Usuário ou senha incorretos.")
else:
    print("Acesso bloqueado após 3 tentativas.")