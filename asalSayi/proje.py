#deger = int(input("Kaça kadar ki asal sayıları arıyorsunuz? : "))
#asal = []


#2 sayisindan başlayarak girilen degere kadar olan asal sayilar.
def asalSayi(deger, asal=[]):
    for i in range(2, deger):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            asal.append(i)

#burada asalSayi.txt adinda bir dosya oluşturuyoruz.
#dosya bulundugunuz klasorde olusacakdir.
    dosya = open('asalSayi.txt', 'w')

#asalSayısı.txt dosyasına yazı yazıyoruz
    dosya.write(f'0 - {deger} Arasinda Olan Asal Sayilar: ')

#dosya.write() str tipinda bir veri girebiliriz,bu yüzden asal degiskenini str() tipine dönüştürüyoruz.
    dosya.write(str(asal))

    return "\n0 - {} arasında toplam {} tane asal sayı vardır.".format(deger, len(asal))

print(asalSayi(20))