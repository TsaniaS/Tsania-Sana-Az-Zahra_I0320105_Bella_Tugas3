#Membuat Dictionary
dict = {'Nama' : 'Tsania',
        'Hobi' : ['Berenang', 'Menonton film', 'Bersepeda'],
        'Sosmed' : [
            'Instagram : Tsaniazhr',
            'Facebook   : Tsania uhuy',
            'Line       : tsaniaok'],
        'Lagu kesukaan' : ['Bertaut', 'Sudah', 'Yours'],
        'Makanan Favorit' : ['Bakso', 'Batagor', 'Sate']}

#mengubah salah satu hobi
dict['Hobi'][1] = ('Memasak')

#mengubah salah satu sosial media
dict['Sosmed'] = [
            'Instagram : Tsaniazhr',
            'Facebook  : Tsania uhuy',
            'Twitter   : apahayo']

#menghapus 2 makanan favorit
del dict['Makanan Favorit'][0:2]

#menambahkan satu hobi
dict['Hobi'].append('Melukis')

#menampilkan semua dict
print(dict)

