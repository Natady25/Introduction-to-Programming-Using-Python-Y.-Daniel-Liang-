# Manual
print("1.4 Print a table")
print("a       a^2       a^3")
print("1       1         1  ")
print("2       4         8  ")
print("3       9         27 ")
print("4       16        64 ")
print("\t")

# Looping
a = 1

print("a\ta^2\ta^3")
while a < 5:
	b = a ** 2
	c = a ** 3
	print(int(a), "\t", int(b), "\t", int(c))
	a += 1