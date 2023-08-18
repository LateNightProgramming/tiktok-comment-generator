from random import randint, choice, getrandbits

def main():
    string = ""
    p1 = ['bro is','his fade be','he be lookin']
    p2 = [' vovacious',' zesty',' sus',' a silly billy',' carmunkulous']
    p2_1 = [' vovacious',' zesty',' sus',' carmunkulous']
    p3 = ['🔥','💀','🥶','🥵','❗','😂','😬']
    selection = choice(p1)
    if bool(getrandbits(1)):
        string+="ayo "
    string+=selection
    if selection in ("his fade be","he be lookin"):
        string+=choice(p2_1)
    else:
        string+=choice(p2)
    selection = bool(getrandbits(1))
    if selection:
        string+=choice([" in ohio", " only in ohio", " in oklahoma", " only in oklahoma"])
    for i in range(randint(2,15)):
        string+=choice(p3)
    print("comment:",string)
    while True:
        inp = input("do you wish to restart: ").lower()
        if inp == "yes":
            print("restarting")
            main()
            break
        elif inp == "no":
            print("quitting")
            exit()
        else:
            print("invalid response")
            
main()
