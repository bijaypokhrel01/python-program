def hcf(x: int , y: int)->int:
    if x == 0:
        return y
    else:
        if x>y:
            return hcf(x%y, y)
        else:
            return hcf(y%x, x)
            
print(hcf(66, 48))
print(66 * 48 // hcf(66, 48))
