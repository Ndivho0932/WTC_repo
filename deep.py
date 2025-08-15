def main():
    user = input("what is the answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    if user == "42":
            print("Yes")
    elif user == "forty two":
            print("Yes")
    elif user == "forty-two":
            print("Yes")
    else:
        print("No")

main()
