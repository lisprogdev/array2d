def main():
    print("Input Data : ")
    nama = input("Nama : ")
    alamat = input("Alamat : ")
    umur = int(input("Umur : "))
    jenkel = input("Jenis kelamin: ")
    institusi = input("Masukkan institusi-nya: ")
    print ()
    print("Output Data : ")
    print("Nama: ", nama)
    print("Alamat : ", alamat)
    thlahir = 2022 - umur
    print("Lahir tahun : ", thlahir)
    print("Jeniskelamin :",jenkel)
    print("Seorang %s di instituti %s" % (jenkel, institusi))
    
main()
