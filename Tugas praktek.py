#menghitung luas dan keliling lingkaran dengan jari-jari
import math

#meminta input jari-jari
jari_jari =float(input("masukkan jari_jari: "))

#menghitung luas lingkaran
luas = (math.pi * jari_jari**2)

#menghitung keliling lingkaran
keliling = 2 * math.pi * jari_jari

#membulatkaan hasil ke bilangan
luas_bulat = print("luas lingkaran :", math.ceil(luas))
keliling_bulat = print("keliling lingkaran :", math.ceil(luas))



