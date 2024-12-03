def read_input():
    # read input file into separate lists, convert strings to int
    with open("input", "r") as input:
        reports = [i.split() for i in input]
        return [[int(i) for i in r] for r in reports]

def check_ascending(r, check):
        # Check if everything in report is ascending normally
        if all(r[i] < r[i+1] and not r[i] <= r[i+1]-4 for i in range(0,len(r)-1)):
            # All good, return true
            return True
        elif (check):
            # Assume nothing works
            safe_with_mods = False
            # Loop through all variations of once modified report
            for i in range(0, len(r)):
               # Make a copy for every possibility to not modify the original list
               new_r = r.copy()
               del new_r[i]
               # Recurse the original loop, change check boolean to false to not go here again
               # If any of the modifications worked, add that to a counter
               safe_with_mods += check_ascending(new_r, False)
            if safe_with_mods > 0:
                # A working modification found, return true
                return True
            else:
                # Nothing worked, return false
                return False
        else:
            # Nothing worked and boolean won't allow check anymore because this is second round, return false
            return False

# Do everything again for descending order
def check_descending(r, check):
        if all(r[i] > r[i+1] and not r[i] >= r[i+1]+4 for i in range(0,len(r)-1)):
            return True
        elif (check):
            safe_with_mods = False
            for i in range(0, len(r)):
               new_r = r.copy()
               del new_r[i]
               safe_with_mods += check_descending(new_r, False)
            if safe_with_mods > 0:
                return True
            else:
                return False
        else:
            return False

def check_safe(reports):
    safe = 0
    # Go through all reports for ascending and descending
    for r in reports:
        safe += check_ascending(r, True)
        safe += check_descending(r, True)
    # How many safe reports were found
    print(safe)

def main():
    reports = read_input()
    check_safe(reports)

if __name__ == "__main__":
    main()