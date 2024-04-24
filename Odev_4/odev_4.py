import sqlite3

def jaccard(metin1,metin2):
    küme1 = set(metin1)
    küme2 = set(metin2)

    kesisim = len(küme1.intersection(küme2))
    birlesim = len(küme1.union(küme2))

    benzerlikKatsayisi = kesisim / birlesim

    return benzerlikKatsayisi

baglan = sqlite3.connect("metinler.db") # Veritabanına bağlanıldı.

imlec = baglan.cursor() # İmleç oluşturuldu.

metin1 = input("Metin giriniz: ")
metin2 = input("Metin giriniz: ")

imlec.execute("CREATE TABLE IF NOT EXISTS metinler(metin TEXT)") # Tablo oluşturuldu.

imlec.execute("INSERT INTO metinler VALUES(?)",(metin1,)) # Metin1 değişkeni tabloya eklendi.
imlec.execute("INSERT INTO metinler VALUES(?)",(metin2,)) # Metin2 değişkeni tabloya eklendi.

baglan.commit() # Veritabanı güncellendi.

imlec.execute("SELECT * FROM metinler") # Sorgu yapıldı.

print(imlec.fetchall()) # Ekrana metinler bastırıldı.

print(f"Metinler arasındaki benzerlik oranı: {jaccard(metin1,metin2)}")

with open("benzerlik_durumu.txt","w") as file: # Dosya write modunda açıldı.
    file.write("Metinler arasındaki benzerlik oranı: {}".format(jaccard(metin1,metin2))) # Dosyaya yazdırıldı.

imlec.execute("DELETE FROM metinler") # Tablo temizlendi.

baglan.commit() # Veritabanı güncellendi.

baglan.close() # Bağlantı kesildi.