#Ders 2

x = "Hello World" #string - text
print(type(x))

x = 5 #integer - sayı
print(type(x))

x = 20.5 #float - kesirli sayı
print(type(x))

x = ["ahmet","mehmet","ali"] #array/list - dizi
print(type(x))

x = False #boolean - doğru/yanlış
print(type(x))

#Kesirli Sayıya Çevirme
x = float(1)
print(x)

x = float("3")
print(x)

#Tam Sayıya Çevirme
x = int(1)
print(x)

x = int("2")
print(x)

x = int(3.9)
print(x)

#Metine Çevirme
x = str(1)
print(type(x))
print(x)

x = str(1.2)
print(type(x))
print(x)


metin = """Daha oyun süre oynayın. Göz Koruyucu Mod, uzun süre oyun oynadığınızda 
mavi ışığı gözleri rahatlatacak şekilde en aza indirir. Titreşimsiz Teknoloji, 
daha az göz yorgunluğu ile daha uzun oyun odaklanabilmeniz için yorucu ve dikkat 
dağıtıcı ekran oyun sürekli olarak ortadan kaldırır."""
print(metin)


x = "Merhaba Dünya"
print(x[8:])

print(x.upper())

print(x.replace("a","e"))

print( len(metin.split("oyun")) - 1 )