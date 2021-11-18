def key_schedule(user_provided_key, permuted_choice):
    keys = []
    print(binary_to_string(user_provided_key))
    bin_user_provided_key = binary_to_string(user_provided_key)
    keys.append(mix_blocks(bin_user_provided_key, permuted_choice))
    keys.append(mix_blocks(keys[0], permuted_choice))
    keys.append(mix_blocks(keys[1], permuted_choice))

    return keys


def encrypt(keys, data):
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
        blocks += bin_user_provided_key[permuted_choice[i]]
    block1 = blocks[0:8]
    block2 = blocks[8:16]
    block3 = blocks[16:24]
    block4 = blocks[24:32]
    return block3 + block4 + block2 + block1

