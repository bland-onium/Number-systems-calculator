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
    print("input number -> "); N = input(); N = str(N)
    fin = 0; degr = 0; n = []
    print("input your mantiss"); mantiss = int(input())
    print("Input required base: "); dl = int(input())
    #separating
    for i in N:
        n.append(i)
    if ("A" in n) or ("B" in n) or ("C" in n) or ("D" in n) or ("E" in n) or ("F" in n):
        n = n.replace("A", "10").replace("B", "11").replace("C", "12").replace("D", "13").replace("E","14").replace("F", "15")
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
        if n % dl == 10: lst.append("A")
        if n % dl == 11: lst.append("B")
        if n % dl == 12: lst.append("C")
        if n % dl == 13: lst.append("D")
        if n % dl == 14: lst.append("E")
        if n % dl == 15: lst.append("F")
        fin = fin // dl
    lst.reverse()
    print(*lst)
    print("============================")