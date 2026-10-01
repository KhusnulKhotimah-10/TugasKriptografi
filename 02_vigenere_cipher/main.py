def vigenere_encrypt(text, key):
    key = ''.join(ch.upper() for ch in key if ch.isalpha())
    if not key:
        raise ValueError("Kunci harus mengandung huruf.")

    result = []
    key_index = 0

    for ch in text:
        if ch.isalpha() and ch.isascii():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(ch)

    return ''.join(result)


def vigenere_decrypt(text, key):
    key = ''.join(ch.upper() for ch in key if ch.isalpha())
    if not key:
        raise ValueError("Kunci harus mengandung huruf.")

    result = []
    key_index = 0

    for ch in text:
        if ch.isalpha() and ch.isascii():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(ch)

    return ''.join(result)


def main():
    print("=" * 45)
    print("       APLIKASI VIGENERE CIPHER")
    print("=" * 45)
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    while True:
        choice = input("\nPilih menu [1/2/3]: ").strip()

        if choice == "3":
            print("Program selesai.")
            break

        if choice not in ("1", "2"):
            print("Pilihan tidak valid.")
            continue

        text = input("Masukkan pesan: ")
        key = input("Masukkan kata kunci: ").strip()

        try:
            if choice == "1":
                print("Cipherteks :", vigenere_encrypt(text, key))
            else:
                print("Plainteks  :", vigenere_decrypt(text, key))
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
