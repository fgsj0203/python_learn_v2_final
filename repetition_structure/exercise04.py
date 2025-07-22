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

# Using function for equal solution


def growthing_population():
    first_population = 80000
    second_population = 200000
    first_growthing = 0.03
    second_growthing = 0.015
    counter_year = 0
    while first_population <= second_population:
        first_population = first_population + (first_population * first_growthing)
        second_population = second_population + (second_population * second_growthing)
        counter_year += 1

    print(
        "After %d years the population A with %.2f is bigger population B with %.2f "
        % counter_year,
        population_a,
        population_b,
    )
