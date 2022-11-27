import re

def main(path):
    path += '.txt'
    with open(path, 'r') as html:
        string = html.readlines()
        for i in string:
            # поиск длинных ссылок
            #out = re.findall(r'href="\S{1,}"', i)
            # поиск ссылок длинной до 512 символов
            out = re.findall(r'href="\S{1,512}"', i)
            if out != []:
                for item in out:
                    print(item, end='\n')

#input files:
# 'test1', 'test2'
path = 'test2'
main(path)
