def trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False

val = trouble(True, False)
print(val)
val = trouble(False, False)
print(val)

def int_sum(a,b):
    if a==b:
        return 2*(a+b)
    else:
        return (a+b)

def hours(h):
    hours_arr = []
    for i in range(h+1,24,1):
        hours_arr.append(i)
    return hours_arr

def hours_1(h):
    return list(range(h+1,24))

def pos_neg(a,b, negative):
    if negative:
        return (a<0) and (b<0)
    else:
        return (a>0 and b<0) or (a<0 and b>0)

def front_back(s):
    if len(s) == 1:
        return s
    else:
        mid = s[1:-1]
        f = s[0]
        l = s[-1]
        return (l + mid + f)

def front3letters(s,num=3):
    if len(s) >= 3:
        new_s = s[0:3]*num
        return new_s

def extra_end(p, num=3):
    if len(p) >= 2:
        new_p = p[-2:]*num
        return new_p

def zero_list(g_list):
    new_list = []
    g_list_len = len(g_list)
    new_list_len = g_list_len * 2
    last_el = g_list[-1]

    for new_el in range(new_list_len):
        new_list.append(0)
    new_list[-1] = last_el
    return new_list

def zero_list_2(g_l):
    new_list = [0]* len(g_l)*2
    new_list[-1] = g_l[-1]
    return new_list

def int_nine(g_list):
    count = 0
    for i in g_list:
        if i ==9:
            count = 1 + count
        else:
            count = 0 + count
    return count


f = lambda a: a* a

# main function
if __name__ == '__main__':
    # val = trouble(True, False)
    # print(val)
    # int_sum()

    # problem03
    #  val_3 = int_sum(3,3)
    # print(val_3)

    # problem 04
    # val_4 = hours(6)
    # print(val_4)

    # print(pos_neg(-3,4,True))
    # problem6
    # print(front_back('prabath'))

    print(front3letters('prabath',6))

    print(extra_end('Prabath',3))

    print(zero_list([4,5,6]))

    print(int_nine([1,2,9,4,9]))

    f = lambda a: a * a
    print(f(12))

    h = lambda x,y: x * x + y
    print(h(3,1))