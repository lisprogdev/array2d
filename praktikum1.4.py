class Buku:
    def __init__(self, kode, judul, pengarang, penerbit):
        self.kode = kode
        self.judul = judul
        self.pengarang = pengarang
        self.penerbit = penerbit

    def display(self):
        print("%s | %30s | %15s | %15s |" % (self.kode, self.judul,
                                             self.pengarang, self.penerbit))
def main():
    buku1 = Buku("123", "Algoritma pemrograman", "suarga", "Andi Offest")
    buku2 = Buku("234", "Pemrograman python", "Abd .kadir", "pelita pub")
    buku3 = Buku("345", "Struktur Data Python", "karl sianipar", "maxwell pub")
    print("Daftar Buku :")
    buku1.display()
    buku2.display()
    buku3.display()
main()
