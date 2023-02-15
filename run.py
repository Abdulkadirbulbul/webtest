try:
    import requests
    import smtplib
    import os
    import dotenv
    import requests
    import json
except ModuleNotFoundError as err:
    print(err)
    exit()

# .env dosyasını okuma işlemi
dotenv.load_dotenv()

# Mail bilgilerini değişkenlere atayalım.
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = os.getenv("SMTP_PORT")

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECIEVER_EMAILS = os.getenv("RECIEVER_EMAILS")

SUBJECT = os.getenv("SUBJECT")

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

MAIL_ENABLED = os.getenv("MAIL_ENABLED") == "True"
DISCORD_ENABLED = os.getenv("DISCORD_ENABLED") == "True"

# program calısırken farklı dizinlerde cakışma olmasın diye dizini çekiyorum.
# Örneğin bende C://Pythonda iken sizde E://Uygulamar// Pythonda olabilir , txt doyasını okuma işlemlerinde
# bize dosya bulunamadı hatası verebilir.
target = os.path.dirname(os.path.abspath(__file__))
dizin = target+os.sep

# Urlleri metin dosyasından bir diziye akatrma işlemi
dosya = open(dizin+"/siteler.txt", "r")
my_sites = []
for satir in dosya:
    my_sites.append(satir.strip("/\n"))
# print(my_sites)

# MAİL GÖNDERME FONKSİYONU

def mail_gonder(metin):
    sender = SENDER_EMAIL
    receiver = RECIEVER_EMAILS.split(",")
    subject = SUBJECT
    message = f"""\
    Subject: {subject}
    To: {receiver}
    From: {sender}

    Mesaj:\n Web Sitenizde Hata Meydana Geldi\n {metin.encode('ascii', 'ignore').decode('ascii')}"""

    # BURADA MAİL SUNUCUZUN BİLGİLERİ OLMASI GEREKİR.
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(sender, receiver, message)
            print("mail gönderildi")
    except Exception as e:
        print(e)
        print("mail gönderilemedi")

# DİSCORD BOTA MESAJ GÖNDERME FONKSİYONU


def discord_gonder(metin):
    # Burada webhook URL'sini tanımlayın
    try:
        webhook_url = DISCORD_WEBHOOK_URL
        data = {"content": metin}
        headers = {"Content-Type": "application/json"}
        response = requests.post(
        webhook_url, data=json.dumps(data), headers=headers)
        print(response.text)
    except Exception as e:
        print(e)

# SİTELERİ TARAMA İŞLEMİ

def status_code_result(siteler):
    metin = ""
    for url in siteler:
        # herhani bir  zaman aşımı varsa bunuda eklemesi için try-cacth yapısı
        try:
            response = requests.get(url, timeout=5)
            yanit = str(response.status_code)
        except requests.exceptions.Timeout:
            print("The request timed out")
            yanit = "t"
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)

        deger = yanit[0]
        sonuc = ""
        if (deger == "3"):
            metin = metin + " "+yanit+" Yonlendirme Hatasi "+url+" urlsinden. \n"
        elif (deger == "t"):
            metin = metin + \
                " Zaman Asimi Hatasi (belirli bir sure cevap alinamadi) " + \
                url+" urlsinden. \n"
        elif (deger == "2"):
            metin = metin + " "+yanit+" Basarili  "+url+" urlsinden. \n"
            # metin=metin            < eğer sadece hatalarda mail göndermesini istiyorsanız burayu aktifleştirip bir üst  satırı devre dışı bırakız
        elif (deger == "4"):
            metin = metin + " "+yanit+" istemci tarafli Hata "+url+" urlsinden.\n"
        elif (deger == "5"):
            metin = metin + " "+yanit+" Sunucu tarafli Hata "+url+" urlsinden. \n"
        else:
            metin = metin + " "+yanit+" Bilinmeyen Hata "+url+" urlsinden. \n"

    print(metin)
    # hata varsa yazdırma islemi
    if (len(metin) != 0):
        if (MAIL_ENABLED):
            mail_gonder(metin)
        
        if (DISCORD_ENABLED):
            discord_gonder(metin)


status_code_result(my_sites)
