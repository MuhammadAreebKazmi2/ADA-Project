import random

class MerkleHellmanKnapsack:
    def __init__(self, key_length=8):
        # Initialize key length (number of bits in the message)
        self.key_length = key_length
        
        # Generate private key (superincreasing sequence, multiplier, modulus)
        self.private_key = self.generate_private_key()
        
        # Generate public key from the private key
        self.public_key = self.generate_public_key()

    def generate_private_key(self):
        # Generate a superincreasing sequence
        sequence = [random.randint(1, 10)]
        for _ in range(1, self.key_length):
            sequence.append(random.randint(sum(sequence) + 1, sum(sequence) * 2))
        
        # Generate a random modulus greater than the sum of the sequence
        modulus = random.randint(sum(sequence) + 1, sum(sequence) * 2)
        
        # Generate a multiplier that is coprime to the modulus
        multiplier = random.randint(2, modulus - 1)
        while self.gcd(multiplier, modulus) != 1:
            multiplier = random.randint(2, modulus - 1)
        
        return (sequence, multiplier, modulus)

    def generate_public_key(self):
        # Calculate the public key using the private key
        sequence, multiplier, modulus = self.private_key
        public_key = [(multiplier * x) % modulus for x in sequence]
        return public_key

    def encrypt(self, plaintext):
        # Convert plaintext to a list of ASCII integers
        ascii_values = [ord(char) for char in plaintext]

        # Initialize the list of ciphertext
        ciphertext = []

        # Encrypt each ASCII integer using the public key
        for ascii_value in ascii_values:
            # Convert the ASCII value to binary representation and pad with leading zeros
            binary_representation = format(ascii_value, f'0{self.key_length}b')
            
            # Initialize the dynamic programming table
            dp = [0] * (self.key_length + 1)
            
            # Fill the DP table
            for i in range(1, self.key_length + 1):
                bit = int(binary_representation[i - 1])
                # Calculate the intermediate sum using the previous sum and current public key
                dp[i] = dp[i - 1] + bit * self.public_key[i - 1]
            
            # The final entry in the DP table is the encrypted value for the current ASCII character
            ciphertext.append(dp[self.key_length])

        return ciphertext
    
    def decrypt(self, ciphertext):
        """Decrypt the ciphertext message using the private key."""
        sequence, multiplier, modulus = self.private_key
        
        # Calculate the inverse of the multiplier modulo the modulus
        inv_multiplier = self.modular_inverse(multiplier, modulus)
        
        # Decrypt each ciphertext value using dynamic programming (subset sum problem)
        ascii_values = []
        for value in ciphertext:
            # Multiply the ciphertext value by the inverse multiplier
            adjusted_value = (value * inv_multiplier) % modulus
            
            # Solve the subset sum problem using dynamic programming
            binary_representation = self.solve_subset_sum(sequence, adjusted_value)
            
            # Convert binary representation to ASCII integer
            ascii_value = int(binary_representation, 2)
            
            # Append the ASCII integer to the list of ASCII values
            ascii_values.append(ascii_value)

        # Convert the list of ASCII integers to a plaintext string
        plaintext = ''.join(chr(ascii_value) for ascii_value in ascii_values)
        return plaintext

    def solve_subset_sum(self, sequence, target):
        """Solve the subset sum problem using dynamic programming."""
        n = len(sequence)
        # Initialize the DP table with False values
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(target + 1):
                if dp[i - 1][j]:
                    # Carry over the previous value
                    dp[i][j] = True
                    if j + sequence[i - 1] <= target:
                        dp[i][j + sequence[i - 1]] = True
        
        # Backtrack to find the binary representation
        binary_representation = []
        i, j = n, target
        while i > 0:
            if j >= sequence[i - 1] and dp[i - 1][j - sequence[i - 1]]:
                binary_representation.append('1')
                j -= sequence[i - 1]
            else:
                binary_representation.append('0')
            i -= 1
        
        # Reverse the binary representation and return it as a string
        binary_representation.reverse()
        return ''.join(binary_representation)

    def gcd(self, a, b):
        """Calculate the greatest common divisor using the Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    def modular_inverse(self, a, m):
        """Calculate the modular inverse using the Extended Euclidean algorithm."""
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

# # Example usage of the Merkle-Hellman knapsack cryptosystem
# def main():
#     # Initialize the cryptosystem with a key length of 8 bits
#     cryptosystem = MerkleHellmanKnapsack(key_length=8)
    
#     # Define a plaintext message
#     plaintext = "Taylor Alison Swift (born December 13, 1989) is an American singer-songwriter. Her reinventive artistry, distinctive songwriting and entrepreneurship have been widely publicized and influential. Swift began professional songwriting at age 14. She signed with Big Machine Records in 2005 and achieved prominence as a country pop singer with the albums Taylor Swift (2006) and Fearless (2008). Their singles Teardrops on My Guitar, Love Story, and You Belong with Me were crossover successes on country and pop radio formats and brought Swift mainstream fame. She experimented with rock and electronic styles on her next albums, Speak Now (2010) and Red (2012), respectively, with the latter featuring her first Billboard Hot 100 number-one single, We Are Never Ever Getting Back Together. Swift recalibrated her image from country to pop with 1989 (2014), a synth-pop album containing the chart-topping songs Shake It Off, Blank Space, and Bad Blood. Media scrutiny inspired the hip-hop-influenced Reputation (2017) and its number-one single Look What You Made Me Do. After signing with Republic Records in 2018, Swift released the eclectic pop album Lover (2019) and the autobiographical documentary Miss Americana (2020). She explored indie folk styles on the 2020 albums Folklore and Ev"
#     # Encrypt the plaintext
#     ciphertext = cryptosystem.encrypt(plaintext)
#     print("Ciphertext:", ciphertext)
    
#     # Decrypt the ciphertext
#     decrypted_text = cryptosystem.decrypt(ciphertext)
#     print("Decrypted text:", decrypted_text)

# if __name__ == "__main__":
#     main()
