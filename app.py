#Hitung luas segitiga sederhana
def luas_segitiga():
    a = int (input("Masukkan alas segitiga : "))
    t = int (input("Masukkan tinggi segitiga : "))
    luas = a * t / 2
    print("luas segitiga adalah : ", luas)
    luas_segitiga()

    #Hitung luas persegi panjang
    def luas_persegi_panjang():
        p = int (input("Masukkan Panjang Persegi"))
        l = int (input("Masukkan Lebar persegi"))

        luas = p * l 
        print("Luas persegi adalah: ", luas)
        luas_persegi_panjang()