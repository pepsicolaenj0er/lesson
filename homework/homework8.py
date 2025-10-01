    #i = день 
    #n = число последовательных дней 
    #m = имена 
    #a = количество имен
def countPageTurns(n, m, a):
    x = 0
    pageTurns = []
    for i in a:
        f = (x+i) // m
        pageTurns.append(f)
        x = (x+i) % m
            
    return pageTurns

m = 4 
a = [3 , 5 , 2]
print(countPageTurns (len(a),m,a))
            