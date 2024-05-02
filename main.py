from algorithms.caesar_cipher import CaesarCipher
from algorithms.rsa import RSA
from algorithms.merkle2 import MerkleHellmanKnapsack
import os, time, psutil

def run_caesar_cipher(text):
    _caeser_cipher = CaesarCipher(shift=3)

    t1 = time.perf_counter()
    process = psutil.Process(os.getpid())
    before_memory = process.memory_info().rss / (1024 ** 2)  # Convert bytes to MiB


    encrypted_text = _caeser_cipher.encrypt(text)
    after_memory = process.memory_info().rss / (1024 ** 2)
    t2 = time.perf_counter()

    print("Memory used for encryption: {} KB".format(after_memory - before_memory))
    print("Time taken for encryption: {:.5f} seconds".format(t2 - t1))

    t1 = time.perf_counter()
    before_memory = process.memory_info().rss / (1024 ** 2)

    decrypted_text = _caeser_cipher.decrypt(encrypted_text)
    after_memory = process.memory_info().rss / (1024 ** 2)
    t2 = time.perf_counter()

    print("Memory used for decryption: {} KB".format(after_memory - before_memory))
    print("Time taken for decryption: {:.5f} seconds".format(t2 - t1))

    # print("Encrypted text: ", encrypted_text)
    # print("")
    # print("Decrypted text: ", decrypted_text)
    # print("")



def run_rsa(text):
    
    _rsa = RSA(p=61, q=53)

    t1 = time.perf_counter()
    process = psutil.Process(os.getpid())
    before_memory = process.memory_info().rss / (1024 ** 2)

    encrypted_text = _rsa.encrypt(text)

    after_memory = process.memory_info().rss / (1024 ** 2)
    t2 = time.perf_counter()

    print("Memory used for encryption: {} KB".format(after_memory - before_memory))
    print("Time taken for encryption: {:.5f} seconds".format(t2 - t1))

    t1 = time.perf_counter()
    before_memory = process.memory_info().rss / (1024 ** 2)
    decrypted_text = _rsa.decrypt(encrypted_text)
    after_memory = process.memory_info().rss / (1024 ** 2)
    t2 = time.perf_counter()
    
    print("Memory used for decryption: {} KB".format(after_memory - before_memory))
    print("Time taken for decryption: {:.5f} seconds".format(t2 - t1))

    # print("Encrypted text: ", encrypted_text)
    # print("")
    # print("Decrypted text: ", decrypted_text)
    # print("")


def run_knapsack(text):
    
    _knapsack = MerkleHellmanKnapsack(key_length=8)

    t1 = time.perf_counter()
    process = psutil.Process(os.getpid())
    before_memory = process.memory_info().rss / (1024 ** 2)

    encrypted_text = _knapsack.encrypt(text)

    after_memory = process.memory_info().rss / (1024 ** 2)
    t2 = time.perf_counter()

    print("Memory used for encryption: {} KB".format(after_memory - before_memory))
    print("Time taken for encryption: {:.5f} seconds".format(t2 - t1))

    t1 = time.perf_counter()
    before_memory = process.memory_info().rss / (1024 ** 2)
    decrypted_text = _knapsack.decrypt(encrypted_text)
    after_memory = process.memory_info().rss / (1024 ** 2)
    t2 = time.perf_counter()
    
    print("Memory used for decryption: {} KB".format(after_memory - before_memory))
    print("Time taken for decryption: {:.5f} seconds".format(t2 - t1))

    # print("Encrypted text: ", encrypted_text)
    # print("")
    # print("Decrypted text: ", decrypted_text)
    # print("")


def get_option_input():
    
    available_options = {
        "1" : run_caesar_cipher,
        "2" : run_rsa,
        "3" : run_knapsack
    }

    print("Select an option below:\n")
    print("1) Caesar Cipher")
    print("2) RSA")
    print("3) Knapsack")

    option = input(">>> ")

    if option in available_options:
        return available_options[option]

    print("Invalid option!")
    exit()

def get_txt_file_path():

    user_path = input("Enter txt file path:\n>>> ")

    if os.path.exists(user_path) and user_path.endswith(".txt"):
        return user_path

    print("Invalid path!")
    exit()

def main():
    
    cipher_function = get_option_input()

    file_path = get_txt_file_path()


    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

        cipher_function(text)
        


if __name__ == "__main__":
    main()