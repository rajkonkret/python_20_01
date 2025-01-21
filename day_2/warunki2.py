# python 3.10
# match case

lista = []
lang = input("Podaj znany Ci język programowania")

match lang.casefold().strip():
    case "python":
        lista.append("Python")
    case "java":
        lista.append("Java")
    case _:  # wartośc domyslna, odpowiednik else
        print("Nie znam takiego języka")

print(lista)
