"""
M_519 =  # M is the map scale denominator

s_mapd_519 = 0.042 

s_terra_519 = M_519 * s_mapd_519

print(s_terra_519)
"""

def scale(M_519, s_mapd_519):
    
    s_terra_519 = M_519 * s_mapd_519

    print(s_terra_519)
    return 

scale(1000, 0.042)