import random  # importa funções aleatórias (tipo sortear números)

# -----------------------------
# Teste de primalidade simples
# -----------------------------
def is_prime(n):
    # se for menor que 2, já não é primo
    if n < 2:
        return False
    
    # testa se dá pra dividir por algum número
    # até a raiz quadrada dele
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # se dividir certinho (resto 0)
            return False  # então NÃO é primo
    
    return True  # se passou por tudo, é primo

# -----------------------------
# Gerar número primo
# -----------------------------
def generate_prime(min_value=100, max_value=300):
    while True:
        num = random.randint(min_value, max_value)  # sorteia um número
        if is_prime(num):  # verifica se é primo
            return num  # se for, retorna

# -----------------------------
# MDC (Algoritmo de Euclides)
# -----------------------------
def gcd(a, b):
    # fica trocando os valores até o resto ser 0
    while b != 0:
        a, b = b, a % b
    return a  # esse é o MDC (máximo divisor comum)

# -----------------------------
# Euclides Estendido
# -----------------------------
def extended_gcd(a, b):
    # caso base (quando b vira 0)
    if b == 0:
        return (1, 0, a)
    
    # chamada recursiva (vai quebrando o problema)
    x1, y1, d = extended_gcd(b, a % b)
    
    # recalcula os valores
    x = y1
    y = x1 - (a // b) * y1
    
    return (x, y, d)

# -----------------------------
# Inverso modular
# -----------------------------
def mod_inverse(e, phi):
    x, y, d = extended_gcd(e, phi)
    
    # se MDC não for 1, não existe inverso
    if d != 1:
        raise Exception("Não existe inverso modular")
    
    return x % phi  # retorna o inverso positivo

# -----------------------------
# Geração de chaves RSA
# -----------------------------
def generate_keys():
    # gera dois números primos
    p = generate_prime()
    q = generate_prime()

    # garante que não são iguais
    while q == p:
        q = generate_prime()

    n = p * q  # número público
    phi = (p - 1) * (q - 1)  # totiente

    # escolhe um número e que seja coprimo com phi
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # calcula o d (chave privada)
    d = mod_inverse(e, phi)

    # chave pública e privada
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# -----------------------------
# Cifrar mensagem
# -----------------------------
def encrypt(message, public_key):
    e, n = public_key
    
    # transforma cada letra em número (ASCII)
    # eleva a e e faz mod n
    cipher = [(ord(char) ** e) % n for char in message]
    
    return cipher  # retorna lista de números "embaralhados"

# -----------------------------
# Decifrar mensagem
# -----------------------------
def decrypt(cipher, private_key):
    d, n = private_key
    
    # pega cada número e faz o caminho inverso
    message = ''.join([chr((char ** d) % n) for char in cipher])
    
    return message  # retorna a mensagem original