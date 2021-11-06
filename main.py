import cypher
import utils

# blocos de 48 bits
# chave de 32 bits

print('Cifrador simétrico de bloco')
file = utils.load_file()

user_provided_key = ''
while len(user_provided_key.encode('utf-8')) != 4:
    user_provided_key = input("Informe o valor da chave (4 bytes): ")

keys = cypher.key_schedule(user_provided_key.encode('utf-8'))
cypher.encrypt(keys, file.read())
