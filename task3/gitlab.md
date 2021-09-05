I have installed gitlab 11.4.7 locally on ubuntu, and in gitlab configuration file, set the external_url is the host's ip address.

I accessed the gitlab page from kali and created a user **ssharma**

![](/imgs/t3p8.png)

I found an [exploit](https://github.com/mohinparamasivam/GitLab-11.4.7-Authenticated-Remote-Code-Execution) on the internet.
I [modified](/task3/exp.py) that exploit and made it work with python3 and made some minor changes.

Run the exploit as shown in the picture. Use option 1 and after run the script again with option 2.

![](/imgs/newone.png)

The script will ask to start a http server on port 80.

![](/imgs/t3p10.png)

It will download a file called shell.py into the folder and use it to exploit.
Now, run the script again with option 2.

Start a netcat listener on port specified in the script and run the script.

![](/imgs/t3p11.png)

A connection on netcat with a shell will be seen.

![](/imgs/t3p12.png)

