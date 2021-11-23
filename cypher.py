import permutedChoises

def key_schedule(user_provided_key, permuted_choice):
    keys = []
    print(binary_to_string(user_provided_key))
    bin_user_provided_key = binary_to_string(user_provided_key)
    keys.append(mix_blocks(bin_user_provided_key, permuted_choice))
    keys.append(mix_blocks(keys[0], permuted_choice))
    keys.append(mix_blocks(keys[1], permuted_choice))

    return keys

def encrypt(keys, data):
    fileValue = binary_to_string(data)
   
    print(fileValue)
    #padding
    #preenche com zeros até quantidade de bits ser divisível por 48
    while(len(fileValue) % 48 != 0):
        fileValue += '0'

    #blocos
    output=[fileValue[i:i + 48] for i in range(0, len(fileValue), 48)]
    print("blocos")
    print(output)    

    #permutação do arquivo
    #mix_blocks(fileValue, permutedChoises.PaddingChoises.pc2)

    print('encrypt')


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

