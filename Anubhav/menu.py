import os
import getpass

os.system("tput setaf 3")
print("\t\t\t----------")


passwd = getpass.getpass("Enter ur password : ")

if passwd != "Anubhav@8126":
    print("Password Incorrect...")
    exit()

r = input("Where you want to run this menu ? (local/remote) : ")
print(r)

while True:
    os.system("clear")
    print("""
    \n
    Press 1 : to install Docker
    Press 2 : to Launch CentOS
    Press 3 : to Pull Docker Images
    Press 4 : to install Server in Docker
    Press 5 : to exit
    """)

    ch = input("Enter ur Choice : ")
    print (ch)

    if r == "local":
        if int(ch) == 1:
            os.system("dnf install docker-ce --nobest")

        elif int(ch) == 2:
                image = input("Enter the Name OS which you want to Launch :")
                os.system("docker run -it --name anubhav -p 9091:80 {}".format(image))

        elif int(ch) == 3:
            os.system("docker ps")

        elif int(ch) == 4:
            os.system("yum install httpd")

        elif int(ch) == 5:
            exit()
        else:
            print("not supported")

    elif r == "remote":
        ip = input("Enter Your ip : ")
        print(ip)
        if int(ch) == 1:
            os.system("ssh {} dnf install docker-ce --nobest".format(ip))

        elif int(ch) == 2:
            os.system("ssh {} docker run -it --name webos -p 9091:80 {}".format(ip))

        elif int(ch) == 3:
            os.system("ssh {} docker ps".format(ip))

        elif int(ch) == 4:
            os.system("ssh {} yum install httpd".format(ip))

        elif int(ch) == 5:
            exit()
        else:
            print("not supported")
    else:
        print("not supported login...")

    input("\n plz. enter to continue...")
