import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # calculate how many links are there in the given page
    index = 0
    index_list = []
    for key in corpus:
        index_list.append((key, index))
        index += 1
    check = 0
    for x in index_list:
        if x[0] == page:
            check = x[1]
    
    elements = [link for link in corpus.values()]
    s = len(elements[check])
    
    dict_ = dict()
    if s > 0:
        prob_d = (damping_factor) / s
        prob_1_d = (1 - damping_factor) / len(corpus)
        for key in corpus:
            dict_[key] = prob_1_d
        for key in elements[check]:
            dict_[key] += prob_d
    
    else:
        prob = 1 / len(corpus)
        for key in corpus:
            dict_[key] = prob
    return dict_


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dict_ = dict()
    for key in corpus:
        dict_[key] = 0
    starting_page = random.choice(list(corpus))
    current_page = starting_page
    
    for i in range(n):
        dict_[current_page] += 1
        model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices([value for value in model], weights=[value for value in model.values()])[0]
    for key in dict_:
        dict_[key] /= n
    return dict_


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    dict_ = dict()
    N = len(corpus)
    # All starting values is 1 / N
    for key in corpus:
        dict_[key] = 1 / N
    pre_dict_ = dict()
    for key in corpus:
        pre_dict_[key] = 0
    # For each page P, count how many links are there on P
    while check_stop(pre_dict_, dict_) == False:
        pre_dict_ = dict_.copy()
        for page in corpus:
            sum = 0
            linkstoPageP = []
            for key in corpus:
                for link in corpus[key]:
                    if link == page:
                        linkstoPageP.append(key)
            if len(linkstoPageP) != 0:
                for link in linkstoPageP:
                    sum += pre_dict_[link] / len(corpus[link])
            else:
                for key in corpus:
                    sum += pre_dict_[key] / len(corpus[key])

            dict_[page] = (1 - damping_factor) / N + damping_factor * sum

    return dict_

def check_stop(pre_dict_, dict_):
    list1 = list(pre_dict_.values())
    list2 = list(dict_.values())
    c = 0
    for i in range(len(list1)):
        if abs(list1[i] - list2[i]) > 0.001:
            c += 1
            break
    if c == 0:
        return True
    return False

if __name__ == "__main__":
    main()
