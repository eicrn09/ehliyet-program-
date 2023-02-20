isim=input("isim: ")
soyIsim=input("soyisim: ")
yas=int(input("yas: "))
egitimDurumu=input("egitim durumu: ")
if (yas>=18) and (yas<=60):
    if (egitimDurumu=='lise') or (egitimDurumu=='universite'):
       print("Sayin",isim,soyIsim,"ehliyet alabilirsiniz.")
    else:
         print("sayin",isim,soyIsim,"ehliyet alabilmek icin en az lise mezunu olmaniz lazim.")
else:
    print("Sayin",isim,soyIsim,"ehliyet alabilmek icin yasinizin 18 ila 60 arasinda olmasi gerek.")