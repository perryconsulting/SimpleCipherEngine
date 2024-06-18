class SimpleCipherEngine:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._offset = None
        self._plaintext = None
        self._ciphertext = None
        self._keyword = None

    def get_offset(self):
        return self._offset

    def get_plaintext(self):
        return self._plaintext

    def get_ciphertext(self):
        return self._ciphertext

    def get_keyword(self):
        return self._keyword

    def set_offset(self, offset):
        if not isinstance(offset, int):
            raise TypeError("Offset must be an integer")
        self._offset = offset

    def set_plaintext(self, plaintext):
        if not isinstance(plaintext, str):
            raise TypeError("Plaintext must be of type: string")
        self._plaintext = plaintext.upper()

    def set_ciphertext(self, ciphertext):
        if not isinstance(ciphertext, str):
            raise TypeError("Ciphertext must be of type: string")
        self._ciphertext = ciphertext.upper()

    def set_keyword(self, keyword):
        if not isinstance(keyword, str):
            raise TypeError("Keyword must be of type: string")
        self._keyword = keyword.upper()

    def print_ciphertext(self):
        print("Your encrypted text is:\n{}".format(self.get_ciphertext()))

    def print_plaintext(self):
        print("Your decrypted text is:\n{}".format(self.get_plaintext()))

    def caesar_encrypt(self):
        temp_plaintext = self.get_plaintext()
        temp_ciphertext = ""
        temp_offset = self.get_offset()

        for char in temp_plaintext:
            if char in self.alphabet:
                character_value = self.alphabet.find(char)
                temp_ciphertext += self.alphabet[(character_value - temp_offset) % len(self.alphabet)]
            else:
                temp_ciphertext += char

        self.set_ciphertext(temp_ciphertext)

    def caesar_decrypt(self):
        temp_plaintext = ""
        temp_ciphertext = self.get_ciphertext()
        temp_offset = self.get_offset()

        for char in temp_ciphertext:
            if char in self.alphabet:
                character_value = self.alphabet.find(char)
                temp_plaintext += self.alphabet[(character_value + temp_offset) % len(self.alphabet)]
            else:
                temp_plaintext += char

        self.set_plaintext(temp_plaintext)

    def caesar_decrypt_brute_force(self):
        for i in range(1, len(self.alphabet) + 1):
            self.set_offset(i)
            print("Offset: {}".format(self.get_offset()))
            self.caesar_decrypt()
            print("\t {}".format(self.get_plaintext()))

    def calculate_vigenere_keyphrase(self, message):
        temp_keyword = self.get_keyword()
        keyword_phrase = ""
        keyword_index = 0
        for char in message:
            if keyword_index >= len(temp_keyword):
                keyword_index = 0
            if char in self.alphabet:
                keyword_phrase += temp_keyword[keyword_index]
                keyword_index += 1
            else:
                keyword_phrase += char
        return keyword_phrase

    def vigenere_encrypt(self):
        temp_plaintext = self.get_plaintext()
        temp_ciphertext = ""
        keyword_phrase = self.calculate_vigenere_keyphrase(temp_plaintext)

        for i in range(len(temp_plaintext)):
            if temp_plaintext[i] in self.alphabet:
                old_char_index = self.alphabet.find(temp_plaintext[i])
                offset_index = self.alphabet.find(keyword_phrase[i])
                new_char = self.alphabet[(old_char_index - offset_index) % 26]
                temp_ciphertext += new_char
            else:
                temp_ciphertext += temp_plaintext[i]

        self.set_ciphertext(temp_ciphertext)

    def vigenere_decrypt(self):
        temp_plaintext = ""
        temp_ciphertext = self.get_ciphertext()
        keyword_phrase = self.calculate_vigenere_keyphrase(temp_ciphertext)

        for i in range(len(temp_ciphertext)):
            if temp_ciphertext[i] in self.alphabet:
                old_char_index = self.alphabet.find(temp_ciphertext[i])
                offset_index = self.alphabet.find(keyword_phrase[i])
                new_char = self.alphabet[(old_char_index + offset_index) % 26]
                temp_plaintext += new_char
            else:
                temp_plaintext += temp_ciphertext[i]

        self.set_plaintext(temp_plaintext)


def main_menu():
    cipher = SimpleCipherEngine()
    option = None
    STR_CIPHERTEXT = "Enter a ciphertext: "
    STR_PLAINTEXT = "Enter a plaintext: "
    STR_KEYWORD = "Enter a keyword: "
    STR_OFFSET = "Enter a offset: "

    while option != "Q":
        print("\nWelcome to the Simple Cipher Engine.\n")
        print("Select an option:")
        print("1. Caesar Encrypt")
        print("2. Caesar Decrypt (Known Offset)")
        print("3. Caesar Decrypt (Brute Force)")
        print("4. Vigenère Encrypt")
        print("5. Vigenère Decrypt")
        print("Q. Exit")
        option = input()
        if option == "1":
            cipher.set_plaintext(input(STR_PLAINTEXT))
            cipher.set_offset(int(input(STR_OFFSET)))
            cipher.caesar_encrypt()
            cipher.print_ciphertext()
            continue
        if option == "2":
            cipher.set_ciphertext(input(STR_CIPHERTEXT))
            cipher.set_offset(int(input(STR_OFFSET)))
            cipher.caesar_decrypt()
            cipher.print_plaintext()
            continue
        if option == "3":
            cipher.set_ciphertext(input(STR_CIPHERTEXT))
            cipher.caesar_decrypt_brute_force()
            continue
        if option == "4":
            cipher.set_plaintext(input(STR_PLAINTEXT))
            cipher.set_keyword(input(STR_KEYWORD))
            cipher.vigenere_encrypt()
            cipher.print_ciphertext()
            continue
        if option == "5":
            cipher.set_ciphertext(input(STR_CIPHERTEXT))
            cipher.set_keyword(input(STR_KEYWORD))
            cipher.vigenere_decrypt()
            cipher.print_plaintext()
            continue
        if option.upper() == "Q":
            print("""
            *************************************************
            * Thank you for using the Simple Cipher Engine. *
            * Goodbye.                                      *
            *************************************************
            """)
            break


# Main entry point
if __name__ == '__main__':
    main_menu()
    exit(0)
