#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime

from datetime import date

expirydate = datetime.date(2021, 8,27)
today=date.today()

if(expirydate>today):
    now = datetime.datetime.now()
    today11am = now.replace(hour=10, minute=55, second=0, microsecond=0)
    end11am = now.replace(hour=11, minute=35, second=0, microsecond=0)
    today02pm = now.replace(hour=13, minute=55, second=0, microsecond=0)
    end02pm = now.replace(hour=14, minute=35, second=0, microsecond=0)
    today05pm = now.replace(hour=16, minute=55, second=0, microsecond=0)
    end05pm = now.replace(hour=17, minute=35, second=0, microsecond=0)
    today08pm = now.replace(hour=19, minute=55, second=0, microsecond=0)
    end08pm = now.replace(hour=20, minute=35, second=0, microsecond=0)
    if (now>today11am and now<end11am):
        def chalo():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rhacking in the parity server for next colour--------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def chalo1():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rgetting the colour wait --------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')

        period=220
        clear()
        decision=1
        y=1
        banner='figlet RXCE'
        while(y):
            clear()
            system(banner)
            
            print("Contact me on telegram @Prithvihackz")
            print("Enter ",newperiod," Parity Price :")
            current=input()
            chalo()
            print("\n---------Successfully hacked the server-----------")
            chalo1()
            print("\n---------Successfully got the colour -------------")
            print('\n')
            m=0
            def getSum(n):
                sum = 0
                for digit in str(n):
                    sum += int(digit)
                return sum
            m=getSum(current)+1
            #print(m)
            newperiod=period+decision
            x=(newperiod,"GREEN","")
            y=(newperiod,"RED","")
            if(m%2==0):
                # print(period+decision)
                print(x)
            else:
                # print(period+decision)
                print(y)
            #input=input("")
            decision+=1
            y=input("Do you want to play : Press 1 and 0 to exit \n")
    if (now>today02pm and now <end02pm):
        def chalo():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rhacking in the Sapre server for next colour--------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def chalo1():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rgetting the colour wait --------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
        period=280
        clear()
        decision=1
        newperiod=period
        y=1
        banner='figlet RXCE'
        while(y):
            clear()
            system(banner)
            print("Contact me on telegram @Prithvihackz")
            print("Enter ",newperiod ," Current Sapre Price :" )
            current=input()
            chalo()
            print("\n---------Successfully hacked the server-----------")
            chalo1()
            print("\n---------Successfully got the colour -------------")
            print('\n')
            m=0
            def getSum(n):
                sum = 0
                for digit in str(n):
                    sum += int(digit)
                return sum
            m=getSum(current)+1
            #print(m)
            newperiod=period+decision
            x=(newperiod,"GREEN","")
            y=(newperiod,"RED","")
            if(m%2==0):
                # print(period+decision)
                print(x)
            else:
                # print(period+decision)
                print(y)
            #input=input("")
            decision+=1
            y=input("Do you want to play : Press 1 and 0 to exit \n")
    if (now>today05pm and now < end05pm):
        def chalo():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rhacking in the Bcone server for next colour--------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def chalo1():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rgetting the colour wait --------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
        #period=input("Enter your current period of Bcone : ")
        period=340
        clear()
        decision=1
        y=1
        newperiod=period
        banner='figlet RXCE'
        while(y):
            clear()
            system(banner)
            print("Contact me on telegram @Prithvihackz")
            current=input("Enter Current Price :")
            chalo()
            print("\n---------Successfully hacked the server-----------")
            chalo1()
            print("\n---------Successfully got the colour -------------")
            print('\n')
            m=0
            def getSum(n):
                sum = 0
                for digit in str(n):
                    sum += int(digit)
                return sum
            m=getSum(current)+1
            #print(m)
            newperiod=period+decision
            x=(newperiod,"GREEN","")
            y=(newperiod,"RED","")
            if(m%2==0):
                # print(period+decision)
                print(x)
            else:
                # print(period+decision)
                print(y)
            #input=input("")
            decision+=1
            y=input("Do you want to play : Press 1 and 0 to exit \n")
    if (now>today08pm and now<end08pm):
        def chalo():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rhacking in the Emerd server for next colour--------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def chalo1():
            done = False
            #here is the animation
            def animate():
                for c in itertools.cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    sys.stdout.write('\rgetting the colour wait --------- ' + c)
                    sys.stdout.flush()
                    time.sleep(0.1)
                sys.stdout.write('\rDone!     ')

            t = threading.Thread(target=animate)
            t.start()

            #long process here
            time.sleep(20)
            done = True

        def clear():
            # for windows
            if name == 'nt':
                _ = system('cls')
            # for mac and linux(here, os.name is 'posix')
            else:
                _ = system('clear')
        #period=input("Enter your current period of Emerd : ")
        period=400
        clear()
        decision=1
        y=1
        banner='figlet RXCE'
        while(y):
            clear()
            system(banner)
            print("Contact me on telegram @Prithvihackz")
            period("Enter ", period ," Current Price of Emerd:")
            current=input()
            chalo()
            print("\n---------Successfully hacked the server-----------")
            chalo1()
            print("\n---------Successfully got the colour -------------")
            print('\n')
            m=0
            def getSum(n):
                sum = 0
                for digit in str(n):
                    sum += int(digit)
                return sum
            m=getSum(current)+1
            #print(m)
            newperiod=period+decision
            x=(newperiod,"GREEN","")
            y=(newperiod,"RED","")
            if(m%2==0):
                # print(period+decision)
                print(x)
            else:
                # print(period+decision)
                print(y)
            #input=input("")
            decision+=1
            y=input("Do you want to play : Press 1 and 0 to exit \n")
    else:
        print("Please play on the given time, and If you think it is an error contact admin on telegram @Prithvihackz ")



else:
    print("Your hack has expired--- Please contact on telegram -----------@Prithvihackz")
