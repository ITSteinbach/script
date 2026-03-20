import requests

urls = ["https://google.com", "https://github.com", "https://deine-website.de"]

def check_sites():
    print(f"{'URL':<30} | {'Status':<10}")
    print("-" * 45)
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status = "ONLINE" if response.status_code == 200 else f"Fehler {response.status_code}"
        except:
            status = "OFFLINE"
        print(f"{url:<30} | {status:<10}")

if __name__ == "__main__":
    check_sites()