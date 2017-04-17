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