import random
import time
def help():
    print("time - date and time")
    print("repeat - repeat input string")
    print("randnum - generate a random number")
    print("quit - quit")
commandline = ""
print("CMD python edition")

#Loop
while commandline != "exit":
    commandline = input("> ").lower()
    if commandline == "time":
        print(time.asctime())
    elif commandline == "help":
        help()
    elif commandline == "":
        print("")
    elif commandline == "quit":
        time.sleep(.5)
        exit()
    elif commandline == "repeat":
        rpt = input("Write sentence to repeat> ")
        print(rpt)
    elif commandline == "randnum":
        randchoice = input("Integer or Uniform?> ").lower()
        randinp = input("Enter max number> ")
        if randchoice == "integer":
            print(random.randint(0, int(randinp)))
        elif randchoice == "uniform":
            print(random.uniform(0, float(randinp)))
    else:
        print(commandline + " is not a recognized command")