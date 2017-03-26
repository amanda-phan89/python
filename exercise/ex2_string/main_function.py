def main():
    str_input = ""
    while len(str_input.strip(" ")) <= 0:
        str_input = input('Please enter your sentence: ')

    str_list = str_input.strip(" ").split(" ")
    str_list.sort()
    print(' '.join(str_list))

if __name__ == "__main__":
   main()