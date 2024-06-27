def pilih(operasi):
    x=float(input("Masukkan angka pertama :"))
    y=float(input("Masukkan angka kedua :"))

    if (operasi == '+'):
        hasil = x + y
    elif (operasi == '_'):
        if (x>y):
            hasil = x - y
        else:
            hasil = y - x
    elif (operasi == "*"):
        hasil = x * y
    else:
        if (y == 0):
            hasil = float (y/x)
        else:
            hasil = float (x/y)
    return hasil

def main():
    print("Silahkan pilih sala**h satu operasi berikut ini : ")
    print(" + : Menjumlahkan")
    print(" - : Mencari selisih")
    print(" * : Perkalian")
    print(" + : Pembagian")

    operasi = input ("Masukkan kode pilihan : ")
    output = pilih(operasi)
    print("Hasilnya = %f" % output)
    
main()
