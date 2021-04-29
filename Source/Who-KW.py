#
# This Is Free Tool By Soud Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os
	import json
	import requests
	from os import system
	system("title " + "Soud Was Here - @8Y - Soud#5866")
	import colorama
	from colorama import Fore
	colorama.init(autoreset=True)

except Exception as m:
    print("Something Went Wrong\n")
    print(m)
    input()
    exit()
logo = f"""
{Fore.CYAN}         _______   __  {Fore.GREEN}_    _ _          ___     
{Fore.CYAN}   ____ |  _  \ \ / / {Fore.GREEN}| |  | | |        |__ \ 
{Fore.CYAN}  / __ \ \ V / \ V /  {Fore.GREEN}| |  | | |__   ___   ) |
{Fore.CYAN} / / _` |/ _ \  \ /   {Fore.GREEN}| |/\| | '_ \ / _ \ / / 
{Fore.CYAN}| | (_| | |_| | | |   {Fore.GREEN}\  /\  / | | | (_) |_|  
{Fore.CYAN} \ \__,_\_____/ \_/    {Fore.GREEN}\/  \/|_| |_|\___/(_)  
{Fore.CYAN}  \____/             
"""
print(logo)
print(f"{Fore.GREEN}### Only For Kuwaity Phone Number ###\n")
print(f"{Fore.RED}This Is Free Tool By Soud Alanzi And Not For Sale\n\n{Fore.RESET}{Fore.GREEN}Instagram: @8Y + @_agf\nDiscord: Soud#5866\n")
phone = input("Enter Target Phone (69696969): ")
url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyAeC2lKS48QOcdveXMOZSXlkpNoyQV6sT0"
head = {"Host":"securetoken.googleapis.com","Content-Type":"application/json","Accept":"*/*","X-Ios-Bundle-Identifier":"io.meetain.Mno","Connection":"keep-alive","X-Client-Version":"iOS/FirebaseSDK/6.9.1/FirebaseCore-iOS","User-Agent":"FirebaseAuth.iOS/6.9.1 io.meetain.Mno/2.10 iPhone/14.2.1 hw/iPhone13_3","Accept-Language":"en",'Accept-Encoding':'gzip, deflate, br'}
data = {"grantType":"refresh_token","refreshToken":"AOvuKvRqUy4Tb6tR_s2joZlBmhoOQt_P77BPpsuV-fNa7oBGEh36eOTb6qOYE-vf8ZZS59TOjaMP5CJFoTwb0_IAZp7iAuTTM3nhPWm89j5_5lrRmVpF-Slp5V-_pPQD9ntyX4BuweEIi3s2HQLZowa3D7kM4I-aT5kpuk8KmdRCmCIj_I83sFU"}
req = requests.post(url, json=data, headers=head).text
tok = json.loads(req)["access_token"]
url2 = "https://us-central1-mnobackend.cloudfunctions.net/authentication/search"
head2 = {'Host':'us-central1-mnobackend.cloudfunctions.net',"Content-Type":"application/json","User-Agent":"Mno/70 CFNetwork/1206 Darwin/20.1.0","Connection":"keep-alive","Accept":"*/*","Accept-Language":"en-us","Accept-Encoding":"gzip, deflate, br",'Authorization':f'Bearer {tok}'}
data2 = {"acceptPolicy":"true","DeviceInfo":" isPhone","permission":"false","VersionIOS":"2.10","Number":phone}
req2 = requests.post(url2, json=data2, headers=head2)
if "Access denied" in req2.text:
	print(f"{Fore.RED}No Name Found For {phone}")
elif "Number doesn't exist" in req2.text:
	print(f"{Fore.RED}Name Not Found For {phone}")
elif 'status":200':
	namee = json.loads(req2.text)["Names"]
	print(f"{Fore.GREEN}Found Name: {namee}")		
input("Press 'Enter' To Close..")
exit()
