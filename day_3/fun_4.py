def all_args(*args, **kwargs):
    print(f"{args=}")
    print(f"{kwargs=}")


all_args()
# args=() # krotka - argumenty pozycyjne
# kwargs={}  słownik - argumenty nazwane
all_args(123, a=10, b=20, c=30)
# args=(123,)
# kwargs={'a': 10, 'b': 20, 'c': 30}
all_args(123, 4556, 67, a=10, b=20, c=30, name="Radek")
# args=(123, 4556, 67)
# kwargs={'a': 10, 'b': 20, 'c': 30, 'name': 'Radek'}
