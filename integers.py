def process_integers():
    try:
        with open("integers_txt", "r") as file:
            content = file.read().split()

        numbers = [int(num) for num in content]

        even_squares = []
        odd_cubes = []

        for num in numbers:
            if num % 2 == 0:
                even_squares.append(num ** 2)
            else:
                odd_cubes.append(num ** 3)
