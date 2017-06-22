'''
This is the parser for osprey.  A basic example can be
found in the README file.  It is based somewhat on
LaTeX but has a unique format.
'''

from utilities import dotdict

def get_command(data):
    words = ""
    while data:
        letter = data[0]
        if letter != "{":
            words=words+letter
        else:
            return words, data
        data= data[1:]
    return "", data

def get_next(string):
    ret = string[0]
    string=string[1:]
    return ret, string

def get_enclosed(data):
    total = 1
    content = ""
    temp, data.curstr(get_next(data.curstr))
# add some error catching here
        while True
        if temp == "}":
            total -=1
            if total == 0:
                return content
            content += temp
        if char == "{":
            total += 1


def execute_command(data):
    command = ''
    temp, data.curstr(get_next(data.curstr))
    while temp != '{':
        command += temp
        temp, data.curstr(get_next(data.curstr))
    substr = get_enclosed(data.curstr)
#at this point we should have both the command and the content
#now we just need to figure out the command and do it
    if command == 'title':
        doTitle(data, substr)
    elif command == 'p':
        doParagraph(data, substr)
    elif command == 'list':
        doList(data, substr)
    elif command == 'nlist':
        doNList(data, substr)
    elif command == 'section':
        doSection(data, substr)
    elif command == 'link':
        doLink(data, substr)
    elif command == 'img':
        doImage(data, substr)


def goto_next_command(data):
    while len(data.curstr) != 0:
        temp, data.curstr = get_next(data.curstr)
        if temp == "\\":
            execute_command(data.curstr)
    return data

#this adds chars to html until it hits a command and return when len is 0
def parse_data(data):
    while len(data.curstr) != 0:
        if data.depth == 0:
            goto_next_command(data)
        else:
            temp, data.curstr = get_next(data.curstr)
            if temp == "\\":
                data.depth+=1
                execute_command(data)
            else:
                data.html += temp
    return data


data['depth'] = 0
data['html'] = ""
data['curstr'] = ""
f = open("test_text", "r")
data.curstr = f.read()
html = parse_data(data)
