import requests, json, colorama, termcolor
from ctypes import windll as dll

dll.kernel32.SetConsoleTitleW("IG | GiveMeCensor")
colorama.init()

class instagram:
    def __init__(self, username):
        self.target = username
    
    def GetCSRF(self):
        return requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", headers={
            "Cookie": "ig_cb=2; ig_did=6E0BD177-F4A6-4794-BB6F-F7BFACA2312B; mid=X7Gm_gALAAHpgUNXbRAazQhhXeCL",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
        }).cookies['csrftoken']

    def PasswordReset(self):
        CSRF_used = self.GetCSRF()
        http_response = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", headers={
            "X-CSRFToken": CSRF_used,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0",
            "Cookie": f"ig_cb=2; csrftoken={CSRF_used}",
        }, data={
            "email_or_username": self.target,
            "recaptcha_challenge_field": None,
        })

        json_message = http_response.json()["message"]

        print(termcolor.colored("Server-Response: " + (type(json_message)==type([]) and json_message[0] or json_message), http_response.status_code != 200 and "red" or "green"))

while True:
    instagram(input("IG-Username: ")).PasswordReset()