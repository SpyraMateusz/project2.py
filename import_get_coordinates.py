def get_coordinates():
    try:
        x, y = map(int, input("Enter coordinates (row col): ").split())
        return x, y
    except ValueError:
        print("Invalid input. Please enter two numbers separated by a space.")
        return get_coordinates()