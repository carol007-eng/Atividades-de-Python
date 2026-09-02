def validar_senha(senha):
    erros = []
    if len(senha) < 8:
        erros.append("menos de 8 caracteres")
    if not any(c.isalpha() for c in senha):
        erros.append("não contém letra")
    if not any(c.isdigit() for c in senha):
        erros.append("não contém número")
    if not any(not c.isalnum() for c in senha):
        erros.append("não contém caractere especial")
    
    if erros:
        print("Senha fraca. Problemas:", ", ".join(erros))
    else:
        print("Senha forte!")

senha = input("Digite uma senha: ")
validar_senha(senha)