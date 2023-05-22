dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def enkripsiPesan(key, pesan):
    return EnkripsiVinegere(key, pesan)


def EnkripsiVinegere(key, pesan):
    enkripsi_hasil = []
    keyIndex = 0
    key = key.upper()

    for karakter in pesan:
        num = dict.find(karakter.upper())
        if num != -1:
            num = num + dict.find(key[keyIndex])
            num %= len(dict)

            enkripsi_hasil.append(dict[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            enkripsi_hasil.append(karakter)

    return ''.join(enkripsi_hasil)

def polybiusCipher(s):
    enkripsi = ''
    for karakter in s:
        if karakter == " ":
            enkripsi += "  "
        elif karakter == ",":
            enkripsi += ", "
        elif karakter == ".":
            enkripsi += ". "
        else:
            row = int((ord(karakter) - ord('a')) / 5) + 1
            col = ((ord(karakter) - ord('a')) % 5) + 1
            if karakter == 'k':
                row = row - 1
                col = 5 - col + 1
            elif ord(karakter) >= ord('j'):
                if col == 1:
                    col = 6
                    row = row - 1
                col = col - 1
            r = str(row)
            c = str(col)
            enkripsi = enkripsi + r + c
    return enkripsi

inputan = open(str(input("Masukkan nama file untuk di enkripsi : ")), 'r')
pesan = inputan.read()

password = str(input("Masukkan Password untuk melakukan enkripsi :"))

enkripsi_vigenere = enkripsiPesan(password, pesan)
enkripsi_polybius = polybiusCipher(enkripsi_vigenere)
hasil_enkripsi = open("pesan_enkripsi.txt", "w")
hasil_enkripsi.write(enkripsi_polybius)

print("================================================================================")
print("Pesan awal : " + pesan)
print("Vigenere :  "+ enkripsi_vigenere)
print("Polybius :" + enkripsi_polybius)
print("================================================================================")
print("Hasil enkripsi tersimpan sebagai pesan_enkripsi.txt")
