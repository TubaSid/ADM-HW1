def count_substring(string, sub_string):
    sbl=len(sub_string)
    sl = len(string)
    c=0
    for i in range(sl):
        if sub_string==string[i:i+sbl]:
            c+=1
    return c

