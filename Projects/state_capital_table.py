import sys

# Initialize empty lists for states and capitals
states = []
capitals = []

# Take user input for states and capitals
states.append(input("Enter the name of the state you wish: "))
capitals.append(input("Enter the capital of the state: "))

# Process command-line arguments
for arg in sys.argv[1:]:
    try:
        state, capital = arg.split()
        states.append(state)
        capitals.append(capital)
    except ValueError:
        print(f"Invalid input: '{arg}'. Please provide state and capital separated by a space.")
        sys.exit(1)

# Print the state and capital table
print(f"{'State':<20} {'Capital':<20}")
print("-" * 40)
for state, capital in zip(states, capitals):
    print(f"{state:<20} {capital:<20}")
