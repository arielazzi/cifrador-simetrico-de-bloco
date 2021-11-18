import cypher
import utils

# blocos de 48 bits
# chave de 32 bits

print('Cifrador simétrico de bloco')
file = utils.load_file()

user_provided_key = ''
while len(user_provided_key.encode('utf-8')) != 4:
    user_provided_key = input("Informe o valor da chave (4 bytes): ")

pc1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

keys = cypher.key_schedule(user_provided_key.encode('utf-8'), pc1)
print(keys)
cypher.encrypt(keys, file.read())
