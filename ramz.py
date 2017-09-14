def digit_sum(ramz_digit):
    jam = 0
    for k in ramz_digit:
        jam += ramz_digit[k]
    return jam




def ramz_is_ok(ramz_digit):
    if  ramz_digit["sevom"]+ramz_digit["panjom"] == 14 and\
         ramz_digit["aval"]==(ramz_digit["dovom"]*2) - 1 and\
         ramz_digit["chaharom"]==ramz_digit["dovom"]+1 and\
         ramz_digit["dovom"]+ramz_digit["sevom"]== 10:
          if digit_sum(ramz_digit)==30:
              return True




for ramz in range(0,100000):
    #print (i)
    string_ramz=str(ramz).zfill(5)


    ramz_digit = {}
    ramz_digit["aval"]=int(string_ramz[0])
    ramz_digit["dovom"]=int(string_ramz[1])
    ramz_digit["sevom"]=int(string_ramz[2])
    ramz_digit["chaharom"]=int(string_ramz[3])
    ramz_digit["panjom"]=int(string_ramz[4])
    #print(ramz_digit)
    if ramz_is_ok (ramz_digit):
        print(ramz)
