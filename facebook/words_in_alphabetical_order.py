# Write a function that takes an array of words and an array of letters
# and determines if the words are in the "alphabetical" order based on the array of letters

# input: words = ["cca", "cc", "cba"]
#        alphabet = ["c", "b", "a", "t"]
# output: False
def isAlphabetical(words, alphabet):
    hash_map = dict()
    for idx, x in enumerate(alphabet):
        hash_map[x] = idx
    print(hash_map)

    curr_idx = 0
    while curr_idx < len(words) - 1:
        curr_word = words[curr_idx]
        next_word = words[curr_idx + 1]

        max_word_length = min(len(curr_word), len(next_word))
        for i in range(0, max_word_length):
            curr_char = curr_word[i]
            next_char = next_word[i]

            if hash_map[curr_char] > hash_map[next_char]:
                print(False)
                return False

        if len(curr_word) > len(next_word):
            print(False)
            return False

        curr_idx += 1

    print(True)


# correct order: cc => cca => cba
isAlphabetical(["cca", "cca", "cba"], ["c", "b", "a", "t"])
