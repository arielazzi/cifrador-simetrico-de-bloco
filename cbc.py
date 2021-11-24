import secrets
import utils

def generate_input_ecc(block, previousBlock) -> bytes:

    if previousBlock is None:
        previousBlock = bin(int.from_bytes(secrets.token_bytes(6), 'big'))[2:].zfill(48)
        utils.write_file_in_bytes(previousBlock, "random.bin")


    result = int(block, 2)^int(previousBlock,2)
    return bin(result)[2:].zfill(len(block))


def generate_ouput_ecc(block, previousBlock) -> bytes:
    
    if previousBlock is None:
        previousBlock = open("random.bin", 'rb').read()
        previousBlock = bin(int.from_bytes(previousBlock, 'big'))[2:].zfill(48)


    result = int(block, 2)^int(previousBlock,2)

    return bin(result)[2:].zfill(len(block))

