def text_to_code(text: str, type: str):
    file = open("program.py", 'a')
    match (type):
        case 'p':
            if text.find('print') == 0:
                file.write(f"{text[:5]}({toString(*splitString(text[6:]))})")
            elif text.find('input') == 0:
                command, data_type, var = text.split()
                file.write(f"{var} = {data_type[1:-1]}(input())")

        case 'r':
            file.write(text)
            
        case 'd':
            pass
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
    l = []
    is_string = False
    in_string = False
    j = 0
    k = 0
    for i in range(len(string)):
        if string[i] == '"':
            if not is_string:
                j = i
                is_string = True
            else:
                l.append(string[j:i+1])
                is_string = False
        
        elif string[i] != ' ' and not is_string:
            if string[i-1] == ' ' and not in_string:
                k = i
                in_string = True
            if i == len(string) - 1:
                l.append(string[k:])
                break
            if string[i+1] == ' ' and in_string:
                    l.append(string[k:i+1])
                    in_string = False
    return l

# "Hello there" name
text_to_code('input (str) name', 'p')
text_to_code('input (int) age', 'p')
text_to_code('age = age + 1', 'r')
text_to_code('print "Hello there" name "! Next year you\'ll be turning " age ":)"', 'p')
