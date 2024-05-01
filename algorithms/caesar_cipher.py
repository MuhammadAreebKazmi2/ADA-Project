class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                shift_value = self.shift % 26  # Ensure shift is within range
                if char.isupper():
                    result += chr((ord(char) - 65 + shift_value) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 + shift_value) % 26 + 97)
            else:
                result += char  # Leave special characters and numbers unchanged
        return result

    def decrypt(self, text):
        result = ""
        for char in text:
            if char.isalpha():
                shift_value = self.shift % 26  # Ensure shift is within range
                if char.isupper():
                    result += chr((ord(char) - 65 - shift_value) % 26 + 65)
                else:
                    result += chr((ord(char) - 97 - shift_value) % 26 + 97)
            else:
                result += char  # Leave special characters and numbers unchanged
        return result