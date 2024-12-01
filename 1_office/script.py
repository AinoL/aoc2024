# split the input to left and right lists
# sort the lists
# pair the numbers (tuples?)
# calc the diff between the numbers
# add the diffs together
# return the result

def splitinput():
    right = []
    left = []
    with open("input") as file:
        for line in file:
            stripped = line.strip()
            sides = stripped.split("   ")
            left.append(int(sides[0]))
            right.append(int(sides[1]))
    return left, right

def merge(left, right):
    return [(left[i], right[i]) for i in range(0, len(left))]

def diff(merged_list):
    diffs = [abs(i[0]-i[1]) for i in merged_list]
    return sum(diffs)
    
    
def main():
    left, right = splitinput()
    left.sort()
    right.sort()
    merged_list = merge(left, right)
    print(diff(merged_list))


if __name__ == "__main__":
    main()