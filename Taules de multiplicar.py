def print_multiplication_tables():
    for i in range(2, 10):
        print(f"Multiplication table for {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
        print()  # Add an empty line between tables

print_multiplication_tables()
