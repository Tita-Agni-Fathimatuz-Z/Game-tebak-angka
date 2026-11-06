def kalkulator():
    while True:
        print("=== KALKULATOR ===")
        print("1. Penjumlahan (a + b)")
        print("2. Pengurangan (a - b)")
        print("3. Pembagian (a / b)")
        print("4. Perkalian (a * b)")
        print("5. Keluar")

        pilihan = input("Opsi yang dipilih: ")

        if pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator!")
            break

        elif pilihan == "1":
            a = float(input("a = "))
            b = float(input("b = "))
            hasil = a + b
            print("a + b =", hasil)

        elif pilihan == "2":
            a = float(input("a = "))
            b = float(input("b = "))
            hasil = a - b
            print("a - b =", hasil)

        elif pilihan == "3":
            a = float(input("a = "))
            b = float(input("b = "))

            if b == 0:
                print("Tidak bisa dibagi dengan 0!")
            else:
                hasil = a / b
                print("a / b =", hasil)

        elif pilihan == "4":
            a = float(input("a = "))
            b = float(input("b = "))
            hasil = a * b
            print("a * b =", hasil)

        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")


kalkulator()