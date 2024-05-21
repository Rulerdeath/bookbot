
def main():
    print("-- Begin report of Frankenstein --")
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        dict_list=[]
        print(f"There are {count_words(file_contents)} words"), print()
        sort_letters = count_letters(file_contents)
        sort_times(sort_letters)
        print("-- End of report --")

def count_words(file_contents):
    words=file_contents.split()
    total_amount_words = 0
    for word in words:
        total_amount_words += 1
    return total_amount_words

def count_letters(file_contents):
    letter_count = {}
    lwrcase_txt = file_contents.lower()
    for letter in lwrcase_txt:
        if letter.isalpha(): # Checks if the letter is part of the alphabet and not another character
                if letter in letter_count:
                    letter_count[letter] +=1
                else:
                    letter_count[letter] = 1
    return letter_count

def sort_times(sort_letters):
    sort_letters = list(sort_letters.items()) # Turns the characters' dictionary into a list of tuples
    sort_letters.sort(key=lambda tuple: tuple[1], reverse=True) # Sorts the list by their amount of occurrences
    for tuple in sort_letters:
        print(f"The character {tuple[0]} was found {tuple[1]} times")

main()