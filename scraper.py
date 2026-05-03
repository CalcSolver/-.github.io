import os
import requests
import json

# This pulls your key from GitHub Secrets
PROXY_URL = os.getenv("PROXIFLY_URL")

def get_data():
    proxies = {
        "http": PROXY_URL,
        "https": PROXY_URL
    }
    
    try:
        # Replacing this with the site you want to scrape
        response = requests.get("https://httpbin.org/ip", proxies=proxies)
        data = response.json()
        
        # Save the result to a file that index.html can read
        with open("data.json", "w") as f:
            json.dump(data, f)
        print("Data updated successfully!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_data()
