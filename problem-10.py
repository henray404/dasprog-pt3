
def move_word(C, K, teks):  # fungsi untuk memindahkan huruf atau word shifting
    result = ''  # mengdefine variavel result sebagai variabel string

    for char in teks:  # for loop untuk mengganti setiap hurufnya
        if char.isalpha():

            if char.isupper():  # mengecek apakah huruf kapital atau bukan
                ASCII = 65
            else:
                ASCII = 97

            if C == 1:  # menentukan apakah shifting maju atau mundur
                moved = chr((ord(char) - ASCII + K) %
                            26 + ASCII)  # kalkulasi huruf
            else:
                moved = chr((ord(char) - ASCII - K) % 26 + ASCII)
            result += moved  # hasilnya dimasukkan kedalam variabel result
        else:
            result += char  # jika bukan huruf maka hasilnya tetap sama

    return result  # hasil dari fungsi move_word


def input_result(cases):  # fungsi untuk perulangan jika kasus lebih dari satu
    result = []  # define variabel result sebagai list

    for kasus in cases:  # for loop untuk mengulang kasus
        C, K, teks = kasus
        result.append(move_word(C, K, teks))
    return result


# input berapa banyak kasus
T = int(input(" masukkan berapa banyak kasus: \n"))

cases = []  # define variabel adalah list

for i in range(T):  # for loop untuk input jika kasus lebih dari satu
    C, K = map(int, input(
        "masukkan huruf berpindah maju atau mundur, (1) jika maju dan (2) jika mundur. masukkan juga huruf berpindah berapa kali: \n").split())
    teks = input("masukkan huruf: \n")
    cases.append((C, K, teks))

results = input_result(cases)  # hasil dari shifting huruf

for i in results:  # for loop print agar hasil keluar di beda line
    print(i + "\n")
