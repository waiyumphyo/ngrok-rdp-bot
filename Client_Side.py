import time, requests, subprocess

gist_raw_url = "https://gist.githubusercontent.com/waiyumphyo/a241e4914694ac11c0e8d9a83edf3bfd/raw/98ff3f6eb31ed08078f45c73613c40e0a8117420/ngrok_url.txt"
last_url = ""

while True:
    try:
        ngrok_url = requests.get(gist_raw_url).text.strip()

        if ngrok_url != last_url:
            print(f"New Ngrok URL: {ngrok_url}")
            last_url = ngrok_url
            subprocess.call('taskkill /IM mstsc.exe /F', shell=True)
            rdp_command = f"mstsc /v:{ngrok_url.replace('tcp://', '')}"
            subprocess.Popen(rdp_command, shell=True)
        
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(60)
