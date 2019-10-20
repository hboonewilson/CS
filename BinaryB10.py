def binaryToTen(value, base):
    '''Transform binary/base10 string to the opposite. Appropriate base values 
    for binary... (binary) for base10...(ten) All numbers entered as numbers not
    strings.'''
    #decide which base it is
    if base == 'binary':
        value = str(value)
        #create place for binary place values
        binarylis = []
        #iterate through place value
        for i in range(0, len(value)):
            #turn list around and subract one more to correctly get place of bit 
            place = len(value) - i - 1
            #get the place value
            placevalue = 2 ** place
            binarylis.append(placevalue)
        retvalue = 0
        #iterate through value and if value is 1 add the same value into 
        #return value (retvalue) 
        for i in range(0, len(value)):
            if value[i] == '0':
                pass
            elif value[i] == '1':
                retvalue += binarylis[i]
            else:
                return 'Not a binary string'
        return retvalue
    if base == 'ten':
        place = 0
        baselis = []
        counter = 0
        while place * 2 <= value:
            place = 2 ** counter
            baselis.append(place)
            counter += 1
        binaryret = ''
        for i in range(0, len(baselis)):
            number = baselis[len(baselis) - i - 1]
            if value >= number:
                value = value - number
                binaryret += '1'
            else:
                binaryret += '0'
        return binaryret
            
            