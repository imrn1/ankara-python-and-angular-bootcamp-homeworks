
import random
import string
import pandas as pd

KELIME_LISTESI_DOSYASI = "tdk_sozcukler2.csv"
TÜRKÇE_ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'

def kelimeleri_yükle():
    
    print("Dosyadan kelime listesi okunuyor...")
    # dosyanın okunması
    dosya = pd.read_csv("tdk_sozcukler2.csv")
    # sözcüklerin küçük harfe çevrilmesi
    dosya['SOZCUKLER'] = dosya['SOZCUKLER'].str.lower() 
    # wordlist: list of strings
    kelime_listesi = dosya['SOZCUKLER'].tolist()
    print(f"{len(kelime_listesi)} kelimelik liste hazırlandı.")
    return kelime_listesi


def kelime_seç(kelime_listesi):
    return random.choice(kelime_listesi)



def kelime_tahmin_edildi_mi(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 
        tüm harflerin küçük olduğunu varsayar
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin 
    listesi; 
        tüm harflerin küçük olduğunu varsayar
    döndürdüğü: boolean, gizli_kelime'nin tüm harfleri 
    tahmin_edilen_harfler içindeyse True; 
        aksi takdirde False
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    for i in gizli_kelime:
        if i not in tahmin_edilen_harfler:
            return False
    else:
        return True

kelime_listesi = kelimeleri_yükle()


def tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler):
    '''
    gizli_kelime: dize, kullanıcının tahmin ettiği kelime; 

    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
    
    döndürdüğü: dize, harflerden oluşur, alt çizgiler (_) ve gizli_kelime 
    içindeki hangi harflerin şimdiye kadar tahmin edildiğini 
    temsil eden boşluklardan oluşur.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
   
    d="" 
    for i in gizli_kelime:
            if i in tahmin_edilen_harfler:
                d+=i+" "   
            else:
                d+="_ "
    return(d)


def uygun_harfleri_al(tahmin_edilen_harfler, alfabe = TÜRKÇE_ALFABE):
    '''
    tahmin_edilen_harfler: şimdiye kadar tahmin edilen harflerin listesi; 
       
    döndürdüğü: dize (harfler), Henüz tahmin edilmemiş harfleri temsil 
    eden harflerden oluşur.
    '''
    # alfabedeki harfleri alır
    # alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    d=""
    for i in alfabe:
        if i not in tahmin_edilen_harfler:
            d+=i+" "
    return d



def puan_hesapla(gizli_kelime,tahmin_edilen_harfler):
    return len(set(gizli_kelime))*len(uygun_harfleri_al(tahmin_edilen_harfler).split())



def insan_asmaca(gizli_kelime, alfabe = TÜRKÇE_ALFABE):
    print("\nİnsan Asmaca oyununa hoşgeldiniz!\n")
    print(f"gizli kelime {len(gizli_kelime)} harf içermektedir.")
    print(f"6 yanlış tahmin , 3 uyarı hakkın var")

    tahmin_edilen_harfler = []
    t=6
    u=0
    c=1
    
    while not kelime_tahmin_edildi_mi(gizli_kelime,tahmin_edilen_harfler):
        if t<=0 or u == 3:
            print("\nkaybettiniz.")
            print("gizli kelime:",gizli_kelime)
            break   
        
        # _ içeren kelimeyi ekranda gösterir
        print("\ngizli kelime: ",tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
    
        print(f"\n{c}. tahmininiz.\n{t} yanlış tahmin hakkınız | {u} uyarınız var")
        print(f"tahmin edilmeyen harfler:\n{uygun_harfleri_al(tahmin_edilen_harfler)}")
        
        while True:
            
            if t<=0 or u == 3:
                break
            
            x = input("harf girin: ").lower()
            if x.isalpha():
                if x not in tahmin_edilen_harfler:
                    tahmin_edilen_harfler.append(x)
                    if x not in gizli_kelime:
                        print(f"\n{x} harfi gizli kelime içinde yok.")
                        if x in ["a","e","ı","i","o","ö","u","ü"]:
                            t-=2
                        else:
                            t-=1    
                    break
                else:
                    print(f"\nOops, {x} harfini daha önce seçmiştiniz")
                    u+=1
                    break
            
            else:
                print("\nharf girmediniz!!!")
                u+=1
                if u!=3:
                    print("\ngizli kelime: ",tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                    print(f"\n{c}. tahmininiz.\n{t} yanlış tahmin hakkınız | {u} uyarınız var")
                    print(f"tahmin edilmeyen harfler:\n{uygun_harfleri_al(tahmin_edilen_harfler)}")
                else:
                    break
        c+=1
    
    if kelime_tahmin_edildi_mi(gizli_kelime,tahmin_edilen_harfler):
        print("\ntebrikler bildiniz!!!")     
        print("puanınız:",puan_hesapla(gizli_kelime,tahmin_edilen_harfler))

    

gizli_kelime = kelime_seç(kelime_listesi)
# print(gizli_kelime)
insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)

"""
bilinmeyen ünlü harfler 2 tahmin hakkını alır
bilinmeyen ünsüz harfler 1 tahmin hakkını alır
puanlama = gizli kellimedeki benzersiz harf sayısı * tahmin edilmeyen harf sayısı
"""



#%% 

def str_cevir(x):
    x = x.split()
    y = ""
    for i in x:
        y+=i
    return y

# str_cevir("k_ _ _ uz")

def boşluklarla_eşleştir(benim_kelimem, diğer_kelime):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    diğer_kelime: dize, normal Türkçe kelime
    döndürdüğü: boolean, 
    eğer benim_kelimem'in tüm gerçek harfleri diğer_kelime'nin karşılık gelen 
    harfleriyle eşleşiyorsa veya 
    harf özel sembol _ ise ve benim_kelimem ve diğer_kelime aynı 
    uzunluktaysa True; aksi takdirde False. 
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
   
    #  "k_ _ _ uz"  =>  k___uz  
    benim_kelimem = str_cevir(benim_kelimem) 
   
    if len(benim_kelimem) == len(diğer_kelime):
        i = 0
        for c in benim_kelimem:
            if c=="_":
                pass
            else:
                if c != diğer_kelime[i]:
                    return False
            i+=1
        else: 
            return True

    else:
        return False

""" sil sonra """
# boşluklarla_eşleştir("k_ _  _uz", "karpuz")
"""      """

# kelime_listesi = kelimeleri_yükle()

def olası_eşleşmeleri_göster(benim_kelimem):
    '''
    benim_kelimem: _ karakterli dize, geçerli gizli_kelime tahmini
    döndürdüğü: hiçbir şey, ancak kelime listesindeki my_word ile eşleşen her kelimeyi 
    yazdırmalıdır. Ekranda bir harf tahmin edildiğinde, o harfin gizli kelimede 
    geçtiği tüm pozisyonların ortaya çıktığını unutmayın. Bu nedenle, 
    gizli harf (_) zaten açığa çıkmış kelimedeki harflerden biri olamaz.
    '''
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    
    kelimeler = []
    # pattern = r""
    benim_kelimem = str_cevir(benim_kelimem)

    for kelime in kelime_listesi:
        if boşluklarla_eşleştir(benim_kelimem,kelime):
            kelimeler.append(kelime)
    print(kelimeler)


    
""" sil sonra """
# çıtlayan => kelime listesinde var 
# olası_eşleşmeleri_göster("ç_ t _ _ y _n")


"""   """  """   """




def ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE):
    
    # alfabedeki harfleri alır
    alfabe = TÜRKÇE_ALFABE
    # KODUNUZU BURAYA YAZIN VE "pass" İFADESİNİ SİLİN
    
    print("\nİnsan Asmaca oyununa hoşgeldiniz!\n")
    print(f"gizli kelime {len(gizli_kelime)} harf içermektedir.")
    print(f"6 yanlış tahmin , 3 uyarı hakkın var")

    tahmin_edilen_harfler = []
    t=6
    u=0
    c=1
    
    while not kelime_tahmin_edildi_mi(gizli_kelime,tahmin_edilen_harfler):
        if t<=0 or u == 3:
            print("\nkaybettiniz.")
            print("gizli kelime:",gizli_kelime)
            break   
        
        # _ içeren kelimeyi ekranda gösterir
        print("\ngizli kelime: ",tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
    
        print(f"\n{c}. tahmininiz.\n{t} yanlış tahmin hakkınız | {u} uyarınız var")
        print(f"tahmin edilmeyen harfler:\n{uygun_harfleri_al(tahmin_edilen_harfler)}")
        
        while True:
            
            if t<=0 or u == 3:
                break
            
            x = input("harf ya da tahmininizle eşleşen tüm kelimeleri görmek için * girin: ").lower()
            if x.isalpha():
                if x not in tahmin_edilen_harfler:
                    tahmin_edilen_harfler.append(x)
                    if x not in gizli_kelime:
                        print(f"\n{x} harfi gizli kelime içinde yok.")
                        if x in ["a","e","ı","i","o","ö","u","ü"]:
                            t-=2
                        else:
                            t-=1    
                    break
                else:
                    print(f"\nOops, {x} harfini daha önce seçmiştiniz")
                    u+=1
                    break
            elif x=='*':
                print("\nolası eşleşmeler:")
                olası_eşleşmeleri_göster(tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                break
            
            else:
                print("\nharf girmediniz!!!")
                u+=1
                if u!=3:
                    print("\ngizli kelime: ",tahmin_edilen_kelimeyi_al(gizli_kelime, tahmin_edilen_harfler))
                    print(f"\n{c}. tahmininiz.\n{t} yanlış tahmin hakkınız | {u} uyarınız var")
                    print(f"tahmin edilmeyen harfler:\n{uygun_harfleri_al(tahmin_edilen_harfler)}")
                else:
                    break
        c+=1
    
    if kelime_tahmin_edildi_mi(gizli_kelime,tahmin_edilen_harfler):
        print("\ntebrikler bildiniz!!!")     
        print("puanınız:",puan_hesapla(gizli_kelime,tahmin_edilen_harfler))


gizli_kelime = kelime_seç(kelime_listesi)
# print(gizli_kelime)
ipuçlarıyla_insan_asmaca(gizli_kelime, alfabe=TÜRKÇE_ALFABE)



