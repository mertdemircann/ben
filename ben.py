#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from os import system as s

import os

os.system("pip install requests")

os.system("apt-get update")

os.system("apt-get upgrade")

os.system("apt-get install curl")
 
os.system("apt-get install python")

os.system("apt-get install figlet")

os.system("clear")

os.system("figlet KAYA - SMS GONDERME  ARACI")

banner = """
>Coder By KAYA
|> İstediginiz telefon numarasına her gun 1 defa mesaj atma hakkınız vardır!
|> Mesajınızdaki karakter sayısı 70'i geçmemelidir.
|> Telefon numarasını doğru girmezseniz hata vericektir.
|> Çalıştığını onaylamak için kendinizde deneyebilirsiniz.
|> Arkadaşlar doğru girdiğiniz halde hata veriyorsa 2. defa tekrar deneyin hata verse bile çalışacaktır.
|> telegram: @hackzafiyetleri
|> instagram: @kaya.root
"""

print(banner)

sor = input("Telefon numarası Örn: 905385408493 >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajınız Gönderilsinmi?[y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hata yaptın knk :D")