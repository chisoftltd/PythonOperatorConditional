# Program by ChisoftMedia

# Python Arithmetic Operator

x = 10
y = 2 * x
z = (x == y)

print(z)

del z


z = (x**y)

print(z)


# Python Comparison/Relational Operators

z = (y//x)
print(z)

z = (x != y)

print(z)


z = (x != y)

print(z)


z = (x > y)

print(z)


z = (x < y)

print(z)


z = (x >= y)

print(z)


z = (x <= y)

print(z)


# Python Assignment Operators

x = 10
y = 2 * x
x += y

print(x)

x -= y

print(x)

x *= y

print(x)

x /= y

print(x)

x %= y

print(x)

x **= y

print(x)

x //= y

print(x)

# Python Logical Operators

x = True
y = False

print(x and y)
print(x or y)

# Conditional statement
a = 20
b = 40
if a == b:
    print("a is equal to b")

# Python Conditional Operators

del x, y, z

x = True
y = False

print(x and y)
print(x or y)

# Conditional statement
a = 40.5
b = 40
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

if a == b:
    print("a is equal to b")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")

value = int(input("Please enter a number : "))
if value < 100:
    if value > 50:
        print("Value is less than 100 but greater than 50")


score = float(input("Enter your score: "))
if score >= 70 and score <= 100:
    print("A")
elif score >= 60 and score <= 69:
    print("B")
elif score >= 50 and score <= 59:
    print("C")
elif score > 45 and score < 49:
    print("D")
