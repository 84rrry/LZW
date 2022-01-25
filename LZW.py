
from pprint import pp, pprint


def encode(msg):
    # Build the dictionary.
    dic_size=128 
    dic ={ chr(i):i for i in range(dic_size)}
    # pprint(dic)
    P = ""
    code = []
    for C in msg:
        S = P + C
        if S in dic:
            P = S
        else:
            # print(P)
            code.append(dic[P])
            dic[S] = dic_size
            dic_size += 1
            P = C
    if P:
       code.append(dic[P])
    return code
def decode(code):

#   [98, 97, 114, 114, 121]
#barry

    dic_size=128
    dic = {i:chr(i) for i in range(dic_size)}
    P=''
    Output=c=chr(code.pop(0))
    for n in code:
        if n in dic:
            courant = dic[n]
        elif n == dic_size:
            courant = c + c[0]
        Output+=courant
        dic[dic_size] = c + courant[0]
        dic_size += 1
        c = courant
    return Output


