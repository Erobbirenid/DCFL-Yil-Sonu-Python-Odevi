print("Meslege Yatkinlik programi")
saglik_alaninda_meslekler_erkek = ["tıp doktoru","diş hekimi","eczacı","psikolog","hemşire","veteriner ","biyolog ","fizyoterapist ","kimyager ","ebe ","hastabakıcı ","","","","","","",""]
kisisel_bio= []
A = "A"
cinsiyet = input("1.Soru-Cinsiyetiniz nedir?\n A:Kadin \n B:Erkek")
if cinsiyet.upper() == A:
    kisisel_bio.append("A")
else:
    kisisel_bio.append("B")

vakit_harcama = input("2.Soru- Boş zamanlarınızi ne ile geciriyorsunuz?\n A: Film izlemek, müzik dinlemek, karaoke yapmak, tiyatroya gitmek yada resim yapmak.\n B: elektronikleri tamir etmek, çicek/bitki yetiştirmek , spor yapmak mesela futbol, koşu, bisiklet sürme")
if vakit_harcama.upper() == A:
    kisisel_bio.append("A")
else:
    kisisel_bio.append("B")

maas = input("3.Soru-Eğer Turkiye kosullarinda msasinizi kullanmak isteseniz asagidakilerden hangilerine harcarsiniz?\n A: En sevdigim filme/futbol macina en onden bilet alma \n B: TEMA , LOSEV ,UNICEF gibi vakif ve kuruluslara")
if maas.upper() == A:
    kisisel_bio.append("A")
else:
    kisisel_bio.append("B")

calisma_saati = input("4.Soru-Hayal mesleginiz sizce hangi saatlerde olmalidir? \n A: Belirli saatleri olan (ornegin Sabah 9 aksam 4 gibi) \n B: Esnek zamanlar sunan bir is ")
if calisma_saati.upper() == A:
    kisisel_bio.append("A")
else:
    kisisel_bio.append("B")

calisma_yontemi = input("5.Soru-Asagidakilerden hangi yontem sizin icin daha efektidir?\n A: KEndi bildigmi ve tek basima kendime guvenerek yapma \nB: Hedefin pesinden ekibimle birlikte kosturma")
if calisma_yontemi.upper() == A:
    kisisel_bio.append("A")
else:
    kisisel_bio.append("B")

if kisisel_bio == "AAAAA" or "BAAAA" or "AAABA" or "BAABA":
    print("Gelecekteki meslegin Aktorluk Garsonluk Kasiyerlik Sinema Yonetmeni Sarkici olabilir.")
elif kisisel_bio == "ABBAA" or "ABBBA" or "BBBBB":
    print("Gelecekteki meslegin Doktorluk muhendis marangoz mimar olabilir.")
else:
    print("Gelecekteki meslegini tam olarak belirleyemedik... ozur dileriz")

