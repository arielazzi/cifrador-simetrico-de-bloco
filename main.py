import cypher
import utils

# blocos de 48 bits
# chave de 32 bits

print('Cifrador simétrico de bloco')
file = utils.load_file()

user_provided_key = ''
while len(user_provided_key.encode('utf-8')) != 4:
    user_provided_key = input("Informe o valor da chave (4 bytes): ")

pc1 = [16, 0, 19, 28, 3, 14, 13, 31, 12, 1, 22, 23, 29, 24, 15, 30, 6, 9, 21, 10, 2, 4, 5, 17, 7, 27, 18, 26, 11, 8, 25, 20]

keys = cypher.key_schedule(user_provided_key.encode('utf-8'), pc1)
print(keys)
cypher.encrypt(keys, file.read())
