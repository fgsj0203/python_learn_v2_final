population_a = 80000
population_b = 200000
growthing_a = 0.03
growthing_b = 0.015
counter_year = 0

while population_a <= population_b:
    population_a = population_a + (population_a * growthing_a)
    population_b = population_b + (population_b * growthing_b)
    counter_year += 1

print("The final growthing population A is %.2f" % population_a)
print("The final growthing population B is %.2f" % population_b)
print("After %d years the population A is bigger population B" % counter_year)
