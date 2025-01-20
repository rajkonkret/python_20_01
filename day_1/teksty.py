tekst = "Wiataj Świecie"
print(tekst)
print(type(tekst))
# Wiatj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
# zamienic tekst na duże litery
print(tekst.upper())  # WIATAJ ŚWIECIE
tekst_upper = tekst.upper()
print(tekst_upper)  # WIATJ ŚWIECIE
print(tekst)  # Wiataj Świecie
