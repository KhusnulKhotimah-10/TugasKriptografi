def columnar_encrypt(text, key):
    key = ''.join(ch for ch in key if not ch.isspace())
    if not key or not key.isalpha():
        raise ValueError("Kunci harus berupa kata.")
    if len(set(key.upper())) != len(key):
        raise ValueError("Gunakan kunci dengan huruf yang berbeda.")

    text = ''.join(ch for ch in text.upper() if ch.isalpha())
    if not text:
        return ""

    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    padded = text.ljust(rows * cols, 'X')

    matrix = [padded[i:i + cols] for i in range(0, len(padded), cols)]

    # Urutan kolom ditentukan oleh urutan alfabet huruf pada kunci.
    order = sorted(range(cols), key=lambda i: key.upper()[i])

    cipher = []
    for col in order:
        for row in matrix:
            cipher.append(row[col])

    return ''.join(cipher)


def columnar_decrypt(ciphertext, key):
    key = ''.join(ch for ch in key if not ch.isspace())
    if not key or not key.isalpha():
        raise ValueError("Kunci harus berupa kata.")
    if len(set(key.upper())) != len(key):
        raise ValueError("Gunakan kunci dengan huruf yang berbeda.")

    cipher = ''.join(ch for ch in ciphertext.upper() if ch.isalpha())
    if not cipher:
        return ""

    cols = len(key)
    if len(cipher) % cols != 0:
        raise ValueError("Panjang cipherteks harus merupakan kelipatan panjang kunci.")

    rows = len(cipher) // cols
    matrix = [[''] * cols for _ in range(rows)]

    order = sorted(range(cols), key=lambda i: key.upper()[i])

    pos = 0
    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[pos]
            pos += 1

    plain = ''.join(''.join(row) for row in matrix)
    return plain.rstrip('X')


def main():
    print("=" * 45)
    print("   APLIKASI COLUMNAR TRANSPOSITION CIPHER")
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
                print("Cipherteks :", columnar_encrypt(text, key))
            else:
                print("Plainteks  :", columnar_decrypt(text, key))
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
