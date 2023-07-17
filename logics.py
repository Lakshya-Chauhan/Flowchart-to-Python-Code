class logics:
    r = list()      #rectangle
    d = list()      #diamond
    p = list()      #parallelogram
    s = list()      #start/stop
    def __init__(self, type:str):
        self.type = type[0]
        self.id = eval(f"len({type[0]})-1")     #'s' for start/stop, 'r' for rectangle, 'd' for diamond, 'p' for parrallelogram
        self.text = ""
        eval(f"{type[0]}.append(self)")
    def function(self):
        return eval(f"logics.{self.type}func({self.id})")
    def rfunc(id):
        return
    def dfunc(id):
        string = logics.d[id]
        try:
            if (eval(string)) in [True, False]:
                return string
        except NameError: return string
        except: pass
        string = string.replace("to", "")
        m = ["greater", "larger", "bigger", "is more"]#Other words which can be used for 'more'
        l = ["lesser", "smaller", "shorter", "is less"]#Other words which can be used for 'less'
        et = ["equals", "is equal", "is"]#==
        mt = ["more than", "not less than or equal"]#>
        lt = ["smaller than", "not more than or equal"]#<
        mtoet = ["more than or equal", "not less than"]#>=
        ltoet = ["less than or equal", "not more than"]#<=
        
