def intersect(cir1, cir2): 
    distSq = (cir1[0] - cir2[0]) * (cir1[0] - cir2[0]) + (cir1[1] - cir2[1]) * (cir1[1] - cir2[1]);  
    radSumSq = (cir1[2] + cir2[2]) * (cir1[2] + cir2[2]);  
    if (distSq == radSumSq): 
        return 1 
    elif (distSq > radSumSq): 
        return -1 
    else: 
        return 0 
   
  
x1 = 2
y1 = 3 
x2 = 3
y2 = 6
r1 = 12
r2 = 10 
  
res = intersect([x1, y1, x2], [y2, r1, r2])  
if (res == 0): 
    print("Circle intersect to each other.") 