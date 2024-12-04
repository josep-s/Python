def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(first='Geeks', second='for', third='Geeks')
# Resultat:
# first: Geeks
# second: for
# third: Geeks
