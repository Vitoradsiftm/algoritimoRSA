from rsa import generate_keys, encrypt, decrypt

def main():
    public_key = None
    private_key = None

    while True:
        print("\n=== RSA - Criptografia Assimétrica ===")
        print("1 - Gerar chaves")
        print("2 - Cifrar mensagem")
        print("3 - Decifrar mensagem")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        # -----------------------------
        # Gerar chaves
        # -----------------------------
        if opcao == "1":
            public_key, private_key = generate_keys()
            print("\n🔓 Chave Pública:", public_key)
            print("🔒 Chave Privada:", private_key)

        # -----------------------------
        # Cifrar
        # -----------------------------
        elif opcao == "2":
            if public_key is None:
                print("\n⚠️ Gere as chaves primeiro!")
                continue

            message = input("Digite a mensagem: ")
            cipher = encrypt(message, public_key)

            print("\n🔐 Mensagem cifrada:")
            print(cipher)

        # -----------------------------
        # Decifrar
        # -----------------------------
        elif opcao == "3":
            if private_key is None:
                print("\n⚠️ Gere as chaves primeiro!")
                continue

            try:
                cipher_input = input("Digite a mensagem cifrada (ex: [123, 456]): ")
                cipher = eval(cipher_input)

                message = decrypt(cipher, private_key)

                print("\n🔓 Mensagem decifrada:")
                print(message)

            except:
                print("\n❌ Erro ao decifrar. Verifique o formato da entrada.")

        # -----------------------------
        # Sair
        # -----------------------------
        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("\n❌ Opção inválida!")

if __name__ == "__main__":
    main()