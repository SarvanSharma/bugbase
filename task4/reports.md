**Report 1:**
<br>
<br>
Host header injection on  http://minet.co/
<br>
After following the steps provided in poc, I found that the issue exists and report is valid
It is valid because the change in host header is leading to redirection.

**Poc:**
<br>
Visited http://minet.co/ and intercepted the request

![](/imgs/pic1.png)
 
Sent that request to repeater and changed the host value from minet.co to hackerone.com

![](/imgs/pic2.png)
 
The response is 301 redirect and after following redirection, it was clear that it got redirected to hackerone
<br>

**CVSS Score:**

![](/imgs/pic3.png)

<br>
<br>
<br>
<br>

**Report 2:**
<br>
<br>
Clickjacking on https://minet.co/
<br>
After following the steps in poc, I found that this issue is valid.
<br>
<br>
**Poc:**
<br>
I used this clickjacking html script to check the clickjacking

![](/imgs/pic4.png)
 
![](/imgs/pic5.png)
																																																																										


**CVSS Score:**

![](/imgs/pic6.png)

<br>
<br>
<br>
<br>
 
**Report 3:**
<br>
<br>
No valid spf record found which leads to email spoofing
<br>
<br>
**Poc:**
<br>
Go to  https://www.kitterman.com/spf/validate.html and enter website name and click get spf record

![](/imgs/pic7.png)
<br>
<br>
You can see no valid spf record found
<br>
<br>
![](/imgs/pic8.png)

Which means, this domain can be used for email spoofing

Now go to https://emkei.cz/ and enter from email as any email with domain minet.co and enter all the details

![](/imgs/pic9.png)

You can see the mail received 
<br>
<br>
![](/imgs/pic10.png)

**CVSS Score:**

![](/imgs/pic11.png)
 
