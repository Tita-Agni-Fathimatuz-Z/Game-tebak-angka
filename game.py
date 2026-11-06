import random

angka_rahasia = random.randint(1, 25)
kesempatan = 5

print("=== GAME TEBAK ANGKA ===")
print("Tebak angka dari 1 sampai 25!")
print("Kamu punya 5 kesempatan.")

while kesempatan > 0:
    tebakan = int(input("Masukkan tebakan kamu: "))

    if tebakan == angka_rahasia:
        print("Selamat! Tebakan kamu benar!")
        break
    elif tebakan < angka_rahasia:
        print("Tebakan kamu terlalu kecil!")
    else:
        print("Tebakan kamu terlalu besar!")

    kesempatan -= 1
    print("Sisa kesempatan:", kesempatan)

if kesempatan == 0 and tebakan != angka_rahasia:
    print("Kesempatan habis!")
    print("Angka yang benar adalah:", angka_rahasia)