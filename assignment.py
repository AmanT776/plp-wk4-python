filename = input('enter the name of a file: ')
try:
    file = open(filename,'r')
    data = file.read()
    print(data)
    modify = input('do you want to write(y/n): ')
    if modify == 'y':
        new_file = open(filename,'a')
        user_data = input('enter your text: ')
        modified_data = new_file.write(f"{user_data}\n")
        print(f"you wrote {data}")
except FileNotFoundError:
    print("file not found")
