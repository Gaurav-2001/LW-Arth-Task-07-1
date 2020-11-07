import os
import getpass as gp

def SPartition(location):
    if location==1:
        #Create Static Partition in Local host
        os.system("tput setaf 2")
        print("""
                Enter the Name of the Harddisk:
                (To See the existing Harddisk in os press 2)
        """)
        os.system("tput setaf 7")
        hd=input()
        if choice=="2":
            os.system("fdisk -l")
            os.system("tput setaf 2")
            hd=input("Enter the Name of the Harddisk: ")
            os.system("tput setaf 7")
        os.system("fdisk {}".format(hd))
        os.system("tput setaf 2")
        fs=input("Enter the format type to be used: ")
        prt=input("Enter the partition name: ")
        os.system("tput setaf 7")
        os.system("mkfs.{} {}".format(fs,prt))
        os.system("tput setaf 2")
        print("""
                Folder to mount
                Press 1: To use a Precreated folder
                Press 2: To create a new floder
        """)
        os.system("tput setaf 7")
        choice=int(input())
        while True:
            if choice==1:
                os.system("tput setaf 2")
                folder=input("Enter the folder name: ")
                os.system("tput setaf 7")
                break
            elif choice==2:
                os.system("tput setaf 2")
                folder=input("Enter the folder name to be created: ")
                os.system("tput setaf 7")
                os.system("mkdir {}".format(folder))
                break
            else:
                print("Invalid choice Try again")
        os.system("mount {} {}".format(prt,folder))
    elif location==2:
        #Create Static Partition in remote host
        os.system("tput setaf 2")
        print("""
                Enter the Name of the Harddisk:
                (To See the existing Harddisk in os press 2)
        """)
        os.system("tput setaf 7")
        hd=input()
        if choice=="2":
            os.system("ssh {} fdisk -l".format(ip))
            os.system("tput setaf 2")
            hd=input("Enter the Name of the Harddisk: ")
            os.system("tput setaf 7")
        os.system("ssh {} fdisk {}".format(ip,hd))
        os.system("tput setaf 2")
        fs=input("Enter the format type to be used: ")
        prt=input("Enter the partition name: ")
        os.system("tput setaf 7")
        os.system("ssh {} mkfs.{} {}".format(ip,fs,prt))
        os.system("tput setaf 2")
        print("""
                Folder to mount
                Press 1: To use a Precreated folder
                Press 2: To create a new floder
        """)
        os.system("tput setaf 7")
        choice=int(input())
        while True:
            if choice==1:
                os.system("tput setaf 2")
                folder=input("Enter the folder name: ")
                os.system("tput setaf 7")
                break
            elif choice==2:
                os.system("tput setaf 2")
                folder=input("Enter the folder name to be created: ")
                os.system("tput setaf 7")
                os.system("ssh {} mkdir {}".format(ip,folder))
                break
            else:
                print("Invalid choice Try again")
        os.system("ssh {} mount {} {}".format(ip,prt,folder))

