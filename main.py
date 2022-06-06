import re
def main():
    file1 = open('PythonRegex/resources/con228.bugs.799464655', 'r')
    Lines = file1.readlines()
    count = 0
    print("Found occurrences:")
    for line in Lines:
        if re.search(".edu.*menu", line):
            count += 1
            print("Line {}: {}".format(count, line.strip()))
if __name__ == "__main__":
    main()
