"""Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words"""



def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths
     
if __name__ == "__main__":
    words = ['abv', 'try me', 'test']
    print(map_to_lengths_for(words))