import goslate
gs = goslate.Goslate()
print('Pilih Bahasa :')
print('1.Indonesia Ke Inggris')
print('2.Inggris Ke Indonesia')
a = raw_input("Pilihan : ")
if a == '1'    : kata = raw_input("Masukan : ")
print(gs.translate(kata, 'id'))
if a == '2'    : kata = raw_input("Enter : ")
print(gs.translate(kata, 'en'))



