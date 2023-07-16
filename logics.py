class logics:
    r = list()      #rectangle
    d = list()      #diamond
    p = list()      #parallelogram
    s = list()      #start/stop
    def __init__(self, type:str):
        self.type = type[0]
        eval(f"{type[0]}.append(self)")
        self.id = eval(f"len({type[0]})-1")     #'s' for start/stop, 'r' for rectangle, 'd' for diamond, 'p' for parrallelogram
        self.text = ""
    def function(self):
        return eval(f"logics.{self.type}func({self.id})")
    def rfunc(id):
        return
    def dfunc(id):
        return #to be designed by terry
