# Versi 1
print(4 * (1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9) - (1 / 11)))
print(4 * (1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9) - (1 / 11) + (1 / 13) - (1 / 15)))

# Versi 2
total_dalam_kurung = 0
tanda = 1
penyebut = 1

for i in range (1, 9):
  total_dalam_kurung += tanda * (1 / penyebut)
  if i == 6 or i == 8:
    hasil_akhir = 4 * total_dalam_kurung
    print(hasil_akhir)
  tanda *= -1
  penyebut += 2
  
