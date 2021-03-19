#list nama teman
teman = ['Efa', 'Erysa', 'Ayu', 'Rengga', 'Hafizh', 'Memed', 'Cita', 'Zafira', 'Diva', 'Salma' ]

#print indeks ke 4,6,dan 7
print("teman[4]:", teman[4])
print("teman[6:-2]:", teman[6:-2])

#remove list 3,5,9
teman.remove('Rengga')
teman.remove('Memed')
teman.remove('Salma')

#insert list 3,5,9
teman.insert(3,'Sekar')
teman.insert(5, 'Rana')
teman.insert(9, 'Yuku')
print(teman)

#menambahkan 2 teman
teman.extend(['Gea', 'Dea'])

#melakukan perulangan pada list
x = 0
for y in range (0,12):
    print(teman[x])
    x = x + 1

#menampilkan panjang list
print(len(teman))