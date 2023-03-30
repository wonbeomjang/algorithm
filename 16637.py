input()
def d(v, e):
    if not e:return v
    a=-9**99
    if len(e)>=4:a=d(eval(f"{v}{e[0]}({e[1:4]})"),e[4:])
    return max(a,d(eval(f"{v}{e[0:2]}"),e[2:]))
print(d(0,"+"+input()))