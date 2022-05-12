import random
sayilar = "0123456789"
karakterler = "ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz"
semboller = "@#$%=:?./|~>*(),</][\\';}{>"
sifreprotatip = ""
olucak_karakterler = input("sifrenizde hangi karakterlerin olmasini istersiniz? \n A: sayilar \n B: semboller\n C: karakterler \n Birden fazla secenek seceilirsiniz")
if olucak_karakterler.upper() == "A":
    sifreprotatip = sayilar
elif olucak_karakterler.upper()=="B":
    sifreprotatip = semboller
elif olucak_karakterler.upper=="C":
    sifreprotatip = karakterler
elif olucak_karakterler.upper()=="AB":
    sifreprotatip = sayilar + semboller
elif olucak_karakterler.upper() == "AC":
    sifreprotatip = karakterler +sayilar
elif olucak_karakterler.upper() == "BC":
    sifreprotatip = karakterler+ semboller
elif olucak_karakterler.upper() == "ABC":
    sifreprotatip = karakterler+ semboller + sayilar


while 1:
    sifre_uzunlugu = int(input("Sifrenizin ne kadar uzun olmasini istiyorsunuz?"))
    sifre_sayisi = int(input("sizin icin kac tane sifre olusturalim"))
    for i in range(0,sifre_sayisi):
        sifre = ""
        for i in range(0,sifre_uzunlugu):
            sifre_karakterleri = random.choice(sifreprotatip)
            sifre = sifre + sifre_karakterleri
        print("buyurun yeni sifreniz  :", sifre )

