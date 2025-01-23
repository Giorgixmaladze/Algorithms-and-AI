






def pos_changer(current_pos,target_pos,num):
    
    num = str(num)
    
    hex = "0123456789ABCDEF"
    
    sum = 0
    
    
    for pos,i in enumerate(reversed(num)):
        sum += int(i) * (current_pos ** pos)
    


    remainder = ""
    
    while sum > 0:
        remainder += str(sum % target_pos)
        sum //= target_pos
    res = remainder[::-1]
    return int(res)

print(pos_changer(10,8,20))