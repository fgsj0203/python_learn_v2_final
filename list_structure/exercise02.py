def list_reverse_numbers():
    list_numbers = []
    for x in range(0, 5):
        number = int(input())
        list_numbers.append(number)
    print("List in order original: ", list_numbers)
    print("List with reverse order: ", list_numbers[::-1])

list_reverse_numbers()
