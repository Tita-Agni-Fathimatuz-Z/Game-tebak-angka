import random

print(input("masukan nama anda: "))
angka_random = random.randint(1, 25)
kesempatan = 5
while kesempatan > 0:
    tebakan = int(input("masukan tebakan anda (1-25): "))
   
    if tebakan < angka_random:
        print("kurang besarr")  
    elif tebakan > angka_random:
        print("kurang kecill")
    else:
        print("SELAMATT, tebakan anda benarrr....")
    kesempatan -= 1
    print("kesempatan: ", kesempatan)

if kesempatan == 0:
    print("MAAFF.... KESEMPATAN ANDA SUDAH HABIS")