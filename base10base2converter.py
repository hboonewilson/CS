#create a function that takes a number and a letter as an argument and converts 
#the number into the opposite base (2==>10) (10===>2)
def binaryTenConverter(num, base):
    #decide which way to convert
    if base.lower() == "b":
        #count length of binary string
        s_num = str(num)
        long = len(s_num)
        #iterate and creat a list of t/f for each place value
        t_f = []
        for i in range(0, long):
            #if zero, add false
            if s_num[i] == '0':
                t_f.append(False)
            #if one add True
            elif s_num[i] == '1':
                t_f.append(True)
        #return t_f
        #set long = to lenght of t_f list       
        long = len(t_f)
        print(long)
        #create three objects ans and counter
        ans = 0
        counter = 0
        for i in range(0, long):
            #set long to new length
            long = long - counter
            value = 2 ** long
            print(value)
            if t_f[i]:
                ans += value 
                counter += 1
            else:
                counter += 1
                pass 
        return ans