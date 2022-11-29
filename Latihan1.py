#Latihan Modul Praktikum 5 (Rhendy Diki Nugraha)
kontak={'Ari':'081278888','Dina':'087677776'}
print('\n', kontak,'\n')

#Tampilkan kontaknya Ari
print('Menampilkan kontak Ari   : ',kontak['Ari'],'\n')

#Tambah kontak baru dengan nama Riko, nomor 087654544
kontak['Riko']='087654544'
print('Menambah kontak Riko     : ',kontak,'\n')

#Ubah kontak Dina dengan nomor baru 088999776
kontak['Dina']='088999778'
print('Mengubah kontak Dina     : ',kontak,'\n')

#Tampilkan semua Nama
print('Menampilkan semua Nama   :',kontak.keys(),'\n')
#Tampilkan semua Nomor
print('Menampilkan semua Nomor  :',kontak.values(),'\n')

#Tampilkan daftar Nama dan nomornya
print('Semua Kontak             :',kontak,'\n')

#Hapus kontak Dina
del kontak['Dina']
print('Menghapus kontak Dina    :',kontak)