while True:
    name = input()
    if any(char.isdigit() for char in name):
        break
        