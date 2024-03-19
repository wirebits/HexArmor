# HexArmor
# A tool that encodes and decodes text using a password in .txt files using Hexadecimal.
# Author - WireBits

import argparse

def hex_encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(hex((ord(message[i]) + ord(key_c)) % 256)[2:])
    return "".join(enc)

def hex_decode(key, message):
    dec = []
    for i in range(0, len(message), 2):
        hex_chunk = message[i:i+2]
        hex_value = int(hex_chunk, 16)
        key_c = key[(i//2) % len(key)]
        dec.append(chr((256 + hex_value - ord(key_c)) % 256))
    return "".join(dec)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HexArmor")
    parser.add_argument("-e", "--encode", action="store_true", help="Encode the input text")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the input text")
    parser.add_argument("-p", "--key", required=True, help="Key to encode/decode the text")
    parser.add_argument("-i", "--input", required=True, help="Input string or text file")
    parser.add_argument("-o", "--output", required=True, help="Output file to store the result")

    args = parser.parse_args()

    if args.encode:
        if args.input.endswith('.txt'):
            with open(args.input, 'r') as file:
                message = file.read()
        else:
            message = args.input
        result = hex_encode(args.key, message)
    elif args.decode:
        if args.input.endswith('.txt'):
            with open(args.input, 'r') as file:
                message = file.read()
        else:
            message = args.input
        result = hex_decode(args.key, message)

    with open(args.output, "w") as file:
        file.write(result)

    print(f"Text has been written to {args.output}!")