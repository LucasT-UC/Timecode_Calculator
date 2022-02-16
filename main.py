import sys, os
from time import time
from termcolor import colored

clear = lambda: os.system('cls')
clear()

def get_minutes(time):
    time /= 30
    if time%60 < 30:
        return int(time//60)
    else:
        return int(time//60 + 1)


def calc(timecode_section):
    timecode_section[0] = timecode_section[0].split(":")
    timecode_section[1] = timecode_section[1].split(":")
    h1 = int(timecode_section[0][0])
    m1 = int(timecode_section[0][1])
    s1 = int(timecode_section[0][2])
    if len(timecode_section[0]) == 4:
        f1 = int(timecode_section[0][3])
    else:
        f1 = 0

    h2 = int(timecode_section[1][0])
    m2 = int(timecode_section[1][1])
    s2 = int(timecode_section[1][2])
    if len(timecode_section[1]) == 4:
        f2 = int(timecode_section[1][3])
    else:
        f2 = 0


    t1_time = total_time(h1, m1, s1, f1)
    t2_time = total_time(h2, m2, s2, f2)
    return t2_time - t1_time


def total_time(h, m, s, f):
    time = 0
    time += f
    time += s*30
    time += m*60*30
    time += h*60*60*30
    return time


def main():
    alive = True
    while alive:
        clear()
        print("WELCOME TO TIMECODE CALCULATOR")
        print("---------------------------------\n")
        total_time = 0
        print("Copy and paste the timecode section as in the format of [0:0:0:0-0:0:0:0] [0:0:0:0-0:0:0:0]")
        timecode_section = input("Insert timecodes here: ")
        timecode_section = timecode_section.split(" ")
        total_time = 0
        for i in range(len(timecode_section)):
            total_time += calculator(timecode_section[i])
        print('________________________________________________________________________')
        print(f"TOTAL DURATION: {colored(get_minutes(total_time), 'green')} minutes\n")
        x = input('Press ENTER to return to menu [0 to exit]: ')
        if x == '0':
            alive = False

    


def calculator(timecode_section):
    timecode_section = timecode_section.replace("[", "")
    timecode_section = timecode_section.replace("]", "")
    timecode_section = timecode_section.replace(" ", "")
    timecode_section = timecode_section.split("-")
    time = calc(timecode_section)
    return time

if __name__ == '__main__':
    main()
    sys.exit()