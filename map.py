temperatures = ["Label", 32, 50, 77, 104]
c = map(lambda f: (f-32)*(5/9), temperatures[1:]) 
print(list(c))