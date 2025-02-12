alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""  # Doğru değişken ismi
    
    for letter in original_text:
        if letter in alphabet:  # Sadece harfler şifrelenecek
            new_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[new_index]
        else:
            cipher_text += letter  # Özel karakterler olduğu gibi eklenmeli

    print(f"Encrypted text: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""

    for letter in original_text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift_amount) % len(alphabet)
            cipher_text += alphabet[new_index]
        else:
            cipher_text += letter  # Özel karakterler olduğu gibi eklenmeli

    print(f"Decrypted text: {cipher_text}")

if direction == "encode":
    encrypt(original_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(original_text=text, shift_amount=shift)
else:
    print("Invalid option. Please type 'encode' or 'decode'.")

