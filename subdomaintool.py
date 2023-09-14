import sys
import requests
import pyfiglet

xdxd = pyfiglet.figlet_format("sub DOMAINER", font = "slant")
print(xdxd) 
ydyd = pyfiglet.figlet_format("Coded w/ <3 By - @p474nj4y", font = "digital" )
print(ydyd)

sub_list = open("wordlists.txt").read()
subs = sub_list.splitlines()

for sub in subs:
    sub_domain = f"http://{sub}.{sys.argv[1]}" #it will form URL in the format of "http://sub.domain.com"
    
    try:
        requests.get(sub_domain)

    except requests.ConnectionError:
        pass

    else:
        print("subdomain found > ",sub_domain)





