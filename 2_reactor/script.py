# read input
# divide each row into their own list
# if the numbers increase or decrease add to safe counter
# take into account how much the number can increase and descrease
# else the input is unsafe
# add safe inputs in the final counter

def read_input():
    # read input file into separate lists, convert strings to int
    with open("input", "r") as input:
        reports = [i.split() for i in input]
        return [[int(i) for i in r] for r in reports]

def check_ascending(reports):
    safe = 0
    for r in reports:
        if all(r[i] < r[i+1] and not r[i] <= r[i+1]-4 for i in range(0,len(r)-1)):
            safe += 1
    return safe

def check_descending(reports):
    safe = 0
    for r in reports:
        if all(r[i] > r[i+1] and not r[i] >= r[i+1]+4 for i in range(0,len(r)-1)):
            safe += 1
    return safe

def check_safe(reports):
    asc = check_ascending(reports)
    desc = check_descending(reports)
    return asc + desc

def main():
    reports = read_input()
    print(check_safe(reports))

if __name__ == "__main__":
    main()