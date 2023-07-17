def text_to_code(text: str, type: str):
    file = open("program.py", 'a')
    match (type):
        case 'p':
            if (i := text.find('print')) != -1:
                file.write(f"{text[:i+5]}({toString(*splitString(text[i+6:]))})")
            elif (i := text.find('input')) != -1:
                command, data_type, var = text.split(' ')
                file.write(f"{command[:i]+var} = {data_type[1:-1]}(input())")

        case 'r':
            file.write(text)
            
        case 'd':
            if text.find('if') == 0:
                file.write(f"{text}:")
            elif text.find('else if') == 0:
                file.write(f"elif {text[8:]}:")
            elif text.find('else') == 0:
                file.write(f"else:")

    file.write("\n")
                
def toString(*args: str):
    string = 'f"'
    for s in args:
        if s.startswith('"') and s.endswith('"'):
            string += s[1:-1] + ' '
        else:
            string += '{' + s + '}' + ' '
    
    return string[:-1] + '"'

def splitString(string: str):
    stringList = []
    in_quoted_string = False    # False -> Outside a quoted("") string || True -> Inside a quoted("") string
    j = 0                       # keeps track of beginning of a quoted("") string inside the string
    in_word = False             # False -> Outside a word || True -> Inside a word
    k = 0                       # keeps track of beginning of a word inside the string
    
    for i in range(len(string)):

        if string[i] == '"':
            if not in_quoted_string:
                j = i
                in_quoted_string = True
            else:
                stringList.append(string[j:i+1])
                in_quoted_string = False
        elif string[i] != ' ' and not in_quoted_string:
            if string[i-1] == ' ' and not in_word:
                k = i
                in_word = True
            elif i == len(string) - 1:
                stringList.append(string[k:])
                break
            elif string[i+1] == ' ':
                    if k == 0:
                        stringList.append(string[:i+1])
                    elif in_word:
                        stringList.append(string[k:i+1])
                        in_word = False
    return stringList
# "Hello there" name
# text_to_code('input (str) name', 'p')
# text_to_code('input (int) age', 'p')
# text_to_code('age = age + 1', 'r')
# text_to_code('print "Hello there" name "! Next year you\'ll be turning " age ":)"', 'p')
# text_to_code('if age < 18', 'd')
# text_to_code('\tprint "Yet you would be too young to drive :(..Next time!"', 'p')
# text_to_code('else', 'd')
# text_to_code('\tprint "Then you\'ll be able to drive! :)"', 'p')
