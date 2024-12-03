print(" __________________________")
print("|                          |")
print("| PROGRAM KASIR SEDERHANA  |")
print("||")
print("| : PILIH MENU MAKANAN :   |")
print("|                          |")
print("| Ayam Bakar      Rp.15000 |")
print("| Ayam Geprek     Rp.15000 |")
print("| Nasi Rendang    Rp.20000 |")
print("| Nasi Pecel      Rp.10000 |")
print("| Soto Ayam       Rp.12000 |")
print("||")

nomer_makanan = int(input("Pilih (1/2/3/4/5) : "))
jml_porsi = int(input("Berapa porsi : "))

if nomer_makanan == 1:
    total_makanan = jml_porsi * 15000
    print(f"Ayam Bakar {jml_porsi} Porsi : Rp.{total_makanan}")
    makanan = "Ayam Bakar"
elif nomer_makanan == 2:
    total_makanan = jml_porsi * 15000
    print(f"Ayam Geprek {jml_porsi} Porsi : Rp.{total_makanan}")
    makanan = "Ayam Geprek"
elif nomer_makanan == 3:
    total_makanan = jml_porsi * 20000
    print(f"Nasi Rendang {jml_porsi} Porsi : Rp.{total_makanan}")
    makanan = "Nasi Rendang"
elif nomer_makanan == 4:
    total_makanan = jml_porsi * 10000
    print(f"Nasi Pecel {jml_porsi} Porsi : Rp.{total_makanan}")
    makanan = "Nasi Pecel"
elif nomer_makanan == 5:
    total_makanan = jml_porsi * 12000
    print(f"Soto Ayam {jml_porsi} Porsi : Rp.{total_makanan}")
    makanan = "Soto Ayam"
else:
    print("Menu tidak terdaftar!")