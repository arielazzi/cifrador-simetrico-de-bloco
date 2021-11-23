import permutedChoises

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
    while(len(fileValue) % 48 != 0):
        fileValue += '0'

    #blocos
    output = [fileValue[i:i + 48] for i in range(0, len(fileValue), 48)]
    
    #permutação do arquivo
    #mix_blocks(fileValue, permutedChoises.PaddingChoises.pc2)

    #separacao dos blocos em left e right
    for block in output:
        print()
        print('initial block')
        print(block)
        left_part_of_block = block[0:16]
        right_part_of_block = block[16:48]

        first_key = keys[0]
        second_key = keys[1]
        third_key = keys[2]

        encrypted_right_part = ''

        for i in range(0, len(right_part_of_block)):
            encrypted_right_part += xor(right_part_of_block[i], first_key[i])

        block = left_part_of_block + encrypted_right_part
        print('block after first key xor')
        print(block)

        ## todo: create function to avoid duplication of following lines
        right_part_of_block = encrypted_right_part
        encrypted_right_part = ''

        for i in range(0, len(right_part_of_block)):
            encrypted_right_part += xor(right_part_of_block[i], second_key[i])

        block = left_part_of_block + encrypted_right_part
        print('block after second key xor')
        print(block)

        ## todo: create function to avoid duplication of following lines
        right_part_of_block = encrypted_right_part
        encrypted_right_part = ''

        for i in range(0, len(right_part_of_block)):
            encrypted_right_part += xor(right_part_of_block[i], third_key[i])

        block = left_part_of_block + encrypted_right_part
        print('final block after third key xor')
        print(block)


def decrypt(keys, data):
    print('decrypt')


def binary_to_string(binary):
    binary_text = ''
    for letter in range(0, len(binary)):
        binary_text += format(binary[letter], "b").zfill(8)
    return binary_text


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

