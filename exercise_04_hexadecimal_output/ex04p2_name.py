def name_triangle():
    name = input("Whats your name: ")

    for x in range(len(name)):
        print(name[:x + 1])


name_triangle()
