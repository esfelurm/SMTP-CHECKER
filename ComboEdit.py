m = input("Address Combo : ")
host = input("Enter the desired domain : ")
port = input("PORT : ")
with open('COMBONEW','w') as p:
    for mk in m:
        mk = mk.strip().replace(':','|')
        p.write(f"{host}|{port}|{mk}\n")
m.close()