def LPartition(location):
    if location==1:
        #Create logical Partition in local host
        os.system("tput setaf 2")
        choice=input("""
                Do U want to created a new PV or use exesting PV:
                Press 1: Create New PV
                Press 2: Use Exesting PV
         """)
        os.system("tput setaf 7")
        if choice=="1":
            print("Creating the PV.... ")
            os.system("tput setaf 2")
            hd=input("""
                Enter the Name of the Harddisk:
                (To See the existing Harddisk in os press 2)
            """)
            os.system("tput setaf 7")
            if hd=="2":
                os.system("fdisk -l")
                os.system("tput setaf 2")
                hd=input("Enter the Name of the Harddisk: ")
                os.system("tput setaf 7")
            os.system("pvcreate {}".format(hd))
        elif choice=="2":
            os.system("tput setaf 2")
            hd=input("""
                Enter the Name of the PV to contribute:
                (To See the existing Harddisk in os press 2)
            """)
            os.system("tput setaf 7")
            if hd=="2":
                os.system("fdisk -l")
                os.system("tput setaf 2")
                hd=input("Enter the Name of the PV to contribute: ")
                os.system("tput setaf 7")
        print("Contribute the PV storage to VG")
        os.system("tput setaf 2")   
        choice=input("""
                Do u want to use Exesting VG or create new VG:
                Press 1: To use Exesting VG
                Press 2: To create new VG
        """)
        os.system("tput setaf 7")
        if choice=="1":
            os.system("tput setaf 2")
            VGname=input("""
                Enter the Exesting VG name:
                (To see names of existing VG Press 2)
            """)
            os.system("tput setaf 7")
            if VGname=="2":
                os.system("vgdisplay")
                os.system("tput setaf 2")
                VGname=input("Enter the Existing VG name: ")
                os.system("tput setaf 7")
        elif choice=="2":
            os.system("tput setaf 2")
            VGname=input("Enter the VG name: ")
            os.system("tput setaf 7")
            os.system("vgcreate {} {}".format(VGname,hd))
        os.system("tput setaf 2")
        LVname=input("Enter the LV name u want to create: ")
        LVsize=input("Enter the LV size u Want to create: ")
        os.system("tput setaf 7")
        os.system("lvcreate --size {}G --name {} {}".format(LVsize,LVname,VGname))
        os.system("tput setaf 2")
        fs=input("Enter the format type to be used: ")
        os.system("tput setaf 7")
        os.system("mkfs.{} /dev/{}/{}".format(fs,VGname,LVname))
        os.system("tput setaf 2")
        fold=input("""
                Folder to mount
                Press 1: To use a Precreated folder
                Press 2: To create a new floder
        """)
        os.system("tput setaf 7")
        if fold=="1":
            os.system("tput setaf 2")
            folder=input("Enter the Existing folder name: ")
            os.system("tput setaf 7")
        elif fold=="2":
            os.system("tput setaf 2")
            folder=input("Enter the folder name to be created to mount: ")
            os.system("tput setaf 7")
            os.system("mkdir {}".format(folder))
        os.system("mount /dev/{}/{} {}".format(VGname,LVname,folder))

    elif location==2:
        #Create logical Partition in remote host
        os.system("tput setaf 2")
        choice=input("""
                Do U want to created a new PV or use exesting PV:
                Press 1: Create New PV
                Press 2: Use Exesting PV
         """)
        os.system("tput setaf 7")
        if choice=="1":
            print("Creating the PV.... ")
            os.system("tput setaf 2")
            hd=input("""
                Enter the Name of the Harddisk:
                (To See the existing Harddisk in os press 2)
            """)
            os.system("tput setaf 7")
            if hd=="2":
                os.system("ssh {} fdisk -l".format(ip))
                os.system("tput setaf 2")
                hd=input("Enter the Name of the Harddisk: ")
                os.system("tput setaf 7")
            os.system("ssh {} pvcreate {}".format(ip,hd))
        elif choice=="2":
            os.system("tput setaf 2")
            hd=input("""
                Enter the Name of the PV to contribute:
                (To See the existing Harddisk in os press 2)
            """)
            os.system("tput setaf 7")
            if hd=="2":
                os.system("ssh {} fdisk -l".format(ip))
                os.system("tput setaf 2")
                hd=input("Enter the Name of the PV to contribute: ")
                os.system("tput setaf 7")
        print("Contribute the PV storage to VG")
        os.system("tput setaf 2")
        choice=input("""
                Do u want to use Exesting VG or create new VG:
                Press 1: To use Exesting VG
                Press 2: To create new VG
        """)
        os.system("tput setaf 7")
        if choice=="1":
            os.system("tput setaf 2")
            VGname=input("""
                Enter the Exesting VG name:
                (To see names of existing VG Press 2)
            """)
            os.system("tput setaf 7")
            if VGname=="2":
                os.system("ssh {} vgdisplay".format(ip))
                os.system("tput setaf 2")
                VGname=input("Enter the Existing VG name: ")
                os.system("tput setaf 7")
        elif choice=="2":
            os.system("tput setaf 2")
            VGname=input("Enter the VG name: ")
            os.system("tput setaf 7")
            os.system("ssh {} vgcreate {} {}".format(ip,VGname,hd))
        os.system("tput setaf 2")
        LVname=input("Enter the LV name u want to create: ")
        LVsize=input("Enter the LV size u Want to create: ")
        os.system("tput setaf 7")
        os.system("ssh {} lvcreate --size {}G --name {} {}".format(ip,LVsize,LVname,VGname))
        os.system("tput setaf 2")
        fs=input("Enter the format type to be used: ")
        os.system("tput setaf 7")
        os.system("ssh {} mkfs.{} /dev/{}/{}".format(ip,fs,VGname,LVname))
        os.system("tput setaf 2")
        fold=input("""
                Folder to mount
                Press 1: To use a Precreated folder
                Press 2: To create a new floder
        """)
        os.system("tput setaf 7")
        if fold=="1":
            os.system("tput setaf 2")
            folder=input("Enter the Existing folder name: ")
            os.system("tput setaf 7")
        elif fold=="2":
            os.system("tput setaf 2")
            folder=input("Enter the folder name to be created to mount: ")
            os.system("tput setaf 7")
            os.system("ssh {} mkdir {}".format(ip,folder))
        os.system("ssh {} mount /dev/{}/{} {}".format(ip,VGname,LVname,folder))

