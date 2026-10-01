# Caesar Cipher

Aplikasi sederhana Caesar Cipher menggunakan Python.

## Fitur
- Enkripsi pesan
- Dekripsi pesan
- Kunci/pergeseran 0–25
- Spasi dan tanda baca dipertahankan

## Rumus
Enkripsi: `c = (p + k) mod 26`  
Dekripsi: `p = (c - k) mod 26`

Konsep ini mengikuti materi Ragam Cipher Klasik Bagian 1.

## Cara menjalankan
```bash
python main.py
```

## Contoh
Plainteks: `ADA RENCANA`  
Kunci: `5`

Hasil enkripsi: `FIF WJSHFSF`
