import random
maxi = 6

jumTebakan = 0
print('Hallo kawan, siapa nama anda?')
nama = input()
angka = random.randint(1, 20)

print('ok ' + nama + 'saya memikirkan satu angka antara 1 s/d 20')
while (jumTebakan < maxi):
    print('coba anda tebak,')
    tebak = input()
    tebak = int(tebak)
    jumTebakan = jumTebakan + 1
    if (tebak < angka):
        print('angka tersebut lebih besar dari ' + str(tebak))
    if (tebak > angka):
        print('angka tersebut lebih kecil dari ' + str(tebak))
    if (tebak == angka):
        break
        
if (tebak == angka):
        print ('Bagus, anda telah menebaknya dalam ' + str(jumTebakan)\
               +' langkah')
if (tebak != angka):
        print ('Maaf, anda tidak berhasil menebak angka ' + str(angka))
        
