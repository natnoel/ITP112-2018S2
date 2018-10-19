result = []
while True:
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
    elif list[0] == 'append':
        result.append(int(list[1]))
    elif list[0] == 'sort':
        result.sort()
    elif list[0] == 'pop':
        result.pop()
    elif list[0] == 'reverse':
        result.reverse()
    elif list[0] == 'quit' or list[0] == 'end':
        break;
    else:
        print("Cannot understand command")