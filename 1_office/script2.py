import math
# take the lists
# go through each left list item
# see how many times it appears in the right list
# multiply by that number
# add to final list

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

def find_appearance_rate(left):
    # go through left list, find how many times it appears on the list, remove duplicates
    return set((left[i], left.count(left[i])) for i in range(0, len(left)))

def find_similarity(left, right):
    # go through tuples, find how many times number is on the right list
    # make a new list, add the count
    similarity_list = []
    for item in left:
        similarity_list_item = list(item)
        similarity_list_item.append(right.count(item[0]))
        similarity_list.append(similarity_list_item)
    return similarity_list
        
def count_score(similarity_list):
    return [math.prod(item) for item in similarity_list]


def main():
    left, right = splitinput()
    appearance_tuple_set = find_appearance_rate(left)
    similarity_list = find_similarity(appearance_tuple_set, right)
    score_list = count_score(similarity_list)
    print(sum(score_list))


if __name__ == "__main__":
    main()