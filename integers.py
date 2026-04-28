def process_integers():
    try:
        with open("integers.txt", "r") as file:
            content = file.read().split()

        numbers = [int(num) for num in content]

        even_squares = []
        odd_cubes = []

        for num in numbers:
            if num % 2 == 0:
                even_squares.append(num ** 2)
            else:
                odd_cubes.append(num ** 3)

        with open("double.txt", "w") as file:
            for value in even_squares:
                file.write(str(value) + "\n")


        with open("triple.txt", "w") as file:
            for value in odd_cubes:
                file.write(str(value) + "\n")

        print("Files created successfully: double.txt and triple.txt")

    except FileNotFoundError:
        print("Error: integers.txt not found.")
    except ValueError:
        print("Error: Make sure integers.txt contains only valid integers.")

process_integers()