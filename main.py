import cypher
import utils
import permutedChoises

# blocos de 48 bits
# chave de 32 bits

print('Cifrador simétrico de bloco')
file = utils.load_file()

def menu():
    print("[1] Cifrar")
    print("[2] Decifrar")
    print("[0] Sair")

menu()
operation = int(input("Escolha uma opção: "))

user_provided_key = ''
while len(user_provided_key.encode('utf-8')) != 4:
    user_provided_key = input("Informe o valor da chave (4 bytes): ")

keys = cypher.key_schedule(user_provided_key.encode('utf-8'), permutedChoises.PaddingChoises.pc1)

if(operation == 1):
    encrypted_file_text = cypher.encrypt(keys, file.read())
    utils.write_text_in_file(open(file.name.replace('txt','encrypted.txt'), 'w+b'), encrypted_file_text, True)
elif(operation == 2):
    decrypted_file_text = cypher.decrypt(keys, utils.binary_file_to_string(file))
    new_file = open(file.name + '_decrypted.txt', 'w', newline='')
    new_file.write(decrypted_file_text)
    new_file.close()
else:
    print("Fim.")
