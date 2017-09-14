import math

def hyp (a, b):
    c = a**2 + b**2
    c = math.sqrt (c)
    return c

functie_result = hyp (3, 4)
#print (functie_result)
print()

def hello(name):
    print ('Welcome ' + name + ' to the world of Python.')

#hello('Julia')

def rng(lijst):
    kleinste =  min(lijst)
    grootste = max(lijst)
    bereik = grootste - kleinste
    return bereik
print (rng([4, 0, 1, -2]))
print (rng([123, 1344, 1234]))