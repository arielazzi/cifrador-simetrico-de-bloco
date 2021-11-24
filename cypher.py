import permutedChoises
import cbc

def key_schedule(user_provided_key, permuted_choice):
    keys = []
    bin_user_provided_key = binary_to_string(user_provided_key)
    keys.append(mix_blocks(bin_user_provided_key, permuted_choice))
    keys.append(mix_blocks(keys[0], permuted_choice))
    keys.append(mix_blocks(keys[1], permuted_choice))

    return keys

def xor(a, b):
    return '0' if a == b else '1'

def encrypt(keys, data):
    fileValue = binary_to_string(data)

    #padding
    #preenche com zeros até quantidade de bits ser divisível por 48
    initial_file_len = len(fileValue)
    while(len(fileValue) % 48 != 0):
        fileValue += '0'

    final_file_len = len(fileValue) - initial_file_len

    #blocos
    output = [fileValue[i:i + 48] for i in range(0, len(fileValue), 48)]

    encrypted_file_value = ''
    previousBlock = None

    #separacao dos blocos em left e right
    for block in output:
        print()
        print('initial block')
        print(block)

        block = cbc.generate_input_ecc(block, previousBlock)
        previousBlock = block

        print('initial block 2')
        print(block)

        #permutacao
        permuted_block = mix_blocks(block, permutedChoises.PaddingChoises.pc2)

        left_part_of_block = permuted_block[0:16]
        right_part_of_block = permuted_block[16:48]

        keyIndex = 0
        encrypted_right_part = ''

        while( keyIndex < 3):
            for i in range(0, len(right_part_of_block)):
                encrypted_right_part += xor(right_part_of_block[i], keys[keyIndex][i])

            permuted_block = left_part_of_block + encrypted_right_part
            #print('block after ' + str(keyIndex + 1) + ' key xor')
            #print(permuted_block)
            right_part_of_block = encrypted_right_part
            encrypted_right_part = ''
            keyIndex = keyIndex + 1

        encrypted_file_value += permuted_block
    print("arquivo encriptado: ")
    print(encrypted_file_value)
    print("encrypt end")
    return bin(final_file_len)[2:].zfill(8) + encrypted_file_value

def decrypt(keys, data):
    padding_size = int(data[0:8], 2)
    fileValue = data[8:]
    #blocos
    output = [fileValue[i:i + 48] for i in range(0, len(fileValue), 48)]

    decrypted_file_bin_value = ''
    previousBlock = None
      #separacao dos blocos em left e right
    for block in output:
        print()
        print('initial block')

        
        left_part_of_block = block[0:16]
        right_part_of_block = block[16:48]

        keyIndex = 0
        decrypted_right_part = ''

        while( keyIndex < 3):
            for i in range(0, len(right_part_of_block)):
                decrypted_right_part += xor(right_part_of_block[i], keys[keyIndex][i])

            block = left_part_of_block + decrypted_right_part
            #print('block after ' + str(keyIndex + 1) + ' key xor')
            #print(permuted_block)
            right_part_of_block = decrypted_right_part
            decrypted_right_part = ''
            keyIndex = keyIndex + 1
        
        #desfaz permutação
        not_permuted_block = undo_mix_blocks(block)
        temp = not_permuted_block
        not_permuted_block = cbc.generate_ouput_ecc(not_permuted_block, previousBlock)
        previousBlock = temp

        decrypted_file_bin_value += not_permuted_block
    print("arquivo decriptado: ")
    print(decrypted_file_bin_value)
    decrypted_file_value = decode_binary_string(decrypted_file_bin_value[:len(decrypted_file_bin_value) - padding_size])
    print("decrypt end")
    return decrypted_file_value


def binary_to_string(binary):
    binary_text = ''
    for letter in range(0, len(binary)):
        binary_text += format(binary[letter], "b").zfill(8)
    return binary_text

def decode_binary_string(string):
    return ''.join(chr(int(string[i*8:i*8+8],2)) for i in range(len(string)//8))

def mix_blocks(bin_user_provided_key, permuted_choice):
    blocks = ''
    for i in range(0, len(bin_user_provided_key)):
        blocks += bin_user_provided_key[permuted_choice.value[i]]
    
    if(permuted_choice == permutedChoises.PaddingChoises.pc1):
        block1 = blocks[0:8]
        block2 = blocks[8:16]
        block3 = blocks[16:24]
        block4 = blocks[24:32]
        return block3 + block4 + block2 + block1
    
    #pc2
    block1 = blocks[0:8]
    block2 = blocks[8:16]
    block3 = blocks[16:24]
    block4 = blocks[24:32]
    block5 = blocks[32:40]
    block6 = blocks[40:48]
    return block6 + block3 + block5 + block4 + block2 + block1

def undo_mix_blocks(bin_user_provided_key):   
    block1 = bin_user_provided_key[0:8]
    block2 = bin_user_provided_key[8:16]
    block3 = bin_user_provided_key[16:24]
    block4 = bin_user_provided_key[24:32]
    block5 = bin_user_provided_key[32:40]
    block6 = bin_user_provided_key[40:48]

    return block6 + block5 + block2 + block4 + block3 + block1



