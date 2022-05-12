print("Gelir Gider Idare Programi")
i = 0
Aylar = ["Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Haziran", "Agustos", "Eylul", "Ekim", "Kasim", "Aralik"]
Mutfak_Giderleri = []
Elektrik_Faturasi = []
Kirtasiye_Masrafi = []
for i in range(len(Aylar)):
    M = input("Lutfen " +Aylar[i]+ " ayinin Mutfak Giderini Yazin:" )
    print("Sisteme kaydedildi...")
    E = input("Lutfen " +Aylar[i]+ " ayinin Elektrik giderini Yazin: ")
    print("Sisteme kaydedildi...")
    K = input("Lutfen " +Aylar[i]+ " ayinin Kirtasiye Giderini Yazin: ")
    print("Sisteme kaydedildi...")
    Mutfak_Giderleri.append(M)
    Elektrik_Faturasi.append(E)
    Kirtasiye_Masrafi.append(K)
    i=+1
while 1==1:
    istenilen_ay = int(input("Lutfen kacinci ayi gormek istediginizi girin (orn: Ocak=1, Subat=2)"))
    y = istenilen_ay-1
    istenilen_masraf = input("Lutfen " +Aylar[y]+ " ayinin hangi masrafini gormek istiyorsunuz? (mutfak,elektrik,kirtasiye) " )
    if istenilen_masraf.capitalize() == "Mutfak":
            print(Aylar[y]," ayinin Mutfak Masrafi", Mutfak_Giderleri[0] )
    elif istenilen_masraf.capitalize() == "Elektrik":
            print(Aylar[y], " ayinin elektrik Masrafi", Elektrik_Faturasi[0])
    elif istenilen_masraf.capitalize() == "Kirtasiye":
        print(Aylar[y], " ayinin Kirtasiye Masrafi", Kirtasiye_Masrafi[0])
    else:
            print("Devam edilirken hata yaptiniz lutfen kelimeleri dogru giriniz... (mutfak,elektrik,kirtasiye)")