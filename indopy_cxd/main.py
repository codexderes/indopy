#####################################
# Progam: IndoPy                    #
# Version: 1.0.0                    #
# Author: Toms Droid                #
# Git: github.com/codexderes        #
# Website: https://codexderes.com   #
#####################################

# Membuat Class Templating Kalkulator
class Kalkulator:

    def penjumlahan(self,a,b):
        return a + b

    def pengurangan(self,a,b):
        return a - b
    
    def perkalian(self,a,b):
        return a * b

    def pembagian(self,a,b):
        return a / b

    def pembagian_bulat(self,a,b):
        return a // b
    
    def pembagian_sisa_bagi(self,a,b):
        return a % b

    def perpangkatan(self,a,b):
        return a ** b

# Membuat Class Templating Bangun Datar
class Bangun_Datar:

    def belah_ketupat(self, diameter_1, diameter_2, sisi):
        luas = (diameter_1*diameter_2)/2
        keliling = 4 * sisi
        return "Luas Belah-Ketupat: ", luas, "\nKeliling Belah-Ketupat: ", keliling
    
    def jajar_genjang(self, panjang, lebar, tinggi):
        luas = lebar*tinggi
        keliling = (2*panjang) + (2*lebar)
        return "Luas Jajar-Genjang: ", luas, "\nKeliling Jajar-Genjang: ", keliling

    def layang_layang(self, panjang, lebar, diameter_1, diameter_2):
        luas = (diameter_1*diameter_2)/2
        keliling = (2*panjang) + (2*lebar)
        return "Luas Layang-layang: ", luas, "\nKeliling Layang-layang: ", keliling

    def lingkaran(self, jari_jari):
        luas = (3.14*jari_jari)**2
        keliling = 2*3.14*jari_jari
        return "Luas Lingkaran: ", luas, "\nKeliling Lingkaran: ", keliling

    def persegi(self, sisi):
        luas = sisi * sisi
        keliling = 4*sisi
        return "Luas Persegi: ", luas, "\nKeliling Persegi: ", keliling

    def persegi_panjang(self, panjang, lebar):
        luas = panjang * lebar
        keliling =(2*panjang)+(2*lebar)
        return "Luas Persegi Panjang: ", luas, "\nKeliling Persegi Panjang: ", keliling

    def segitiga(self, alas, tinggi, lebar):
        luas = (alas*tinggi)//2
        keliling = alas+tinggi+lebar
        return "Luas Segitiga: ", luas, "\nKeliling Segitiga: ", keliling
    
    def trapesium(self, sisi_1, sisi_2, sisi_3, tinggi):
        luas = (sisi_1+sisi_2) * tinggi // 2
        keliling = sisi_1 + sisi_2 + sisi_3 + tinggi
        return "Luas Trapesium: ", luas, "\nKeliling Trapesium: ", keliling