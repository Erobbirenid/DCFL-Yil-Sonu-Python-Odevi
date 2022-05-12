import random
import time
toplam_puan = 0
SORU_SAYISI = 10

tumsorular = [
    "Bir yere gitmeyi ifade ederken cümlenin başında kullanılan söz hangisidir? \n A: Ver elini \n B: Kir Dizini \n C: Sik Disini \n D: Yum Gozunu" ,
    "Bugunden sonra gelecek ilk gunun anlamina gelen kelimenin yazilisi nedir? \n A: Yaǧrin \n B: Yarin \n C: Yaarin \n D: Yaǧarin",
    "Ince kesilmis doner icin kullanilan tabir asagidakilerden hangisidir? \n A: Cam \n B: Cerceve \n C: Kaǧit \n D: Yaprak",
    "Hangisi, Hollywood filmlerinin mahkeme sahnelerinde sıklıkla duyulan ifadelerdendir? \n A: Sakin ol şampiyon! \n B: Bir cisim yaklaşıyor! \n C:Senin sorunun ne! \n D:İtiraz ediyorum!",
    "Masalların klişe giriş cümlesinde develer ne iş yapar?\n A: Berber \n B: Hallac \n C: Tellal\n D: Nalbant",
    """"Baygın baygın bakmak" hangi durum için kullanılan bir sözdür? \n A: Saskinlik \n B: Tembellik \n C:Hayranlik \nD: Tembellik""",
    """Dışaridan yiyecek ve içecek getirmek yasaktır" uyarısıyla karşılaşıyorsanız muhtemelen neredesinizdir?\n A: Beyazsaray \n Ogrenci Evi \nSanayi Sitesi \n Sinema """,
    "Öğretmen, öğrencilerinden çiçek olmalarını istediğinde öğrenciler hangisini yapıp ses çıkarmadan dururlar? \n A:Kollarini Goguste Baglayip\nB:Ayaga Kalkip \nC:Ellerini Havaya Kaldirip\nD: Tek Ayak Ustunde Durup",
    """Yemekten sonra "Eline sağlık" diyen kişiye verilen cevapta, afiyet bal ______olsun denir. Boslukta hangisi olsun denilir? \n A:Lokum \nB:Surup \nC:Kaymak \nD: Seker """,
    "Bir olayı kutlamak veya eğlenmek için düzenlenen ziyafete ne ad verilir?\n A: Panayir \n B: Solen \nC:Resmi Gecit \nD:Anma Toreni ",
    """"Aynı, bildiğiniz gibi" cevabını aldıysanız sorduğunuz soru hangisidir?\n A:Isminiz nedir? \n B:Nasilsiniz \n C: Ne alirdiniz\n D:Nerelisiniz""",
    """Bir şeyin miktarından bahsederken "hatırı sayılır" denildiğinde nasıl bir miktar ifade edilir?\n A:Eksik \n B:Cok \n C: Cesitli\n D: Oratalma""",
    "Halk arasında kullanılan bir söze göre, kötü komşu insanı ne sahibi yapar?\n A: Karavan  \n B:Dusman \n C: Dert\n D:Ev",
    """Izlemekte olduğunuz programda "Haydi çocuklar, 78 milyon tek yürek" gibi ifadeler kullanılıyorsa, muhtemelen hangisini izliyorsunuzdur?\n A:Evlilk Programi \n B: Futbok Musabakasi \nC:Cizgi Film \n D:Belgesel""",
    "Körling, hokey ve paten hangi zeminde yapılan sporlardır?\n A:Buz \n B:Tahta \n C:Cimen \n D: Kum",
    "4'ün 4 katının 4'te birine 4 eklerseniz hangi sayıyı bulursunuz? \n A:4 \n B:5 \n C:8 \n D:20 ",
    "      497 x 33 \nişleminin sonucu kaçtır?\n A:18.324 \n B:19.676\n C:17.893 \n D:16.401",
    "Ölçüsü 80 derece olan açı nasıl açıdır?\n A: Dik  \n B: Dogru \n C:Dar \n D: Tam",
    "Yarısının 2 katı 122 olan sayının 18 fazlası kaçtır? \n A:79 \n B: 130 \n C:140 \n D:262 ",
    "Hangi sayı, hem 2’nin hem 3’ün hem de 5’in katıdır?\n A:15  \n B:66 \n C:60  \n D:80 ",
]
tumcevaplar = ["A","B","D","D","C","C","D","A","D","B","B","B","D","B","A","C","D","C","C","C"]

ad = input('adinizi ogrenebilir miyiz?').capitalize()

for i in range(SORU_SAYISI):

   x = random.randint(0, len(tumsorular)-1)
   print("sayin ",ad,"sorumuz su: \n " ,tumsorular[x])
   y = input("cevabiniz: \n").upper()
   if y == tumcevaplar[x]:
       toplam_puan += 10
       print("dogru"," toplam puaniniz",toplam_puan,"oldu.")
   else:
       print(toplam_puan)
       print("yanlis"," toplam puaniniz",toplam_puan)
   tumsorular.pop(x)
   tumcevaplar.pop(x)
if toplam_puan ==100:
    print("Tebrikler! Butun sorulari dogru bildin, 10 sorudan hepsini dogru tamamladin")
else:
    print("Tebrikler ama daha iyi olabilirdi, 10 sorudan olusan testin",int(toplam_puan/10),"tanesini dogru yapabildiniz.")
