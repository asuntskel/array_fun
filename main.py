
class Pos:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

tab = [[" " for i in range(5)] for i in range(5)]
cur = Pos(1, 2);

tab[cur.y][cur.x] = "$"

inc=1;

flags = [True, True, True, True];
while(any(flags)):
    if cur.y-inc >= 0:
        tab[cur.y-inc][cur.x] = "*";
    else:
        flags[0]=False;
        
    if cur.y+inc < 5:
        tab[cur.y+inc][cur.x] = "*";
    else:
        flags[1]=False;
        
    if cur.x-inc >= 0:
        tab[cur.y][cur.x-inc] = "*";
    else:
        flags[2]=False;
        
    if cur.x+inc < 5:
        tab[cur.y][cur.x+inc] = "*";
    else:
        flags[3]=False;
        
    inc+=1;
    
for line in tab:
    for char in line:
        print("_" + char + "_", end=" ")
    print("\n")
    
