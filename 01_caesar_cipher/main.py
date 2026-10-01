def caesar_encrypt(text, key):
    result = []
    for ch in text:
        if ch.isalpha() and ch.isascii():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + key) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)


def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)


def main():
    print("=" * 45)
    print("      APLIKASI CAESAR CIPHER")
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
        try:
            key = int(input("Masukkan kunci/pergeseran (0-25): "))
            if not 0 <= key <= 25:
                raise ValueError
        except ValueError:
            print("Kunci harus berupa bilangan 0 sampai 25.")
            continue

        if choice == "1":
            print("Cipherteks :", caesar_encrypt(text, key))
        else:
            print("Plainteks  :", caesar_decrypt(text, key))


if __name__ == "__main__":
    main()
