print("Liskania Aprilia (312210383)")
print("=================================")

kontak={'Ari':'081267888','Dina':'087677776'}
#Tampilkan Kontaknya Ari
print(kontak['Ari'])
#Tambah kontak baru
kontak['Riko'] = '087654544'
#Ubah kontak dina dengan nomor baru
kontak['Dina'] = '088999776'
#Tampilan semua Nama
list(kontak.keys())
#Tampilan semua Nomor
list(kontak.values())
for i in kontak.items():
    print('{0:>10} | {1} '.format(i[0],i[1]))
kontak.pop('Dina')
print('menghapus kontak Dina')
for a in kontak.items():
    print('{0:>10} | {1} |'.format(a[0],a[1]))