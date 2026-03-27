import string
import secrets

def gerar_senha(tamanho=16):
    # Define os caracteres possíveis: letras, números e pontuação
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Garante que a senha seja gerada de forma aleatória e segura
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Execução do programa
if __name__ == "__main__":
    print("--- Gerador de Senhas Seguras ---")
    try:
        qtd = int(input("Quantos caracteres você quer na senha? "))
        nova_senha = gerar_senha(qtd)
        print(f"\nSua nova senha é: {nova_senha}")
        print("---------------------------------")
    except ValueError:
        print("Erro: Por favor, digite apenas números.")