def word_count(my_file):
    word_dict = {}
    file_name = open(my_file)
    for line in file_name:
        line = line.rstrip()
        word_list  = line.split(" ")
        for word in word_list:
            word_dict[word] = word_dict.get(word, 0)+1
    file_name.close()
    return word_dict
 

def print_count(records):
    """ Prints word count in a readable format """
    for words, counts in records.iteritems():
        print "{} {}".format(words, counts)

parse_dict = word_count("twain.txt")
print_count(parse_dict)        
