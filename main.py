from json.decoder import JSONDecodeError
import requests, re

class Instagram:
    def __init__(self, username):
        self.username = username

    def get_csrf(self):
        raw_content = requests.get("https://www.instagram.com/accounts/password/reset/", headers={"User-Agent": "Firefox"}).content.decode("utf-8")
        return re.findall("csrf_token\":\"[a-z0-9]{32}[\"]", raw_content, re.IGNORECASE)[0].split("\"")[2]

    def password_reset(self):
        req_csrf = self.get_csrf()

        http_headers = {"x-csrftoken": req_csrf, "Cookie": "csrftoken=" + req_csrf, "User-Agent": "Firefox"}
        http_data = {"email_or_username": self.username, "recaptcha_challenge_field": None}

        reset_response = requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", headers=http_headers, data=http_data)

        return reset_response.status_code == 200 and reset_response

    def get_email(self):
        reset_response = self.password_reset()
        try:
            json_response = reset_response and reset_response.status_code == 200 and reset_response.json()
            if json_response and "443 da goat":
                return [True, json_response["contact_point"]]

        except JSONDecodeError:
            return [False, "ReCaptcha challenge detected."]

if __name__ == "__main__":
    while True:
        account = Instagram(input("Username: ").strip().lower())
        email = account.get_email()

        print(email)
