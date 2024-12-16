menu = {
    "Fried Chicken"   :15000,
    "pizza"           :20000,
    "burger"          :30000,
    "jasmine tea"     :12000,
    "milk tea"        :15000,
}
print("=================== Daftar Menu ===================")
for i in menu:
    print("Daftar Menu : ", i,"\t Harga : ",menu[i])
print("Pembelian diatas Rp100.000,- mendapatkan diskon 15%")
print("===================================================")
beli = input("pilih menu : ")
jumlah = int(input("jumlah pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar
print("=================== Detail Pembayaran ===================")
print("Menu yang dipesan        : ",beli)
print("jumlah yang dipesan      : ",jumlah)
print("Total Biaya              : ",bayar)
print("Total yang harus dibayar : ",total)