def hdfs_site(node,location):
    os.system("cp /arth-task/task7.1/dn/temp.xml /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \<configuration\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \<property\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \<name\>dfs.{}.dir\</name\> >> /arth-task/task7.1/dn/hdfs-site.xml".format(node))
    os.system("tput setaf 3")
    print("""
                Enter the {}node directory
                Press 1: To use a Precreated directory
                Press 2: To create a new directory
    """.format(node))
    os.system("tput setaf 7")
    choice=int(input())
    while True:
        if choice==1:
            os.system("tput setaf 3")
            folder=input("Enter the {}node directory name: ".format(node))
            os.system("tput setaf 7")
            break
        elif choice==2:
            os.system("tput setaf 3")
            folder=input("Enter the {}node directory to be created: ".format(node))
            os.system("tput setaf 7")
            if location==1:
                os.system("mkdir {}".format(folder))
            elif location==2:
                os.system("ssh {} mkdir {}".format(ip,folder))
            break
        else:
            print("Invalid choice Try again")
    os.system("echo \<value\>{}\</value\> >> /arth-task/task7.1/dn/hdfs-site.xml".format(folder))
    os.system("echo \</property\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    os.system("echo \</configuration\> >> /arth-task/task7.1/dn/hdfs-site.xml")
    if location==1:
        os.system("mv -f /arth-task/task7.1/dn/hdfs-site.xml /etc/hadoop/hdfs-site.xml")
    elif location==2:
        os.system("scp /arth-task/task7.1/dn/hdfs-site.xml {}:/etc/hadoop/hdfs-site.xml".format(ip))
        os.system("rm -f /arth-task/task7.1/dn/hdfs-site.xml")

def core_site(node,location):
    os.system("cp /arth-task/task7.1/dn/temp.xml /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \<configuration\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \<property\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \<name\>fs.default.name\</name\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("tput setaf 3")
    nnip=input("Enter the ip of the namenode: ")
    port=input("Enter the port number of hadoop cluster: ")
    os.system("tput setaf 7")
    os.system("echo \<value\>hdfs://{}:{}\</value\> >> /arth-task/task7.1/dn/core-site.xml".format(nnip,port))
    os.system("echo \</property\> >> /arth-task/task7.1/dn/core-site.xml")
    os.system("echo \</configuration\> >> /arth-task/task7.1/dn/core-site.xml")
    if location==1:
        os.system("mv -f /arth-task/task7.1/dn/core-site.xml /etc/hadoop/core-site.xml")
    elif location==2:
        os.system("scp /arth-task/task7.1/dn/core-site.xml {}:/etc/hadoop/core-site.xml".format(ip))
        os.system("rm -f /arth-task/task7.1/dn/core-site.xml")

def namenode(location):
    if location==1:
        #Configure and start namenode in local host
        os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
        os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
        hdfs_site("name",location)
        core_site("name",location)
        os.system('hadoop namenode -format')
        os.system('hadoop-daemon.sh start namenode')
        os.system('jps')
        input("\n\nHit any key to continue")
    elif location==2:
        #Configure and start namenode in remote host
        os.system('scp /root/jdk-8u171-linux-x64.rpm /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/'.format(ip))
        os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(ip))
        os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(ip))
        hdfs_site("name",location)
        core_site("name",location)
        os.system('ssh {} hadoop namenode -format'.format(ip))
        os.system('ssh {} hadoop-daemon.sh start namenode'.format(ip))
        os.system('ssh {} jps'.format(ip))
        input("\n\nHit any key to continue")

