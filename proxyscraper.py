#Python3 
#This tool is made by https://github.com/webvuln 

import requests
import time 

def main():
  T = input("HTTP, SOCK4, SOCK5: ")
  print("Fetching your proxys")
  r = requests.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol={T}&timeout=10000&country=all&ssl=all&anonymity=all")
  f = open(T + ".txt", "w+")
  f.write(r.text)
  f.close()
  print("Done getting your proxys check the .txt out")
  time.sleep(5.5)
