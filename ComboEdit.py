m = input("Address Combo : ")
m = open(m,'r')
host = input("Enter the desired domain : ")
port = input("PORT : ")
with open('/sdcard/COMBONEW.txt','w') as p:
    for mk in m:
        mk = mk.strip().replace(':','|')
        p.write(f"{host}|{port}|{mk}\n")
