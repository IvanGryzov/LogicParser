fr=[]
pos=0

def OrOp():
    pass

def NotOp():
    global pos,fr
    if fr[pos] in "ABCDEFGH":
        return False
    elif fr[pos]=='(':
        pos+=1
        return OrOp()
        pos+=1
    elif fr[pos]=='not':
        pos+=1
        return not NotOp()

def Parser(s):
    """
    
    :param s: Строка с формулой 
    :return: значение
    """
    global fr
    fr = s.split()
    print(fr)
    pos=0
    print(NotOp())

Parser('not C')
print(fr)
