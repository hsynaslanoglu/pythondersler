sayı= 11
while(True):
    sayı = sayı-2
    #print("if den önce "+str(sayı))
    if(sayı<0):
        break
    #print("if den sonra "+str(sayı))

def my_function():
    print("----------fonksiyonu içi-------------")

my_function()
my_function()
my_function()
my_function()


def faktoriyel(sayı):
    x = 1

    for i in range(sayı): 
        i = i+1
        x = x*i

    return x


print(faktoriyel(15))
print(faktoriyel(5))
print(faktoriyel(1))
print(faktoriyel(0))

hesap = faktoriyel(4)
hesap2 = faktoriyel(6)

print(hesap+hesap2)

KullanıcıAdları = ["Ahmet","Mehmet","Cemal"]
KullanıcıArabaları = ["Ford","Reno","Volvo"]
SigortaTarihleri = ["Ocak","Şubat","Mart"]

TeknikDirektörler = ["Yılmaz Vural","Ersun Yanal","İsmail Kartal","Aykut Kocaman"]
print(TeknikDirektörler)


def arrayYazdır(dizi):
    for i in dizi:
        print(i)

arrayYazdır(TeknikDirektörler)
arrayYazdır(KullanıcıAdları)

def arrayYazdırv2(dizi):
    liste = ""
    for i in dizi:
        liste = liste+"\n"+i
    return liste

print(arrayYazdırv2(KullanıcıAdları))