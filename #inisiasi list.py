#inisiasi list
my_list = ["prodi TI",1,2,3,4,1,2]

#mengetahui panjang list
panjang_my_list = len(my_list)


#cetak list
print("my list:", my_list)
print("panjang list:",panjang_my_list)
print("panggil index ke 5:", my_list[5])

#tambah anggota di dalam list
my_list.append("keren")


#cetak list setelah input anggota baru
print("my_list setelah diinput nilai baru: ", my_list)


#cetak list setelah menghapus nilai 2 yang pertama
print("my_list setelah menghapus nilai 2: ", my_list)

#menghapus nilai 2 dalam list
my_list.remove(2)

#cetak list setelah menghapus nilai 2 yang pertama
print("my_list setelah menghapus nilai 2: ", my_list)

#menghapus index ke 1
del my_list[1]

#cetak list setelah menghapus index ke 1
print("my_list setelah menghapus index ke 1: ", my_list)


