# Cardly
# By: MrMidnight / Twitter: @MrMidnight53

import random, time

def date_n_cvc():
    print(end=", ")
    print(random.randint(1, 12), end="" + "/")
    print(random.randint(2027, 2077), end="" + ", ")
    print(random.randint(000, 999))

def rng():
    print(random.randint(0, 9), end='')

def mastercard():

    print("Mastercard",end=", ")
    for i in range(0,18):
        rng()
    date_n_cvc()

def visa():

    print("Visa",end=", ")
    for i in range(0,16):
        rng()
    date_n_cvc()


def amex():

    print("Amex",end=", ")
    for i in range(0,15):
        rng()
    date_n_cvc()


def unionpay():

    print("Unionpay",end=", ")
    for i in range(0,16):
        rng()
    date_n_cvc()

def diners():

    print("Diners", end=", ")
    for i in range(0,16):
        rng()
    date_n_cvc()

def discover():

    print("Discover", end=", ")
    for i in range(0,16):
        rng()
    date_n_cvc()


def logo():
    print("  /$$$$$$                            /$$ /$$          ")
    print(" /$$__  $$                          | $$| $$          ")
    print("| $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$$| $$ /$$   /$$")
    print("| $$       |____  $$ /$$__  $$ /$$__  $$| $$| $$  | $$")
    print("| $$        /$$$$$$$| $$  \__/| $$  | $$| $$| $$  | $$")
    print("|  $$$$$$/|  $$$$$$$| $$      |  $$$$$$$| $$|  $$$$$$$")
    print(" \______/  \_______/|__/       \_______/|__/ \____  $$")
    print("                                             /$$  | $$")
    print("By: MrMidnight                              |  $$$$$$/")
    print("Twitter: @MrMidnight53                       \______/ \n")



def __init__():
    logo()
    while True:
        print("What kind of card do you wish to generate?")
        print("1.Mastercard\n2.Visa\n3.Amex\n4.Unionpay\n5.Diners\n6.Discover\n7.Quit")
        userimp=input(":> ")
        print("")


        if userimp=="1":

            print("How many times?")
            times = int(input(":> "))
            print("")

            for i in range(0,times):
                mastercard()
            time.sleep(1)
            print("")

        elif userimp=="2":

            print("How many times?")
            times = int(input(":> "))
            print("")

            for i in range(0,times):
                visa()
            time.sleep(1)
            print("")

        elif userimp=="3":
            print("How many times?")
            times = int(input(":> "))
            print("")
            for i in range(0,times):
                amex()
            time.sleep(1)
            print("")

        elif userimp=="4":
            print("How many times?")
            times = int(input(":> "))
            print("")
            for i in range(0,times):
                unionpay()
            time.sleep(1)
            print("")

        elif userimp=="5":
            print("How many times?")
            times = int(input(":> "))
            print("")
            for i in range(0,times):
                diners()
            time.sleep(1)
            print("")

        elif userimp=="6":
            print("How many times?")
            times = int(input(":> "))
            print("")
            for i in range(0,times):
                discover()
            time.sleep(1)
            print("")

        elif userimp=="7":
            print("Thx 4 using me :D")
            exit()

        else:
            print("Invalid Input!\n")
            time.sleep(1)


__init__()
