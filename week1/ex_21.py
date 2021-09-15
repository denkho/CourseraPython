n1, n2 = int(input()), int(input())

one = n1 // n2
two = n2 // n1

print((n1 * one + n2 * two) // (one + two))
