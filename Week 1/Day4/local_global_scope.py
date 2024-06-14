#local_global_scopes
#global_count = gets from outside of the function
count = 1


def calculation(a,b):

    result = a+b
    #count = 5
    return(result,count)

calculation(5,3)
print(count)


def sum_total():
    calc1 = calculation(5,3)
    calc2 = calculation (10,4)
    result_add = calc1 + calc2
    result_sub = calc1 - calc2
    result  = result_add + result_sub
    return result

print(sum_total())
add,sub = sum_total()
print(add)
print(sub)