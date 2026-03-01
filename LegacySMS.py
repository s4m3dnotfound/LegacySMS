from colorama import Fore, Style
from time import sleep
from os import system
from sms_api import SendSms
import threading

# --- Başlangıç Bilgilendirme Ekranı ---
system("cls||clear")
print(Fore.LIGHTGREEN_EX + """                   
**************************************************
*               LegacySMS v2 - 2026              *
*      Bu program tamamen eğitim amaçlıdır.      *
*      Tüm sorumluluklar kullanıcıya aittir.     *
*    Program 10 saniye sonra başlayacaktır...    *
**************************************************
""" + Style.RESET_ALL)

# 5 saniyelik geri sayım
for i in range(10, 0, -1):
    print(Fore.LIGHTGREEN_EX + f"\rBaşlıyor: {i} saniye ", end="")
    sleep(1)
print("\n")

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

# Bu Tool https://github.com/s4m3dnotfound/LegacySMS Adresine Aittir...
            
while 1:
    system("cls||clear")
    
    # ASCII yeşil logo
    print(Fore.LIGHTGREEN_EX + r"""
     _                                ____  __  __ ____    ____   ___ ____   __   
    | |    ___  __ _  __ _  ___ _   _/ ___||  \/  / ___|  |___ \ / _ \___ \ / /_  
    | |   / _ \/ _` |/ _` |/ __| | | \___ \| |\/| \___ \    __) | | | |__) | '_ \ 
    | |__|  __/ (_| | (_| | (__| |_| |___) | |  | |___) |  / __/| |_| / __/| (_) |
    |_____\___|\__, |\__,_|\___|\__, |____/|_|  |_|____/  |_____|\___/_____|\___/ 
               |___/            |___/                                             
""" + Style.RESET_ALL)
    
    # Alt metin, tek satır, renkler ayrı
    print(
        f"{Fore.LIGHTGREEN_EX}UYARI: Tamamen Eğitim Amaçlıdır.{Style.RESET_ALL}    "
        f"{Fore.LIGHTBLUE_EX}Geliştirici: {Style.RESET_ALL}s4m3dnotfound    "
        f"{Fore.LIGHTRED_EX}Güncel Sürüm:{Style.RESET_ALL} LegacySMS v2"
    )
    
    print()  
    
    try:
        menu = (input(Fore.LIGHTWHITE_EX + " 1- SMS Gönder\n\n 2- Çıkış\n\n" + Fore.LIGHTGREEN_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı işlem. Lütfen Tekrar dene.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTWHITE_EX + "SMS'lerin gönderileceği numarayı yazınız(başına '0' eklemeden): "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTWHITE_EX + "Numarayı Yazmadan Neden 'enter' Tuşuna Bastın Mal Mısın?: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Kafana Sıçayım O Zaman.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Geçersiz telefon numarası girdiniz. Lütfen tekrar dene.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTWHITE_EX + "yazdığın numarayı onaylamak için 'enter' tuşuna bas: "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Sadece 'enter' Tuşuns Basman Gerek.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTWHITE_EX + f"Kaç adet SMS göndermek istiyorsun? [sonsuz göndermek için 'enter'e bas.]: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı işlem. Lütfen Tekrar dene.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTWHITE_EX + "SMS'ler kaç saniye aralıkla gönderilsin? [Aralıksız göndermek için '0' yaz]: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı işlem. Lütfen Tekrar dene.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                while sms.adet < kere:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if attribute.startswith('__') == False:
                                if sms.adet == kere:
                                    break
                                exec("sms."+attribute+"()")
                                sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nAna ekrana dönmek için 'Enter' tuşuna bas")
        input()
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break

#Bu Tool https://github.com/s4m3dnotfound/LegacySMS Adresine Aittir...
