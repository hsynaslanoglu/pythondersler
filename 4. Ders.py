KullanıcıAdı = "Ahmet"
KullanıcıAraba = "Ford"
SigortaTarihi = "02.02.2022"

mail = "Sayın {2}, {0} marka arabanızın sigortası {1} tarihinde bitmiştir. En yakın zamanda {0} bayisine gelerek işlemlerinizi yapabilirsiniz."

print(mail.format(KullanıcıAraba,SigortaTarihi,KullanıcıAdı))

KullanıcıAdları = ["Ahmet","Mehmet","Cemal"]
KullanıcıArabaları = ["Ford","Reno","Volvo"]
SigortaTarihleri = ["Ocak","Şubat","Mart"]

for index in range(len(KullanıcıAdları)):
    print(mail.format(KullanıcıArabaları[index],SigortaTarihleri[index],KullanıcıAdları[index]))


print("----------------------------------------------------------------------------------------")

MüsteriAdı = "Yılmaz Vural"
FaturaTarihi = "Mayıs"
FaturaTutarı = 100

FaturaMail = "Sayın {0}, {1} ayına ait faturanız ekte bulunmaktadır. Toplam fatura tutarınız: {2}TRY."

print(FaturaMail.format(MüsteriAdı,FaturaTarihi,FaturaTutarı))

print("----------------------------------------------------------------------------------------")

MüsteriAdları = ["Yılmaz Vural","Ersun Yanal","İsmail Kartal","Aykut Kocaman"]
FaturaTarihi = "Mayıs"
FaturaTutarları = [120,250,100,70]

for t in range(len(MüsteriAdları)):
    print(FaturaMail.format(MüsteriAdları[t],FaturaTarihi,FaturaTutarları[t]))

print("******************************************************************************************")

print("Burası çok \"GÜZEL\" olmuş!\nAma bu taraf daha da güzel olmuş...")

print("----------------------------------------------------------------------------------------")

Tablo = "Müşteri Adı\tFatura Tarihi\tFatura Tutarı\nYılmaz Vural\tMayıs\t100TRY"
print(Tablo)


print("******************************************************************************************")

print(10 > 9)
print(10 < 9)

print("----------------------------------------------------------------------------------------")

if(10 > 9):
    print("Büyüktür")

if(10 < 9):
    print("Burası yazılmayacak")

a = 5
b = 6 
c = 7

if(c > b):
    print("C, B'den büyükmüş")
if(c > a):
    print("C, A'dan da büyükmüş")

print("----------------------------------------------------------------------------------------")

if(a > b):
    print("A, B'den büyükmüş")
else:
    print("A, B'den küçükmüş")

print("----------------------------------------------------------------------------------------")

if(a > b):
    print("A, B'den büyükmüş")
elif(a >= b):
    print("A, B'ye eşitmiş")
else:
    print("A, B'den küçükmüş")

print("******************************************************************************************")

TeknikDirektörler = ["Yılmaz Vural","Ersun Yanal","İsmail Kartal","Aykut Kocaman"]
ŞimdikiTD = "İsmail Kartal"

for td in TeknikDirektörler:
    if(td == ŞimdikiTD):
        print(td + " şimdiki teknik direktör")
    else:
        print(td + " şimdiki teknik direktör değil")

print("----------------------------------------------------------------------------------------")

TeknikDirektörler = ["Yılmaz Vural","Ersun Yanal","İsmail Kartal","Aykut Kocaman"]
ŞimdikiTD = "İsmail Kartal"

for i in range(len(TeknikDirektörler)):
    if(TeknikDirektörler[i] == ŞimdikiTD):
        print(TeknikDirektörler[i] + " şimdiki teknik direktör")
    else:
        print(TeknikDirektörler[i] + " şimdiki teknik direktör değil")