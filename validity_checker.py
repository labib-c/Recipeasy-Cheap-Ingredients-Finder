from nltk.corpus import wordnet

def check_similarity(term, sorted_tuple_list):
    term_words = term.split()
    for i in range(len(sorted_tuple_list)):
        new_name = sorted_tuple_list[i][1].rsplit(',', 1)[0]  # remove last comma and beyond
        name_words = new_name.split()

        if len(name_words) >= len(term_words):
            counter = -(len(term_words))
            similarities = []
            while counter < 0:
                term_net = wordnet.synsets(term_words[counter])[0]
                name_net = wordnet.synsets(name_words[counter])[0]
                similarities.append(term_net.wup_similarity(name_net))
                counter = counter + 1
            if (sum(similarities)/(float(len(similarities)))) >= 0.80:
                return sorted_tuple_list[i]

    lower_term = term.lower()
    for i in range(len(sorted_tuple_list)):
        new_name = sorted_tuple_list[i][1].rsplit(',', 1)[0].lower()  # remove last comma and beyond
        if lower_term in new_name:
            return sorted_tuple_list[i]

    return sorted_tuple_list[0]




if __name__ == "__main__":
    tuple_list = [(1.2, "hello"), (1.2, "good good"), (1.443, "banana sauce"), (1.5, "banana, whattup")]
    print(check_similarity("apple sauce", tuple_list))






