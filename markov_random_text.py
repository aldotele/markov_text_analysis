from markov.markov_analysis import markov_analysis

import sys, random


def markov_random_text(filename, n):
    """
    @param filename is the path to the file we want to perform the analysis on
    @param n is the prefix length (how many words there will be in a prefix)
    """
    
    # the return value of the markov analysis is a dictionary which maps prefixes of length n to suffix(es)
    d = markov_analysis(filename, n)
    # I use the beginning of the file as first prefix
    prefix = list(d)[0]
    output = prefix

    for i in range(len(d)):
        suffixes = d[prefix]
        suffix = random.choice(suffixes)   
        output += ' ' + suffix
        # the new prefix will esclude the first word and add the suffix
        prefix = prefix.split()[1:] + [suffix]
        prefix = ' '.join(prefix)

        # if a formed prefix does not exist, the function stops generating text, exiting the loop
        if prefix not in d:
            break
          
    return output


def main():
    if len(sys.argv) != 3:
        print('please enter 2 arguments from command line: a file.txt and a prefix length')
        quit()

    # the file name and the prefix length get passed from command line
    inf = sys.argv[1]
    prefix_length = sys.argv[2]

    inf_random_text = markov_random_text(inf, prefix_length)
    print(inf_random_text)

main()


