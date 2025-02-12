alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    chipher_text = ""  # Başlangıçta boş olmalı
    
    for letter in original_text:
        if letter in alphabet:  # Sadece harfler şifrelenecek
            sum_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            chipher_text += alphabet[sum_index]
        else:
            chipher_text += letter  # Özel karakterler olduğu gibi eklenmeli

    print(f"Encrypted text: {chipher_text}")
encrypt(original_text=text, shift_amount=shift)

def dycrpt(orginal_text,shift_amount):
    chipher_text=""
    for letter in orginal_text:
        sum_index=(alphabet.index(letter)-shift_amoun)%len(alphabet)
        chipher_text+=sum_index
    print(f"dycript text: {chipher_text}")
encrypt(original_text=text, shift_amount=shift)
