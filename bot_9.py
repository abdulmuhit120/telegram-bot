# 30-may-2026 12:34 PM
import requests
import json
import base64
import time

class Uid_to_info:
    def __init__(self):
        with open("bot_token.txt", "r") as bot_token:
            token = bot_token.read()
        self.token = base64.b64decode(token).decode("utf-8")
        
        
        with open("id_info_api.txt", "r") as id_info_api:
            read_api = id_info_api.read()
        self.decode_api = base64.b64decode(read_api).decode("utf-8")
        
        
    def get_json(self):
        get_url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        update_id = 0
        while True:
            try:
                params = {"offset" : update_id}
                get_bot = requests.get(get_url, params=params).json()
                for bot_response in get_bot.get("result",[]):
                    update_id = bot_response["update_id"] + 1
                    self.chat_id = bot_response["message"]["from"]["id"]
                    self.text = bot_response["message"].get("text")
                    self.info_api()
                    self.post_url()
                    
            except:
                print("try agen")
                
                
    def info_api(self):
        params = {"uid" : self.text}
        get_info_api = requests.get(self.decode_api, params=params).json()
        if self.text == "/start":
            all_text = "হাই আপনাকে Free Fire Uid To Info বটে স্বাগতম\n\nfree fire গেমের UID দিন"
        
        elif self.text.isdigit() and len(self.text) >= 8 and len(self.text) <= 12:
            
            if get_info_api.get("status") == "success" : 
                self.nickname = get_info_api["player_info"]["nickname"]
                self.uid = get_info_api["player_info"]["uid"]
                self.level = get_info_api["player_info"]["level"]
                self.likes = get_info_api["player_info"]["likes"]
                self.region = get_info_api["player_info"]["region"]
                b = "\n"
                
                all_text = (
                f"├├𝙽𝙸𝙺𝙽𝙰𝙼𝙴  {self.nickname}{b}"
                f"├├𝚄𝙸𝙳            {self.uid}{b}"
                f"├├𝙻𝙴𝚅𝙴𝙻       {self.level}{b}"
                f"├├𝙻𝙸𝙺𝙴         {self.likes}{b}"
                f"├├𝚁𝙴𝙶𝙸𝙾𝙽     {self.region}")
            else:
                all_text = "​এই বটটি শুধুমাত্র BD, ID, SG এবং MENA সার্ভার সাপোর্ট করে।"
                
        self.txt = all_text
    
    def post_url(self):
        post_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        
        payload = {"chat_id" : self.chat_id, "text" : self.txt}
        
        post_api = requests.post(post_url, json=payload)
        print(post_api)
            
            
        
        
                
            
    

a = Uid_to_info()
a.get_json()