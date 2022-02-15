import sys
from time import time


def get_minutes(time):
    time /= 30
    print(f"minutes: {time//60}")
    print(f"seconds: {time%60}")
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
    print(f"t1 time = {t1_time}")
    t2_time = total_time(h2, m2, s2, f2)
    print(f"t2 time = {t2_time - t1_time}")
    return t2_time - t1_time


def total_time(h, m, s, f):
    time = 0
    time += f
    time += s*30
    time += m*60*30
    time += h*60*60*30
    return time


def main():
    print("WELCOME TO TIMECODE CALCULATOR")
    print("---------------------------------\n")
    total_time = 0
    print("Copy and paste the timecode section as in the format of [0:0:0:0-0:0:0:0] [0:0:0:0-0:0:0;0]")
    timecode_section = input("Insert timecodes here: ")
    timecode_section = timecode_section.split(" ")
    total_time = 0
    for i in range(len(timecode_section)):
        total_time += calculator(timecode_section[i])
    print(f"TOTAL DURATION: {get_minutes(total_time)} minutes")



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