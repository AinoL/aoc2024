# each report can make one mistake in the logic
# once an error is found, remove the item that caused the error and run the check again
from itertools import dropwhile

def read_input():
    # read input file into separate lists, convert strings to int
    with open("test", "r") as input:
        reports = [i.split() for i in input]
        return [[int(i) for i in r] for r in reports]


def check_ascending(r, original_length, recheck):
    new_list = []
    for i in range(0,len(r)-1):
        if r[i] < r[i+1] and r[i]+3 >= r[i+1]:
            new_list.append(r[i])
    new_list.append(r[-1])
    if(len(new_list) == original_length-1) and recheck==True:
        return check_ascending(new_list, original_length, False)
    elif(len(new_list) < original_length-1):
        return 0
    else:
        return 1

def check_descending(r, original_length, recheck):
    new_list = []
    for i in range(0,len(r)-1):
        if r[i] > r[i+1] and r[i]-3 <= r[i+1]:
            new_list.append(r[i])
    new_list.append(r[-1])
    if(len(new_list) == original_length-1) and recheck==True:
        return check_descending(new_list, original_length, False)
    elif(len(new_list) < original_length-1):
        return 0
    else:
        return 1



def check_safe(reports):
    safe = 0
    for r in reports:
        safe += check_ascending(r, len(r), True)
        safe += check_descending(r, len(r), True)
    print(safe)

def main():
    reports = read_input()
    check_safe(reports)

if __name__ == "__main__":
    main()