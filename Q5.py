# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
# The Tower of Hanoi is a classic puzzle that involves moving a stack of disks from one peg to another with the help of a third peg, following a specific set of rules.
def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n - 1, source, auxiliary, destination)

        # Move the nth disk from source to destination peg
        print(f"Move disk {n} from {source} to {destination}")

        # Move the n-1 disks from auxiliary peg to destination peg
        tower_of_hanoi(n - 1, auxiliary, destination, source)

# Example usage
n = 3  # Number of disks
source_peg = "A"
destination_peg = "C"
auxiliary_peg = "B"

tower_of_hanoi(n, source_peg, destination_peg, auxiliary_peg)
