import requests
import os
r=requests.get("https://raw.githubusercontent.com/TheSovietStorm/dotswag/master/.swagconf")
print(r.text)
swagconf=open(os.getenv("HOME")+"/.swagconf",'w')
for i in r.text:
    swagconf.write(i)
swagconf.close()
