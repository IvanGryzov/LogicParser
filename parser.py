fr=[]
pos=0
var={}

def imp(a,b):
    return not(a)or b

def equ(a,b):
    return a and b or not(a) and not(b)

def getPos():
    global pos,fr
    if len(fr)>pos:
        return fr[pos]
    else:
        return ""

def ImpOp():
    global pos, fr
    res = OrOp()
    while getPos() in ['imp','equ']:
        op = getPos()
        pos+=1
        res2 = OrOp()
        if op=='imp':
            res = imp(res,res2)
        elif op=='equ':
            res = equ(res,res2)
    return res

def OrOp():
    global pos, fr
    res = AndOp()
    while getPos() == 'or':
        op = getPos()
        pos += 1
        res2 = AndOp()
        res = res or res2
    return res

def AndOp():
    global pos, fr
    res = NotOp()
    while getPos() == 'and':
        op = getPos()
        pos += 1
        res2 = NotOp()
        res = res and res2
    return res

def NotOp():
    global pos,fr,var
    literal=getPos()
    if len(literal)>0 and literal in "ABCDEFGH":
        pos+=1
        #print("---",literal)
        return var[literal]
    elif literal=='(':
        pos+=1
        return OrOp()
        pos+=1
    elif literal=='not':
        pos+=1
        return not NotOp()

def Parser(s):
    """
    
    :param s: Строка с формулой 
    :return: значение
    """
    global fr,var,pos
    fr = s.split()
    print(fr)
    bool=[False,True]
    for x in bool:
        for y in bool:
            pos=0
            var['A'] = x
            var['C'] = y
            print(x,y,ImpOp())



var={'A':True,'C':True}
Parser('A or not C')

