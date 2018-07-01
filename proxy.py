import requests
import os

def proxies():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
                             @@@
                             @@@
                              @@@                      P R O X Y
                              @@@
                      @@@@@@@@@@@@@@@@@@@@@@         C H E C K E R
                    @@@@@@@@@@@@@@@@@@@@@@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                @@@@@@@@ @@@@@@@@@@@@@@@@ @@@@@@@@
              @@@@@@@@@   @@@@@@@@@@@@@@   @@@@@@@@@
            @@@@@@@@@@     @@@@@@@@@@@@     @@@@@@@@@@
           @@@@@@@@@@       @@@@  @@@@       @@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@    @@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@        @@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
           @@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@
            @@@@@@@@  @@ @@ @@ @@ @@ @@ @@ @  @@@@@@@@
              @@@@@@@                        @@@@@@@
                @@@@@@  @@ @@ @@ @@ @@ @@ @ @@@@@@
                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    @@@@@@@@@@@@@@@@@@@@@@@@@@
                      @@@@@@@@@@@@@@@@@@@@@@
                      
""")
	file = input("Your proxies txt to check: ")
	proxies = []
	alive = []
	url = "http://www.mon-ip.com/"
	header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'}
	with open(file, "r") as p:
		proxies = [line.strip() for line in p]

	for proxy in proxies:
		start = 0
		end = proxy.index(":")
		st = proxy[start:end]
		e = proxy[end+1:]
		proxie = {"http":"{}:{}".format(st, e)}
		r = requests.get(url, headers=header, proxies=proxie)
		if st not in r.text:
			print("Testing...")
			print(proxie)
		else:
			print("Testing...")
			alive.append(proxy)
	for prox in alive:
		print("\nAlive list:")
		print(prox)


proxies()
