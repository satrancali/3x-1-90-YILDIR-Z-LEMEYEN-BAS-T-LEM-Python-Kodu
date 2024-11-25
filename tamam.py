def cift_sayi_ise_ikiye_bol(sayi):
    return sayi / 2


def tek_sayi_ise_uc_ile_carp_ve_bir_ekle(sayi):
    return (sayi * 3 ) + 1


def sayi_tek_mi_cift_mi_kontrol_et_ona_gore_islem_yap(sayi):
    if sayi % 2 == 0:
        sonuc = cift_sayi_ise_ikiye_bol(sayi)
    elif sayi % 2 == 1:
        sonuc = tek_sayi_ise_uc_ile_carp_ve_bir_ekle(sayi)
    else:
        print(f"Bir yerlerde sıkıntı var, sayı {sayi}")
        exit()

    #print(sayi)
    return sonuc


def tek_tek_sayilari_arttir():
    baslangic_sayisi = 1
    while True:
        q = baslangic_sayisi
        for a in range(1000):
            q = sayi_tek_mi_cift_mi_kontrol_et_ona_gore_islem_yap(q)
            if q == 4:
                print(f"DEGIL {baslangic_sayisi}")
                break
            if a == 999:
                print(f"BULUNDU {baslangic_sayisi}")
                exit()

        baslangic_sayisi  = baslangic_sayisi + 2
        print(baslangic_sayisi)
tek_tek_sayilari_arttir()


