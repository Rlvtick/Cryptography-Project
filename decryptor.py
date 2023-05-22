def DekripsiPesan(input_enc):
    s1 = list(input_enc)
    dekripsi = ""
    for i in range(0, len(input_enc), 2):
        if s1[i] == " ":
            dekripsi += "  "
            i += 1
        elif s1[i] == ",":
            dekripsi += ", "
            i += 1
        elif s1[i] == ".":
            dekripsi += ". "
            i += 1
        elif s1[i] == "-":
            dekripsi += ""
            i += 1
        else:
            r = int(s1[i])
            c = int(s1[i + 1])
            ch = chr(((r - 1) * 5 + c + 96))
            if (ord(ch) - 96 >= 10):
                ch = chr(((r - 1) * 5 + c + 96 + 1))
                ch1 = str(ch)
                dekripsi = dekripsi + ch1
            else:
                ch1 = str(ch)
                dekripsi = dekripsi + ch1
    return dekripsi


dict = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def dekripsiPesan(key, pesan):
    return DekripsiVigenere(key, pesan)


def DekripsiVigenere(key, pesan):
    dekripsi_hasil = []
    keyIndex = 0
    key = key.upper()

    for char in pesan:
        num = dict.find(char.upper())
        if num != -1:
            num -= dict.find(key[keyIndex])
            num %= len(dict)

            dekripsi_hasil.append(dict[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            dekripsi_hasil.append(char)

    return ''.join(dekripsi_hasil)


input_enc = open('pesan_enkripsi.txt', 'r')
input_enc = input_enc.read()
DekripsiPesan(input_enc)
pesan = DekripsiPesan(input_enc)
password = str(input("Masukkan Password untuk melakukan dekripsi:"))

#INTERACTIVE
print("================================================================================")
print("Polybius : " + input_enc)
decrypt = dekripsiPesan(password, pesan)
print("Vigenere: " + pesan)
print("Pesan Dekripsi: " +  decrypt)
hasil_dekripsi = open("pesan_dekripsi.txt", "w")
hasil_dekripsi.write(decrypt)
print("================================================================================")
print("Hasil dekripsi tersimpan sebagai pesan_dekripsi.txt")
