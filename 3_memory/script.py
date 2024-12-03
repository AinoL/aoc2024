import re

def read_input():
    with open('input', 'r') as input:
        lines = input.readlines()
        strippedlines = [v.strip() for v in lines]
        return " ".join(strippedlines)

def find_occurences(input):
    pattern = r"mul\([0-9]+\,[0-9]+\)"
    return re.findall(pattern, input)

def parse_occurences(occurences):
    numberlist = []
    for o in occurences:
        numbers_with_comma = re.search(r'\((.*)\)', o)
        numbers_as_strings = numbers_with_comma.group(1).split(',')
        numbers = [ int(x) for x in numbers_as_strings ]
        numberlist.append(numbers)
    return numberlist

def multiply(numbers):
    result = []
    for pair in numbers:
        result.append(pair[0] * pair[1])
    return result
        
def main():
    input = read_input()
    occurences = find_occurences(input)
    number_list = parse_occurences(occurences)
    print(number_list)
    multiplied = multiply(number_list)
    print(sum(multiplied))



if __name__ == "__main__":
    main()