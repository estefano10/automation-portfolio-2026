def two_fer(name="you"):
    return f"One for {name}, one for me."

x = two_fer("Estefano")
y = two_fer()
print(x)
print(y)