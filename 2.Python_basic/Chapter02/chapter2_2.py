def timeconvert(second):
    minutes=0
    while second>60:
        second=second-60
        minutes=minutes+1
    return str(minutes)+":"+str(second)
    #return minutes+":"+
print(timeconvert(200))
#No.2===========================================
def timeconvert2(second2):
    min_time=60
    divide_times=divmod(second2,min_time)  #  (xx, di) return #(x//y,x%y)
    returnstr_="{}:{}".format(divide_times[0],divide_times[1])
    #return divide_times[0],divide_times[1]
    return returnstr_
print(timeconvert2(323))