global_var=10 #global variable

def add(x,y):
    local_var=x+y 
    return local_var+global_var

result=add(4,5)
print("Addition is :", result)