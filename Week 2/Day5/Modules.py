import requests
import time

def measure_webpage_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    if response.status_code == 200:
        load_time = end_time - start_time
        return load_time
    else:
        return None