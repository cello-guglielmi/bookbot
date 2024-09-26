def main():
    file = 'books/frankenstein.txt'
    text = get_text(file)
    num_words = count_words(text)
    char_appearances = count_character_occurances(text)

    # >>> .items() returns a List of tuples, from a Dictionary key:value pairs 
    # >>> sorted() sorts a List alphabetically (if string) or numerically (if numbers)
    # >>> syntax: sorted(iterable, key=function, reverse=bool)
    # >>> dict() converts List back into a Dictionary

    sorted_dict = dict(sorted(char_appearances.items(), key=lambda item: item[1], reverse=True))

    print(f'--- Beginning report of {file} ---\n\n\
{num_words} total words found in the document.\n')
    for i in sorted_dict:
        print(f"The character '{i}' was found {sorted_dict[i]} times.")
    print('\n--- End of report ---')

'''
def count_character_occurances(text):
    lower_txt = text.lower()

    words = lower_txt.split() # >>> THOUGHT I HAD TO SPLIT TEXT INTO WORDS, AND WORDS INTO CHARS!
    char_list = []            # >>> YOU CAN JUST LOOP THROUGH CHARS IN A STRING! ✔
    char_count = []

    for word in words:
        l = list(word)
        char_list.extend(l)

    for char in char_list:
        num = text.count(char)
        char_count.append(num)

    char_dic = dict(zip(char_list, char_count))
    return char_dic
'''

def count_character_occurances(text):
    lower_txt = text.lower()
    char_dic = {}
    for x in lower_txt:
        if x.isalpha():          # >>> checks if char is a-z
            if x in char_dic:
                char_dic[x] += 1 # >>> YOU CAN DIRECTLY CREATE A KEY AND ASSIGN A VALUE! ✔
            else:
                char_dic[x] = 1
    return char_dic

def count_words(text):
    words = text.split()
    return len(words)

def get_text(file_path):
    with open(file_path) as f:
        return f.read()

if __name__ == '__main__':
    main()
