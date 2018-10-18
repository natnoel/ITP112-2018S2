count = int(input('Enter number of steps: '))
result = []
for i in range(count):
    command = input('Enter command: ')
    list = command.split()
    if list[0] == 'insert':
        result.insert(int(list[1]), int(list[2]))
    elif list[0] == 'print':
        print(result)
    elif list[0] == 'remove':
        item = int(list[1])
        if item in result:
            result.remove(item)
        else:
            print(f"Cannot find {item}")