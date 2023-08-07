def find_pieces_in_bowl():
    for i in range(1, 200):
        if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
            return i

    return None

def main():
    result = find_pieces_in_bowl()

    if result is not None:
        print(f"The number of pieces in the bowl is: {result}")
    else:
        print("The number of pieces in the bowl cannot be determined with the given information.")

if __name__ == "__main__":
    main()