def datanode(location):
    if location==1:
        #Configure and start datanode in local host
        os.system('rpm -ivh /root/jdk-8u171-linux-x64.rpm')
        os.system('rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force')
        hdfs_site("data",location)
        core_site("data",location)
        os.system('hadoop-daemon.sh start datanode')
        os.system('jps')
    elif location==2:
        #Configure and start datanode in remote host
        os.system('scp /root/jdk-8u171-linux-x64.rpm /root/hadoop-1.2.1-1.x86_64.rpm {}:/root/'.format(ip))
        os.system('ssh {} rpm -ivh /root/jdk-8u171-linux-x64.rpm'.format(ip))
        os.system('ssh {} rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force'.format(ip))
        hdfs_site("data",location)
        core_site("data",location)
        os.system('ssh {} hadoop-daemon.sh start datanode'.format(ip))
        os.system('ssh {} jps'.format(ip))

def Linux_cmd(location):
    if location==1:
        #Run Cmd on local host
        os.system("tput setaf 3")
        cmd=input("\t\t\t\tEnter the command: ")
        os.system("tput setaf 2")
        os.system(cmd)
        os.system("tput setaf 7")
        input("\n\nHit any key to continue")
    elif location==2:
        #run cmd on remote host
        os.system("tput setaf 3")
        cmd=input("\t\t\t\tEnter your command: ")
        os.system("tput setaf 2")
        os.system("ssh {} {}".format(ip,cmd))
        os.system("tput setaf 7")
        input("\n\nHit any key to continue")

os.system("clear")
os.system("tput setaf 3")
print("\t\t\t\t\t***Welcome To My Program***")
os.system("tput setaf 7")
print("\t\t\t\t\t---------------------------\n\n")
for i in range(3):
    os.system("tput setaf 1")
    Password=gp.getpass("Enter the password: ")
    os.system("tput setaf 7")
    if Password=="redhat":
        os.system("tput setaf 2")
        print("""
                Where do you want to run your :
                Press 1: for local system
                Press 2: for remote system
        """)
        os.system("tput setaf 7")
        location=int(input("-->"))
        if location==2:
            ip = input("\n Please enter the remote host IP: ")
        while True:
            os.system("clear")
            os.system("tput setaf 3")
            print("\t\t\t\t\t***Welcome To My Program***")
            os.system("tput setaf 7")
            print("\t\t\t\t\t---------------------------\n\n")
            if location==1:
                os.system("tput setaf 2")
                print("""
                Press 1: Run Basic Linux command
                Press 2: To configure and start the NameNode
                Press 3: To configure and start datanode
                Press 4: To Create a Static Partition
                Press 5: To Create a logical Partition
                Press 6: To Exit
                """)
                os.system("tput setaf 7")
                requirement=int(input("-->"))
                if requirement==1:
                    Linux_cmd(location)
                elif requirement==2:
                    namenode(location)
                elif requirement==3:
                    datanode(location)
                elif requirement==4:
                    SPartition(location)
                elif requirement==5:
                    LPartition(location)
                elif requirement==6:
                    exit()
            elif location==2:
                os.system("tput setaf 2")
                print("""\n
                Press 1: Run Basic Linux command
                Press 2: To configure and start the NameNode
                Press 3: To configure and start datanode
                Press 4: To Create a Static Partition
                Press 5: To Create a logical Partition
                Press 6: To Exit
                """)
                os.system("tput setaf 7")
                requirement=int(input("-->"))
                if requirement==1:
                    Linux_cmd(location)
                elif requirement==2:
                    namenode(location)
                elif requirement==3:
                    datanode(location)
                elif requirement==4:
                    SPartition(location)
                elif requirement==5:
                    LPartition(location)
                elif requirement==6:
                    exit()
            else:
                print("Invalid input")
                break
    else:
        print("Try Again")
        if (3-i)!=0:
            print("you have",2-i,"Chances left")
