import random

compartments = {chr(i): random.randint(0, 100) for i in range(ord('A'), ord('G') + 1)}

# Point a
min_compartment = min(compartments, key=compartments.get)
min_load = compartments[min_compartment]
print(f"Minimum load: compartments {min_compartment} with workload {min_load}")

# Point b
compartments["H"] = 0
print("Added an empty compartment 'H' with a load of 0")

# Point c
random_compartment = random.choice(list(compartments.items()))
separated_compartment = {random_compartment[0]: random_compartment[1]}
print(f"Randomly selected compartment: {separated_compartment}")

# Point d
is_e_present = "E" in compartments
print(f"Compartment E remained in dictionary" if is_e_present else "Compartment E is not left in the dictionary")