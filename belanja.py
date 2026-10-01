print("=== PROGRAM BELANJA ===")

harga = int(input("Masukkan harga barang: Rp"))
jumlah = int(input("Masukkan jumlah barang: "))
diskon = int(input("Masukkan diskon (%): "))

total = harga * jumlah
potongan = total * diskon / 100
total_bayar = total - potongan

print("Total harga: Rp", total)
print("Potongan diskon: Rp", potongan)
print("Total yang harus dibayar: Rp", total_bayar)