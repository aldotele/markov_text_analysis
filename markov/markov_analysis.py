
import sys


"""
- the markov analysis function returns a dicitionary which maps from prefixes of length n to a list of suffix(es)
- each word together with its (n-1) following words will form a prefix, for a total of n words in the same prefix
- the suffix of a specific prefix is the single word which follows the last word of that prefix
- all possible suffixes of the same prefix occurrence will form a list which is mapped to that specific prefix in the key-value pair
"""

def markov_analysis(filename, n):
    """
    @param filename is the path to the file we want to perform the analysis on
    @param n is the prefix length (how many words there will be in a prefix)
    """
    n = int(n)
    if n < 1:
        raise ValueError('the prefix length must be a positive integer')
    
    # d will store all prefix-suffix(es) key-value pairs
    d = {}

    # opening file and extracting all the words    
    inf = open(filename, 'r')
    filestring = inf.read()
    words = filestring.split()

    # a loop will start at the first word and stop at the word which preceeds the n-to-last word
    # because that will be the last chance to create BOTH a n-words-prefix mapped to the last suffix
    # the index i will always be the index of the current (looped) word
    i = 0
    for word in words[:-n]:
        # the prefix will always start with the current word
        prefix = word
        # j is used to add consecutive words in the prefix. In case of a single-word prefix, j will always stay zero (no more words added)
        j = 0
        # after word at index i, the (n-1) following words  will be added to the prefix
        for j in range(1, n):
            prefix += ' ' + words[i + j]

        # the suffix is the word that follows the last word of the prefix
        suffix = words[i+j+1]        
        # each prefix is added as a key in the dictionary with the suffix being its value
        if prefix not in d:
            d[prefix] = [suffix]
        else:
            # if the prefix already exists as a key, the suffix will be added among its values (if it is not already there)
            if suffix not in d[prefix]:
                d[prefix].append(suffix)
        i += 1

    inf.close()

    return d


def main():
    if len(sys.argv) != 3:
        print('please enter 2 more valid arguments by command line: file.txt and prefix length')
        quit()
    # the name of the file and the prefix length get passed from command line
    inf = sys.argv[1]
    prefix_length = sys.argv[2]
    inf_analysis = markov_analysis(inf, prefix_length)
    print(inf_analysis)

    # printing only the prefixes with more than one suffix
    """
    for key in my_analysis:
        if len(my_analysis[key]) > 1:
            print(key, my_analysis[key])
    """
    
if __name__ == '__main__':
    main()
