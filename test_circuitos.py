
#Entrada dos valores das chaves a ser testadas, com 0 e 1 que serão convertidas para bool
bins = [
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
]

bins_bool = []

for num in bins:
    
    #print(bins.index(num), " -",num)
    
    new_nun_bool = []
    for val in num:
        new_nun_bool.append(bool(val))
    bins_bool.append(new_nun_bool)
        

print(bins_bool)
    

def test_a(bins_bool):
    
    print("\n ------------[ a ]-------------")
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if not( ( not(A) and not(B) and C ) or (A and not(B) and not(C)) ):
            print( bins_bool.index(num_bool), " - ", num_bool)
    

def test_b(bins_bool):
    
    print("\n ------------[ b ]-------------")
    
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if not( A and ( (not(B) and C ) or (B and not(C)) ) ):
            print( bins_bool.index(num_bool), " - ", num_bool)
    
def test_c(bins_bool):
    
    print("\n ------------[ c ]-------------")
    
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if not( not(A) and B and not(C) ):
            print( bins_bool.index(num_bool), " - ", num_bool)
            
        
def test_d(bins_bool):
    
    print("\n ------------[ d ]-------------")
    
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if not( ( not(A) and not(B) and C) or (A and ( ( not(B) and not(C) ) or (B and C) ) ) ):
            print( bins_bool.index(num_bool), " - ", num_bool)
            
        
    
def test_e(bins_bool):
    
    print("\n ------------[ e ]-------------")
    
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if ( not(A) and not(B) and not(C) ) or ( A and ( (not(B) and C) or (B and not(C)) ) ):
            print( bins_bool.index(num_bool), " - ", num_bool)
            
        
def test_f(bins_bool):
    
    print("\n ------------[ f ]-------------")
    
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if (not(B) and not(C)) or (A and ( (not(B) and C) or (B and not(C)) )):
            print( bins_bool.index(num_bool), " - ", num_bool)
            
    

def test_g(bins_bool):
    
    print("\n ------------[ g ]-------------")
    
    for num_bool in bins_bool:
        
        A, B, C = num_bool
        
        if not( (not(A) and not(B)) or (A and B and C) ):
            print( bins_bool.index(num_bool), " - ", num_bool)
            
        
test_a (bins_bool)
test_b (bins_bool)
test_c (bins_bool)
test_d (bins_bool)
test_e (bins_bool)
test_f (bins_bool)
test_g (bins_bool)




