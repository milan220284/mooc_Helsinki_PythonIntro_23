# Write your solution here
def find_words(search_term: str):
    words = []
    with open("words.txt") as new_file:
        for line in new_file:
            words.append(line.strip())
    
    result = [] 

    if not ('.' in search_term) and not ('*' in search_term):
        for word in words:
            if search_term == word:
                result.append(word)
    elif '*' in search_term:
        if '*' == search_term[0]:
            for word in words:
                if word.endswith(search_term[1:]):
                    result.append(word)
        else:
            for word in words:
                if word.startswith(search_term[:len(search_term)-1]):
                    result.append(word)
    elif '.' in search_term:
        search_term_list = list(search_term)
        for word in words:
            if len(word) == len(search_term):
                match = True
                for i in range(len(word)):
                    if search_term[i] != '.':
                        match = match and (search_term[i] == word[i])
                if match:
                    result.append(word)

        
    return result

