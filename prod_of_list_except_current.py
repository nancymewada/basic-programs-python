def my_function(arg):
    ans = []
    prods_of_except_index =  []
    prod = 1
    prod1 = 1
    for i,v in enumerate(arg):
        prods_of_except_index.append(prod)
        prod *=v
    for i in range(len(arg)-1,-1,-1):
        prods_of_except_index[i] *= prod1
        prod1 *= arg[i]
    return prods_of_except_index

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function([2,6,7,10])