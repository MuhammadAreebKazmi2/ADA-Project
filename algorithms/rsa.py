import random

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.public_key, self.private_key = self.generate_keypair()

    def square_and_multiply(self, base, exponent, modulus):
        result = 1
        base = base % modulus

        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent = exponent // 2
            base = (base * base) % modulus

        return result

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def extended_gcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def mod_inverse(self, a, m):
        g, x, y = self.extended_gcd(a, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def generate_keypair(self):
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)

        while True:
            e = random.randrange(2, phi)
            if self.gcd(e, phi) == 1:
                break

        d = self.mod_inverse(e, phi)
        
        return ((e, n), (d, n))

    def encrypt(self, plaintext):
        e, n = self.public_key
        ciphertext = [self.square_and_multiply(ord(char), e, n) for char in plaintext]
        return ciphertext

    def decrypt(self, ciphertext):
        d, n = self.private_key
        decrypted = [chr(self.square_and_multiply(char, d, n)) for char in ciphertext]
        return ''.join(decrypted)
