class Rocket:
	def __init__(self , mass_kg , rocket_force_n , velocity_start , velocity_end):
		self.kg = mass_kg
		self.w = ''
		self.r_f = rocket_force_n
		#adjusted force of rocekt in N
		self.a_f = ''
		#acceleration in m/s
		self.acceleration = ''
		self.v_s = velocity_start
		self.v_e = velocity_end

	def weight(self):
		weight = self.kg * 9.8
		print(weight)
		self.w = weight


	def actual_force(self):
		adjusted_force = self.r_f - self.w
		print(adjusted_force)
		self.a_f = adjusted_force

	def find_acceleration(self):
		acceleration = (self.a_f / self.kg)
		print(acceleration)
		self.acceleration = acceleration

	def how_many_seconds(self):
		if self.v_s > self.v_e:
			velocity_change = self.v_s - self.v_e
		elif self.v_e > self.v_s:
			velocity_change = self.v_e - self.v_s
		else:
			print("No change needed!")

		seconds = (velocity_change / self.acceleration)
		print(f"Burn for {seconds} seconds")

kg = float(input("What is the mass of your rocekt: "))
rocket_force_n = float(input("How much force does it provide: "))
velocity_start = float(input("What is the start of its velocity: "))
velocity_end = float(input("What is the end velocity you'd like: "))


print("\nWelcome astronauts! Tell us about your rocekt and we'll tell you how long to light it for!")
my_rocet = Rocket(kg, rocket_force_n, velocity_start , velocity_end)
my_rocet.weight()
my_rocet.actual_force()
my_rocet.find_acceleration()
my_rocet.how_many_seconds()

