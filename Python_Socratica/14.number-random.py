import random

# Display 10 random numbers from interval [0, 1)

for i in range(10):
    print(random.random())

# Generate random numbers from inteval [3, 7)

for i in range(10):
    print(random.uniform(4, 9))

# Generate a normal random number

for i in range(20):
    print(random.normalvariate(5,3))

# Generate random int like a frieze

for i in range(10):
    print(random.randint(1,6))

# Generate a random item from a list
outcomes = ["rock", "paper", "scissors"]

for i in range(20):
    print(random.choice(outcomes))