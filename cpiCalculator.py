def purchasePower(salaryadjust, cpix, cpiy ):
    '''This function takes in three arguments... 
    salaryadjust == the salary you'd like to adjust for another place/time's CPI
    cpix == cpi index of salaryadjust
    cpiy == cpi index of place/time you are adjusting for
    rounds to the nearest cent'''
    
    new_salary =  salaryadjust * (cpiy / cpix)
    return round(new_salary, 2)