def main():
    f = open('resources/US_Senate_voting_data_109.txt')
    voting_dict, dem_set, rep_set = create_voting_dict(list(f))
    print("The senator that have the most similar votes with Chafee is ", end='')
    print(most_similar('Chafee', voting_dict))
    print("The senator that have the least similar votes with Santorum is ", end='')
    print(least_similar('Santorum', voting_dict))
    print("The senator with most similar votes comparing to the democratic average is ", end='')
    print(most_similar_to_set(dem_set, voting_dict))
    print("The senator with most similar votes comparing to the republican average is ", end='')
    print(most_similar_to_set(rep_set, voting_dict))

def create_voting_dict(strlist):
    vot_matrix = [vot_line.split() for vot_line in strlist]
    vot_dict = {vot_line[0]:tuple(int(x) for x in vot_line[3:]) for i, vot_line in enumerate(vot_matrix)}
    
    dem_set = set()
    rep_set = set()
    for vot_line in vot_matrix:
        if vot_line[1] == 'D':
            dem_set.add(vot_line[0])
        else:
            rep_set.add(vot_line[0])

    return vot_dict, dem_set, rep_set

def policy_compare(senA, senB, voting_dict):
    return sum([a*b for (a,b) in zip(voting_dict[senA], voting_dict[senB])])

def most_similar(senA, voting_dict):
    sim_sen, bgst_dot = ['Null', -len(voting_dict[senA])]
    for sen in voting_dict:
        if sen != senA:
            new_dot = policy_compare(senA, sen, voting_dict)
            if new_dot > bgst_dot:
                sim_sen, bgst_dot = sen, new_dot
    return sim_sen

def least_similar(senA, voting_dict):
    lst_sen, smlst_dot = ['Null', len(voting_dict[senA])]
    for sen in voting_dict:
        if sen != senA:
            new_dot = policy_compare(senA, sen, voting_dict)
            if new_dot < smlst_dot:
                lst_sen, smlst_dot = sen, new_dot
    return lst_sen

def find_average_similarity(senA, sen_set, voting_dict):
    accum = 0
    for senB in sen_set:
        accum += policy_compare(senA, senB, voting_dict)
    return (accum / len(sen_set))

def most_similar_to_set(sen_set, voting_dict):
    sim_sen, best_avg = ['Null', 0]
    for senA in voting_dict:
        avg = find_average_similarity(senA, sen_set, voting_dict)
        if avg > best_avg:
            best_avg = avg
            sim_sen = senA
    return sim_sen

if __name__ == '__main__':
    main()
