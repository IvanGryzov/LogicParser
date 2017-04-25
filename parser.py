fr=[]
pos=0
var={}
bool=[False,True]

def imp(a,b):
    return not(a)or b

def equ(a,b):
    return a and b or not(a) and not(b)

def xor(a,b):
    return a and not(b) or not(a)and b

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
    while getPos() in ['or','xor']:
        op = getPos()
        pos += 1
        res2 = AndOp()
        if op == 'or':
            res = res or res2
        elif op == 'xor':
            res = xor(res,res2)
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
    if len(literal)>0 and literal in "ABCDEFGHIKLMNOPQRSTVXYZ":
        pos+=1
        #print("---",literal)
        return var[literal]
    elif literal=='(':
        pos+=1
        res = ImpOp()
        pos+=1
        return res
    elif literal=='not':
        pos+=1
        return not NotOp()

def All(n):
    global fr, var, pos,bool
    if n>=len(var):
        pos = 0
        for x in sorted(var):
            print(var[x], end="\t")
        print(ImpOp())
    else:
        for x in bool:
            var[sorted(list(var.keys()))[n]] = x
            All(n+1)


def Parser(s):
    """
    
    :param s: Строка с формулой 
    :return: значение
    """
    global fr,var,pos
    lit=['(',')','xor','or','and','imp','equ','not']
    for x in lit:
        s=s.replace(x,' '+x+' ')

    print(s)
    fr = s.split()

    for x in fr:
        if x in 'ABCDEFGHIKLMNOPQRSTVXYZ':
            var[x]=False
    print(fr)

    for x in sorted(var):
        print(x,end="\t\t")
    print("F")
    All(0)


Parser('(A imp B ) or ( not A imp not B )')

