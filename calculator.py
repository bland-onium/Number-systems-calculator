print("input command(0->float)(1->int): ")
cmnd = int(input())

if cmnd == 0:
    print("Now you're turning 10th to 2nd.")
    print("input number -> ")
    numb = float(input())
    print("Please, input length of required base -> "); listlen = int(input())
    lst = []
    while (len(lst) < listlen) or (numb != 0):
        if numb == 0: break
        if numb * 2 < 1:
            lst.append('0')
        elif numb * 2 > 1:
            lst.append('1')
        numb = numb * 2
        if numb > 1: numb = numb - 1
        if len(lst) == listlen:
            print(*lst)
            break

if cmnd == 1:
    fin = 0; degr = 0; n = []
    print("input number -> "); N = input(); N = str(N); N = N.upper()
    print("input your mantiss"); mantiss = int(input())
    print("Input required base: "); dl = int(input())
    #separating
    for i in N:
        if   ("A" == i): i = "10"
        elif ("B" == i): i = "11"
        elif ("C" == i): i = "12"
        elif ("D" == i): i = "13"
        elif ("E" == i): i = "14"
        elif ("F" == i): i = "15"
        n.append(i)
    #turn into 10
    while len(n) > 0:
        fin = fin + int(n[-1]) * ((mantiss ** degr))
        del n[-1]
        degr += 1
    print("10 ->", fin)
    #turn into another system
    lst = []
    while fin > 0:
        n = fin
        if n % dl < 10: lst.append(n % dl)
        elif n % dl == 10: lst.append("A")
        elif n % dl == 11: lst.append("B")
        elif n % dl == 12: lst.append("C")
        elif n % dl == 13: lst.append("D")
        elif n % dl == 14: lst.append("E")
        elif n % dl == 15: lst.append("F")
        fin = fin // dl
    lst.reverse()
    print(*lst)
    print("============================")