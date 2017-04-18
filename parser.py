fr=[]
pos=0

def ImpOp():
    global pos, fr
    res = OrOp()
    while fr[pos] in ['imp','equ']:
        op = fr[pos]
        pos+=1
        res2 = OrOp()
        if op=='imp':
            res = res or res2
        elif op=='equ':
            res = res or res2
    return res

def OrOp():
    global pos, fr
    res = AndOp()
    while fr[pos] == 'or':
        op = fr[pos]
        pos += 1
        res2 = AndOp()
        res = res or res2
    return res

def AndOp():
    global pos, fr
    res = NotOp()
    while fr[pos] == 'and':
        op = fr[pos]
        pos += 1
        res2 = NotOp()
        res = res and res2
    return res

def NotOp():
    global pos,fr
    if fr[pos] in "ABCDEFGH":
        pos+=1
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
    print(ImpOp())

Parser('A or not C')
print(fr)
"""
var s: string; {исходное выражение}
 i: integer; {номер текущего символа}
function Mul: longint; forward;
function Factor: longint; forward;
///Суммирует слагаемые
function Add: longint;
var
 q, res: longint;
 c: char;
begin
 res := Mul; {первое слагаемое}
 while s[i] in ['+', '-'] do
 begin
 c := s[i];
 i := i + 1;
 q := Mul; {очередное слагаемое}
 case c of
 '+': res := res + q;
 '-': res := res - q;
 end
 end; {while}
 Add := res
end;
///Перемножает множители
function Mul: longint;
var
 q, res: longint;
 c: char;
begin
 res := Factor; {первый множитель}
 while s[i] in ['*', '/'] do
 begin
 c := s[i];
 i := i + 1;
 q := Factor; {очередной множитель}
 case c of
 '*': res := res * q;
 '/':
 if q = 0 then
 begin
 writeln('деление на 0');
 halt
 end
 else res := res div q
 end {case}
 end; {while}
 Mul := res
end;
///Выделяет число
function Number: longint;
var
 res: longint;
begin
 res := 0;
 while (i <= length(s)) and
 (s[i] in ['0'..'9']) do
 begin
 res := res * 10 + (ord(s[i]) - ord('0'));
 i := i + 1
 end;
 Number := res
end;
///Выделяет множитель
function Factor: longint;
var
 q: longint;
 c: char;
begin
 case s[i] of
 '0'..'9': Factor := Number;
 '(':
 begin
 i := i + 1;Factor := Add;
 i := i + 1; {пропустили ')'}
 end;
 '-':
 begin
 i := i + 1;
 Factor := -Factor;
 end
 else begin
 writeln('ошибка');
 halt
 end
 end {case}
end;
begin {основная программа}
 readln(s); i := 1;
 writeln(Add)
end.
"""