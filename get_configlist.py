import requests
import os
r=requests.get("https://raw.githubusercontent.com/TheSovietStorm/dotswag/master/.swagconf")  #Edit this Link to your swagconf
swagconf=open(os.getenv("HOME")+"/.swagconf",'w')
for i in r.text:
    swagconf.write(i)
swagconf.close()
