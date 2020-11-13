# Markov Text Analysis


### Introduction
In this project a Markov Chain, built upon an existing file.txt, is used in order to build a random text generator. 
The random text generator generates the text by randomly and continuously picking one suffix for each prefix inside 
the Markov Chain.
Check this  [detailed article](https://blog.rinatussenov.com/text-analysis-markov-chains-and-bible-quotes-generator-fd0fa09ced20) for further knowledge.

### Scripts
- *markov_random_text.py* is the script which actually generates the random text based on a Markov Analysis.
- *markov_analysis.py* is a module inside the *markov* package, and it is where the actual Markov Analysis is performed.

Inside *markov_random_text.py*, a function called `markov_random_text` is used to generate the random text. 
The function accepts two parameters: `filename` is the name of the file.txt based on which the random generation 
will come from, and  `n` which is the prefix length. The prefix length is the number of words that have to be present
in each Markov Chain prefix. 
The `markov_random_text`, inside its body, will invoke the  `markov_analysis` function and passing the same two 
arguments to it (the name of the file and the prefix length). This last function will perform the analysis and return
a dictionary where each key is a prefix (with n words inside it) and its value is the list of the possible suffixes coming
after that prefix occurrence (it might be one suffix or more).
The higher is n, the lower is the chance to encounter multiple suffixes for the same prefix, since the prefix will be closer
to a sentence than to a word/expression. On the oppositve, if the prefix length is one word, it is likely to encounter many
prefixes with multiple suffix possibilities.
Therefore, the higher is n, the more similar the random text will be to the original text.

### How to Launch
Both *markov_random_text.py* and *markov_analysis.py* can be launched through command line by passing the name of the file.txt
and the prefix length as parameters. For example typing *python markov_analysis.py filename.txt 3* will generate a random text
based on a 3-words-prefix Markov Analysis being performed on a file called *filename.txt*.


### Output
When launching the *markov_random_text.py*, the output will be a random text, generated upon an originary text upon which
a Markov Analysis was performed.
If launching *markov_analysis.py* only, the program will return the Markov Chain of the original file.txt, without 
generating a new random text.