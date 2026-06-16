#Versi 1
a = 1

print("a\t b\t a ** b")
while a < 6:
	b = a + 1
	c = a ** b
	print(a, "\t", b, "\t", c)
	a += 1

#Versi 2
a = 1

print("a\tb\ta ** b")

for a in range(1, 6):
	b = a + 1
	c = a ** b

	print(f"{a}\t{b}\t{c}")