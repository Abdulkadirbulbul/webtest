# Web Site Test Uygulaması

Merhabalar bu uygulamamızın amacı web sitemizde olacak hataları **Mail kutumuza ve Discord Botumuza** ileterek anlık olarak discord sunucumuzda görüntülenmesidir.
Herhangi bir arayüze sahip değildir.
2 farklı çalışma dosyası vardır.
## tek_run.py 
Eğer url sayınız az ise ve **tek_run.py** dosyasının içerisinde bulunan **my_sites** adlı diziye eklemesi gerekir.
```python:
my_sites=["https://www.kadirbulbul.com"]
```
Eğer eliniz de bir çok url var ve bunları bir txt doyasında tutmak isterseniz o zaman siteler.txt doyasına web sitelerinizi ekleyebilirsiniz.

## Çalıştırmak için  (run.py)
 **Adım 1** 
> Sitelerinizi siteler.txt ekledikten  sonra run.py dosyasını açın.

**Adım 2**
```python:
# MAİL GÖNDERME FONKSİYONU
def  mail_gonder(metin):
sender = "gonderen_mail"
receiver = ['alici_mail1','alicimail_2']
subject="Web Tester Hatalari"
message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}
Mesaj:\n Web Sitenizde Hata Meydana Geldi\n  {metin.encode('ascii', 
'ignore').decode('ascii')}"""
 """BURADA MAİL SUNUCUZUN BİLGİLERİ OLMASI GEREKİR."""
with  smtplib.SMTP("mailsunucunuz.com", 0000) as  server:
server.login("usarneme", "password")
server.sendmail(sender, receiver, message)
print("mail gönderildi")
```
> Belirtilen kısımlara alıcı mail hesabı  , gönderici mail hesabı ve kendi mail sunucunuzun bilgilerini girmeniz  gerekir. Eğer yoksa fonskiyonu devre dışı bırakabilirsiniz.

**Adım 3**
```python:
# DİSCORD BOTA MESAJ GÖNDERME FONKSİYONU
def  discord_gonder(metin):
#Burada webhook URL'sini tanımlayın
webhook_url = "https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx"  
data = {"content": metin}
headers = {"Content-Type": "application/json"}
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
print(response.text)
```
> Burada ise sadece webhook_url yazan değişkene discord webhook urlnizi yazanız gerekir.

**Adım 4**
```python:
if(len(metin)!=0):
	mail_gonder(metin)
	discord_gonder(metin)
```
> Burada çıktıların hangilerinde göndereceğiniz kısımlar yazıyor. İstediğiniz kısmı deaktif/aktif yaptıkdan sonra kodunuzu çalıştırabilirsiniz. **İşte Bu Kadar Kolay :)**


## Sunucuda çalıştırmak için 
Eğer kodunuzu sunucuda her 10 dakika da bir çalıştırmak istiyorsanız bunun için Ubuntu sunucunuzun olması  ve içerisinde pythonun kurulu olması gerekir.
Eğer bu ikisi tamamsa yerinizi alın :)

**Adım 1** 

```sh: 
crontab -e
```
> yazıyoruz ve gelen ekran buna benzer  olmalıdır.

```sh: 
 Edit this file to introduce tasks to be run by cron.
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/

```

**Adım 2**
> En alt kısma bir komut satırı ekliyoruz.
```sh:
*/10 * * * * python3 /home/ubuntu/python/mailtest/run.py
```
> bunu yazıyoruz ve CTRL+X , sonrasında Y , en sonunda ENTER a basıyoruz.
> Buradaki amacımız kodumuzun her 10 dakika da bir çalışmasıdır.
> Sizler istediğiniz süreyi ayarlamak için https://crontab.guru/ sitesinden yardım  alıp üsteki kodda değişiklik yapabilirsiniz..

*Bundan sonra artık hep otonom olarak 10 dakikada bir wb sitelerinizi kontrol edip size bilgi verecektir.
 

 # Web Site Test Application (EN)

Hello, the purpose of this application is to display the errors on our website instantly on our discord server by forwarding them to our **Mail box and Discord Bot**.
It does not have any interface.
There are 2 different working files.
## single_run.py
If your url number is low and it should be added to the array named **my_sites** in the **single_run.py** file.
`` python:
my_sites=["https://www.kadirbulbul.com"]
```
If you have many urls and you want to keep them in a txt file, then you can add your websites to the sites.txt file.

## To run (run.py)
  **Step 1**
> After adding sites.txt to your sites, open the run.py file.

**Step 2**
`` python:
# SEND MAIL FUNCTION
def mail_gonder(text):
sender = "sender_mail"
receiver = ['recipient_mail1','receivermail_2']
subject="Web Tester Errors"
message = f"""\
Subject: {subject}
To: {receiver}
From: {sender}
Message:\n An Error Occurred on Your Website\n {metin.encode('ascii',
'ignore').decode('ascii')}"""
  """THERE SHOULD HAVE YOUR MAIL SERVER'S INFORMATION."""
with smtplib.SMTP("yourmailserver.com", 0000) as server:
server.login("usarneme", "password")
server.sendmail(sender, receiver, message)
print("mail sent")
```
> In the specified sections, you must enter the information of the recipient mail account, sender mail account and your own mail server. If not, you can disable the function.

**Step 3**

`` python:
# SEND MESSAGE FUNCTION TO DISCORD BOTA
def discord_gonder(text):
#Define webhook URL here
webhook_url = "https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx"
data = {"content": text}
headers = {"Content-Type": "application/json"}
response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
print(response.text)
```
> Here, you just need to write your discord webhook url to the variable that says webhook_url.

**Step 4**
`` python:
if(len(text)!=0):
mail_gonder(text)
discord_gonder(text)
```
> Here, the parts you will send are written in which of the printouts. You can run your code after you deactivate/activate the part you want. **It's That Easy :)**


## To run on server
If you want to run your code on the server every 10 minutes, you must have Ubuntu server and python installed in it.
If these two are ok, take your place :)
**Step 1**

``sh:
crontab -e
```
> and the screen should look like this.

``sh:
  Edit this file to introduce tasks to be run by cron.
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# For example, you can run a backup of all your user accounts
# at 5 a.m. every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/

```
**Step 2**
> Add a command line at the bottom.
``sh:
*/10 * * * * python3 /home/ubuntu/python/mailtest/run.py
```
> we write this and press CTRL+X , then Y , finally ENTER.
> Our goal here is for our code to run every 10 minutes.
> You can get help from https://crontab.guru/ and make changes in the code above to set the time you want.

*From now on, it will always autonomously check your web sites every 10 minutes and inform you.