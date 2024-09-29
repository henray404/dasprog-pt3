x, y = input().split()  # masukkan ada berapa susunan segitiga
x = int(x)
y = y.lower()
if y == 'aku':  # if statement untuk cek bentuk segitiganya jika aku maka segitiga dari kiri dan jika kamu maka segitiga dari kanan

    for i in range(x):  # for loop untuk setiap line nya
        for j in range(i + 1):  # for loop untuk satu linenya
            if (j % 2 == 1):  # if statement jika ganjil maka u jika genap maka i
                print("u ", end="")
            else:
                print("i ", end="")

        print()

else:
    for i in range(1, x+1):  # for loop pertama untuk setiap barisnya dan menentukan nilai i

        # print space kosong agar bisa menaruh huruf i atau u di kanan
        print(" " * (x - i), end="")
        for j in range(i):  # for loop untuk peletakan huruf
            if j % 2 == 1:
                print("u", end="")
            else:
                print("i", end="")

        print()
