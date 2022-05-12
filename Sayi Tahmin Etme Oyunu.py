import random
i = 0
random_sayi = random.randint(0,100)
toplam_sayi = 0
    while i <=2:
        girilen = int(input("sayi giriniz :"))
        toplam_sayi = toplam_sayi + girilen
        i = i+1

    if toplam_sayi == random_sayi:
        print("kazandin")

    else:
        print("kaybettin tekrar dene")
