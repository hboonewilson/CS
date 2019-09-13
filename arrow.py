def arrow_KE(arrow_weight , fps):
	"""
	Calculate an Arrows KE in foot pounds from it's weight in grains and it's
	fps. According to the bow's KE , the function will also tell you the biggest
	type of game you can ethically harvest.
	"""
	ke = (fps**2) * arrow_weight / 450_240
	print(f"{ke} ft-lbs")
	if ke < 25:
		print("You can hunt small game only.")
	elif 25 < ke < 40:
		print("You can kill pronghorn and deer.")

print("Enter info about your bow and we'll tell you your kenetic energy")

arrow_weight = int(input('Arrow weight (grains): '))
fps = int(input("Bow speed (feet per second): "))

arrow_KE(arrow_weight , fps)