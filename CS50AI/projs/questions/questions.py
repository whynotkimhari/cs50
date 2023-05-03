import nltk
import sys
import string
import os
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    
    file_idfs = compute_idfs(file_words)
    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dir_list = os.listdir(directory)
    paths = [os.path.join(directory, file) for file in dir_list]
    dic = {}

    for path, name in zip(paths, dir_list):
        with open(path, 'r', encoding='utf8') as f:
            s = f.read()
            dic.update({name : s})

    return dic


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    stopwords = nltk.corpus.stopwords.words("english")
    document = document.lower()
    prefix = []
    fixed = []

    for word in document.split(' '):
        w = nltk.RegexpTokenizer(r"\w+").tokenize(word)
        for i in w:
            prefix.append(i)

    for _ in prefix:
        if _ in stopwords:
            continue
        else:
            fixed.append(_)
    fixed.sort()
    return fixed


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    resulting_dic = {}
    for file in documents:
        for word in documents[file]:
            if word in resulting_dic:
                continue
            else:
                count = 0
                for _ in documents:
                    if word in documents[_]:
                        count += 1
                idf = math.log(len(documents) / count)
                resulting_dic.update({word : idf})
            
    return resulting_dic


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    dict_for_computing = {
        name: 0
        for name in files.keys()
    }
    output_list = []

    for name in dict_for_computing:
        for word in query:
            idf = 0
            for _ in files[name]:
                if _ == word:
                    idf += 1
            tfidf = idf * idfs[word]
            dict_for_computing[name] += tfidf

    list_for_computing = [(name, dict_for_computing[name]) for name in dict_for_computing]
    list_for_computing.sort(key=lambda x : x[1], reverse=True)
    
    for x in list_for_computing:
        output_list.append(x[0])
        
    return output_list[:n]


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    dict_for_computing = {
        sentence: 0
        for sentence in sentences.keys()
    }
    
    for sentence in dict_for_computing:
        for word in query:
            if word in sentences[sentence]:
                dict_for_computing[sentence] += idfs[word]

    list_for_computing = [(sentence, dict_for_computing[sentence]) for sentence in dict_for_computing]
    list_for_computing.sort(key=lambda x : x[1], reverse=True)

    # If max of list the largest element
    if list_for_computing[0][1] > list_for_computing[1][1]:
        output_list = []
        for _ in list_for_computing:
            output_list.append(_[0])

        return output_list[:n]
    
    # If exist some numbers of element that has the same value of max element
    elif list_for_computing[0][1] == list_for_computing[1][1]:
        max_element = list_for_computing[0][1]
        considering_elements = []
        for _ in list_for_computing:
            if _[1] == max_element:
                considering_elements.append(_)

        zz = []
        for element in considering_elements:
            density = 0
            for _ in sentences[element[0]]:
                if _ in query:
                    density += 1
            d = density / len(sentences[element[0]])
            zz.append((element[0], element[1], d))

        zz.sort(key=lambda x : x[2], reverse=True)

        output_list = []
        for xx in zz:
            output_list.append(xx[0])
            
        return output_list[:n]

if __name__ == "__main__":
    main()
