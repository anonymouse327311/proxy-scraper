import requests

T = input("HTTP, SOCK4, SOCK5: ")

if T == "HTTP":
	r = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
	f= open("https.txt", "w+")
	f.write(r.text)
	f.close()

if T == "SOCK4":
	r = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all')
	f= open("sock4.txt", "w+")
	f.write(r.text)
	f.close()

if T == "SOCK5":
	r = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all')
	f= open("sock5.txt", "w+")
	f.write(r.text)
	f.close()