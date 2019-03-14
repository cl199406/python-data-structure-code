from pythonds.basic.stack import Stack
#base10 convert base2,base8,base16
def num(n,base):
    DIGITS='0123456789ABCDEF'
    s=Stack()
    while (n>0):
        num=n%base
        s.push(num)
        n=n//base
    string=''
    while (not s.isEmpty()):
        string=string+DIGITS[s.pop()]
    return string
print(num(10,2))
print(num(25,16))
print(num(100,8))