text = "benim ismim Hüseyin"
a = text.split(" ")
print(a[2])
print(a[len(a)-1])

print(text[12:])
print(text[-7:])

ben = a[len(a)-1]

print(ben.upper())
print(ben.lower())

ben = " Hüseyin "
print("!"+ben+"!")
print("!"+ben.strip()+"!")

print("*"+ben.replace(" ","")+"*")


adet = 5
fiyat = 10.50
barkodNumarası = 981231341345
print(str(barkodNumarası)+" barkod numaralı"+" ve "+str(fiyat)+ " fiyattaki üründen "+ str(adet)+" adet istiyorum")

print("-------------------------------------------------------------------------------")
adetListesi = [5,2,3,22,10]
fiyatListesi = [5,1,30,2,99]
barkodNumarası = 981231341345

for index in range(len(adetListesi)):
    print(str(barkodNumarası)+" barkod numaralı"+" ve "+str(fiyatListesi[index])+ " fiyattaki üründen "+ str(adetListesi[index])+" adet istiyorum")
print("-------------------------------------------------------------------------------")


sipariş = " {2} barkod numaralı ve {0} fiyattaki üründen {1} adet istiyorum"

sipariş2 = sipariş.format(fiyat,adet,barkodNumarası)

print(sipariş2)