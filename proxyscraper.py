import requests

T = input("HTTP, SOCK4, SOCK5: ")
r = requests.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={T}&timeout=10000&country=all&ssl=all&anonymity=all")
f = open(T + ".txt", "w+")
f.write(r.text)
f.close()
