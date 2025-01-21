# działania z plikami
# context manager do usprawniania pracy z plikami
# with - cm w pythonie
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding="utf-8") as f:
    f.write("Powitanie\n")

with open("test.log", "w", encoding="utf-8") as f:
    f.write("Kolejne\n")

# dodanie do istniejącego pliku
with open("test.log", "a", encoding="utf-8") as f:
    f.write("Kolejne\n")
    f.write("Kolejne\n")
    f.write("Kolejne\n")
    f.write("Jescze jedno\n")
    f.write("Dośdane\n")

with open("test.log", "r", encoding="utf-8") as f:
    dane = f.read()
print(dane)
# Kolejne
# Kolejne
# Kolejne
# Kolejne
# Jescze jedno
