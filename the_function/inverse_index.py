def main():
    f = open('resources/stories_big.txt')
    strlist = list(f)
    print(makeInverseIndex(strlist))

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

if __name__ == '__main__':
    main()
