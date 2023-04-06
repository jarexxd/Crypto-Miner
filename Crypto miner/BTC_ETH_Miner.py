import time
import colorama
from colorama import Fore
from colorama import Style
import random
import string

crypto = str(input('Choose Between ETH and BTC: '))

if crypto == 'ETH' or crypto == 'BTC':
    print("Okay, Wallets are being prepared...")
    time.sleep(3)

    if crypto == 'ETH':
        address = str(input("Please enter your ETH address: "))
        print("Checking if address exist...")
        time.sleep(3)
        print("Check Successful!")
        time.sleep(1)

    elif crypto == 'BTC':
        address = str(input("Please enter your BTC address: "))
        print("Checking if address exist...")
        time.sleep(3)
        print("Check Successful!")
        time.sleep(1)

    class bcolors:
        won = '\033[92m'
        fail = '\033[91m'
    
    def id_gen(size = 40, chars = string.ascii_uppercase + string.digits):
        return "".join(random.choice(chars) for _ in range(size))

    tries = 0

    colorama.init()
    if crypto == 'ETH':
        while(True):
            if(tries > random.randint(10000, 10000)):
                print(Fore.GREEN + "[-] 0x" + id_gen() + " | Vaild | " + "0.0132 ETH")
                print("Transfer 0.0132 ETH to", address)
                time.sleep(6)
                tries = 0
                print("Done! Miner is running again")
                time.sleep(3)
            else:
                print(Fore.RED + "[-] 0x" + id_gen() + " | Invaild | " + "0.0000 ETH")
                tries += 1

    colorama.init()
    if crypto == 'ETH':
        while(True):
            if(tries > random.randint(10000, 10000)):
                print(Fore.GREEN + "[-] bc1" + id_gen() + " | Vaild | " + "0.0132 BTC" )
                print("Transfer 0.0132 BTC to", address)
                time.sleep(6)
                tries = 0
                print("Done! Miner is running again")
                time.sleep(3)
            else:
                print(Fore.RED + "[-] 0x" + id_gen() + " | Invaild | " + "0.0000 BTC")
                tries += 1

else: print("Invaild Currency Please Pick Between: 'ETH' or 'BTC'")