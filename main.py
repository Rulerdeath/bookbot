
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        dict_list=[]
        print(f"There are {count_words(file_contents)} words")
        print (count_letters(file_contents))
        print(file_contents)

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
        if letter in letter_count:
            letter_count[letter] +=1
        else:
            letter_count[letter] = 1
    return letter_count


main()