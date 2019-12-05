class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@combany.com'
    #raise pay of employee by x amount (x)
    def payRaise(self, x):
        self.pay += x
        print(f"Pay raised ${x}")
        print(f"Salary now ${self.pay}")

class Falcon9InSpace:
    def __init__(self, vel, mass):
        #vel = m/s
        self.vel = vel
        #mass = kg
        self.mass = mass
        #Thrust in Newtons
        self.thrust = 7_607_000
        
    #m-e-b = main engine burn
    def m_e_b(self, seconds):
        #find weight by multiplying mass by 9.8 (calling it newtons)
        newtons = mass * 9.8
        #calculate extra thrust (extra)
        extra = self.thrust - newtons
        #find acceleration by extra thrust / mass (acc)
        acc = extra / mass
        #new velocity is acceleration by the length of burn
        self.vel +=  (acc * seconds)
        
        