import os

pathVar = ""

while(1):
    print("1 - Select iso\n2 - Install on usb\n3 - Quit")
    menu = input("Chose option: ")
    if(menu == "1"):
        path = input("Give path of iso(ex: /home/user/iso/galaxy.iso): ")
        pathVar = path
        print("Ok!")
    if(menu == "2"):
        if(pathVar == ""):
            print("Please give path of iso")
        else:
            usb = input("Usb drive: ")
            os.system("sudo sudo dd if=" + path + " of=" + usb + " && sync")
    if(menu == "3"):
        break;
