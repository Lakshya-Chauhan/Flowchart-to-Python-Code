import os

class FlowChartComponent(object):
    IO = 0
    PROCESS = 1
    DECISION = 2
    __FILE_PATH = os.path.dirname(__file__) + r'\program.py'    # Mangled Attribute. Cannot be accessed directly in code.

    def __init__(self, text: str, type: int) -> None:
        self.text = text
        self.type = type # IO, PROCESS, DECISION

    def text_to_code(self):

        file = open(FlowChartComponent._FlowChartComponent__FILE_PATH, 'a')

        match (self.type):
            case FlowChartComponent.IO:
                if self.text.find('print') != -1:
                    splittingIndex = self.text.find('print') + 5
                    file.write(f"{self.text[:splittingIndex]}({FlowChartComponent.toString(*FlowChartComponent.splitString(self.text[splittingIndex+1:]))})\n")
                    return True
                elif (i := self.text.find('input')) != -1:
                    command, data_type, var = self.text.split(' ')
                    file.write(f"{command[:i]+var} = {data_type[1:-1]}(input())\n")
                    return True
                return False # signfies an error 
                
            case FlowChartComponent.PROCESS:
                file.write(self.text + '\n')
                return True

            case FlowChartComponent.DECISION:
                if self.text.find('if') == 0:
                    file.write(f"{self.text}:\n")
                    return True
                elif self.text.find('else if') == 0:
                    file.write(f"elif {self.text[8:]}:\n")
                    return True
                elif self.text.find('else') == 0:
                    file.write(f"else:\n")
                    return True
                return False
            

    @staticmethod
    def toString(*args: str):
        string = 'f"'
        for s in args:
            if s.startswith('"') and s.endswith('"'):
                string += s[1:-1] + ' '
            else:
                string += '{' + s + '}' + ' '
        return string[:-1] + '"'
    
    @staticmethod
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
    
# print(FlowChartComponent.__FILE_PATH) # doesn't work
ioBox1 = FlowChartComponent("print \"Hi! What's your age?\"", FlowChartComponent.IO)
ioBox2 = FlowChartComponent("input (int) age", FlowChartComponent.IO)
processBox1 = FlowChartComponent("age = age + 1", FlowChartComponent.PROCESS)
decisionBox1 = FlowChartComponent("if age < 18", FlowChartComponent.DECISION)
ioBox3 = FlowChartComponent("\tprint \"You would be underage to drive even next year :(\"", FlowChartComponent.IO)
decisionBox2 = FlowChartComponent("else", FlowChartComponent.DECISION)
ioBox4 = FlowChartComponent("\tprint \"You would be able to drive the next year :)\"", FlowChartComponent.IO)

components = [ioBox1, ioBox2, processBox1, decisionBox1, ioBox3, decisionBox2, ioBox4] # We would need to store all the components in a linked list
for obj in components:
    obj.text_to_code()