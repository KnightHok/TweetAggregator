import tempfile
import requests
from datetime import datetime

def download_temp_media(dir, url):
    response = requests.get(url, stream=True)
    filename = url.split("/")[-1]
    if response.ok:
        f = open(f'{dir}\\{filename}', 'wb')
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)
        return f 

if __name__ == "__main__" :
    now = datetime.now()
    
    print(now)