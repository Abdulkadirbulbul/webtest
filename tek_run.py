import requests
import smtplib
import os
import requests
import json

#taratmak istediğiniz web siteleri dizi içerisine yazınız.
my_sites=["https://www.kadirbulbul.com"]

# MAİL GÖNDERME FONKSİYONU
def mail_gonder(metin):
    sender = "gonderen_mail"
    receiver = ['alici_mail1','alicimail_2']
    subject="Web Tester Hatalari"
    message = f"""\
    Subject: {subject}
    To: {receiver}
    From: {sender}

    Mesaj:\n Web Sitenizde Hata Meydana Geldi\n {metin.encode('ascii', 'ignore').decode('ascii')}"""

    # BURADA MAİL SUNUCUZUN BİLGİLERİ OLMASI GEREKİR.
    with smtplib.SMTP("mailsunucunuz.com", 0000) as server:
        server.login("usarneme", "password")
        server.sendmail(sender, receiver, message)
        print("mail gönderildi")

# DİSCORD BOTA MESAJ GÖNDERME FONKSİYONU
def discord_gonder(metin):
    webhook_url = "https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx" # Burada webhook URL'sini tanımlayın
    data = {"content": metin}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    print(response.text)

# SİTELERİ TARAMA İŞLEMİ
def status_code_result(siteler):
    metin=""
    for url in siteler:
        #herhani bir  zaman aşımı varsa bunuda eklemesi için try-cacth yapısı
        try:
            response = requests.get(url, timeout = 5)
            yanit=str(response.status_code)
        except requests.exceptions.Timeout:
            print("The request timed out")
            yanit="t"
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)
    
        deger=yanit[0]
        sonuc=""
        if(deger=="3"):
            metin=metin+ " "+yanit+" Yonlendirme Hatasi "+url+" urlsinden. \n"
        elif(deger=="t"):
            metin=metin+ " Zaman Asimi Hatasi (belirli bir sure cevap alinamadi) "+url+" urlsinden. \n"
        elif(deger=="2"):
            metin=metin+ " "+yanit+" Basarili  "+url+" urlsinden. \n"
            #metin=metin            < eğer sadece hatalarda mail göndermesini istiyorsanız burayu aktifleştirip bir üst  satırı devre dışı bırakız
        elif(deger=="4"):
            metin=metin+ " "+yanit+" istemci tarafli Hata "+url+" urlsinden.\n"
        elif(deger=="5"):
            metin=metin+ " "+yanit+" Sunucu tarafli Hata "+url+" urlsinden. \n"
        else:
            metin=metin+ " "+yanit+" Bilinmeyen Hata "+url+" urlsinden. \n"
        
    print(metin)
    #hata varsa yazdırma islemi
    if(len(metin)!=0):
        mail_gonder(metin)
        discord_gonder(metin)
status_code_result(my_sites)