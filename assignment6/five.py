def sorthyphen(input):
    words = input.split("-")
    sorted_words = sorted(words)
    sorted_sequence = "-".join(sorted_words)
    print(sorted_sequence)

input = "green-red-yellow-black-white"
sorthyphen(input)