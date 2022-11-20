import re

def main(path):
    path += '.txt'
    with open(path, 'r') as html:
        string = html.readlines()
        for i in string:
            out = re.findall('href=\"\S*\"', i)
            if out != []:
                print(*out)

#input files:
# 'test1', 'test2'
path = 'test2'
main(path)
