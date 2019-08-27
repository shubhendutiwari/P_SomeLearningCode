"""Write a function find_longest_word() that takes a list of words and returns the length of the longest one"""

def find_longest_word(words):
    i = 0
    for word in words:
        if len(word)> i:
            i=len(word)
        else:
            continue
    return i

if __name__ == "__main__":
    words = ['abv', 'try me', 'test']
    print(find_longest_word(words))