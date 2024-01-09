class SimpleRandomGenerator:
    def __init__(self, seed=12345):
        self.state = seed

    def generate(self):
        # LCG parameters (a, c, m)
        a = 1664525
        c = 1013904223
        m = 2**32

        # Update the state using LCG formula
        self.state = (a * self.state + c) % m

        # Return a normalized random value between 0 and 1
        return self.state / m

# Create an instance of the random number generator
random_generator = SimpleRandomGenerator()

# Generate and print 5 random numbers
for _ in range(5):
    random_number = random_generator.generate()
    print(random_number)
