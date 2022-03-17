sayı = 5
i = 1
bosluksayısı = int(sayı/2)

for satır in range(sayı):

    BastakiBosluk = bosluksayısı*" "
    AradakiBosluk = i*" "

    if(satır > 0):
        if(satır < int(sayı/2)):
            i = i+2
        else:
            i = i-2
            
    if(satır < int(sayı/2)):
        bosluksayısı = bosluksayısı-1
    else:
        bosluksayısı = bosluksayısı+1

    if(satır != sayı-1 and satır != 0):
        print(BastakiBosluk+"*"+AradakiBosluk+"*")
    else:
        print(BastakiBosluk+"*")

    