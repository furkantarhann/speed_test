import random
import time


liste=["car","elipse","jewelery","reddit","phone","skimming","mouse","laptop"]
total=0



def start():
    global total
    key=random.choice(liste)
    print("Type:",key)
    start=time.time()
    answer2=input()
    if answer2.upper()==key.upper():
        finish=time.time()
        questiontime=finish-start
        total+=questiontime
        liste.remove(key)
    else:
        print("You made a mistake.Try later!")
        finish = time.time()
        questiontime = finish - start
        total += questiontime



def main():
    print("*************************************")
    print("             SPEED  TEST             ")
    print("*************************************\n")
    time.sleep(1)
    print("Do you want to see how is your speed of typing skills?")
    time.sleep(1)
    answer1 = input("Type 'START' to start. ")
    if answer1.upper() == "START":
        while len(liste)!=0:
            start()
    print(total)




main()
