def main():
    f = open('resources/stories_big.txt')
    strlist = list(f)
    inverseIndex = makeInverseIndex(strlist)
    while True:
        resp = input("Do you want to do a orSearch or a andSearch? (x to quit) ").lower()
        if resp == 'x':
            print("Thank You!")
            break
        elif resp != 'or' and resp != 'orsearch' and resp != 'and' and resp != 'andsearch':
            print("I didn't understand you, asking again...")
            continue
        querry = input("Enter your search querry: ").split()
        if resp == 'or' or resp == 'orsearch':
            search_set = orSearch(inverseIndex, querry)
        else:
            search_set = andSearch(inverseIndex, querry)
        print("The documents where you can find what you want are...")
        print(search_set)

def makeInverseIndex(strlist):
    doc_word_set = []
    for doc in strlist:
        doc_word_set.append(set(doc.split()))
    inv_index = {word:{0} for word in doc_word_set[0]}
    for i, doc in enumerate(doc_word_set[1:]):
        for word in doc:
            if word in inv_index:
                inv_index[word].add(i+1)
            else:
                inv_index[word] = {i+1}
    return inv_index

def orSearch(inverseIndex, querry):
    search_word_arr = []
    for word in querry:
        if word in inverseIndex:
            search_word_arr.append(inverseIndex[word])
    return set.union(*search_word_arr)

def andSearch(inverseIndex, querry):
    search_word_arr = []
    for word in querry:
        if word in inverseIndex:
            search_word_arr.append(inverseIndex[word])
        else:
            print("WARNING: '%s' doesn't seems to exist in dict. Ignoring it." %(word))
    return set.intersection(*search_word_arr)

if __name__ == '__main__':
    main()
