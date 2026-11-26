def fast_sort(a):
    if len(a) <= 1: 
        return a
    opora = a[len(a) // 2]
    menshe = [x for x in a if x < opora]
    ravno = [x for x in a if x == opora]
    bolshe = [x for x in a if x > opora]
    return fast_sort(menshe) + ravno + fast_sort(bolshe)


print(fast_sort([5,2,3,4,5,4]))
