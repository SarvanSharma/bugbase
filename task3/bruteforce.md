Upon accessing the site, I got this prompt to enter password.


![](/imgs/t3p1.png)


I entered a letter a and intercepted it through burp

![](/imgs/t3p2.png)
 
I sent this request to intruder and started bruteforcing.

![](/imgs/t3p3.png)
 
I used a bruteforcing list containing a to z in lower and upper case with all special charecters.
After that I started the attack.
I sorted the intruder attack result using response received.

![](/imgs/t3p4.png)
 
The first letter is a because it took more time than other characters.
For the next character, I added another letter and started the attack.

![](/imgs/t3p5.png)
  

After doing this for 20 characters, I was successfully able to retrieve the password.
**The password is enc0re{5hm0ll_fl4g}**

![](/imgs/t3p6.png)
 
After entering this into prompt, It shows as correct password.

![](/imgs/t3p7.png)
 
