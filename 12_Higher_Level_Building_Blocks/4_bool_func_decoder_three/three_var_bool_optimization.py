def three_var_bool_optimization (f_minterms):
    product_term = [
            "a'b'c'",
            "a'b'c",
            "a'bc'",
            "a'bc",
            "ab'c'",
            "ab'c",
            "abc'",
            "abc"
            ]
    
    list_terms = []
    for i in range(len(f_minterms)):
        list_terms.append(product_term[f_minterms[i]])

    res = []
    combined = []
    original = []
    c_minterms = []
    loop_max = len(f_minterms)
    i = 0
    while i < loop_max:
        termi = f_minterms[i]
        for j in range(i+1, len(f_minterms)):
            termj = f_minterms[j]
            diff = termi^termj
            match diff:
                case 1:
                    ind = list_terms[i].find("c")
                    new_term = list_terms[i][:ind]
                    res.append(new_term)
                    combined.append(list_terms[i])
                    combined.append(list_terms[j])
                    c_minterms.append((f_minterms[i], f_minterms[j]))
                    del list_terms[j]
                    del f_minterms[j]
                    loop_max -=1
                    break
                case 2:
                    ind = list_terms[i].find("b'")
                    offset = 2
                    if ind == -1:
                        ind = list_terms[i].find("b")
                        offset = 1
                    new_term = list_terms[i][:ind] + list_terms[i][ind+offset:]
                    res.append(new_term)
                    combined.append(list_terms[i])
                    combined.append(list_terms[j])
                    c_minterms.append((f_minterms[i], f_minterms[j]))
                    del list_terms[j]
                    del f_minterms[j]
                    loop_max-=1
                    break
                case 4:
                    ind = list_terms[i].find("a'")
                    offset = 2
                    if ind == -1:
                        offset = 1
                    new_term = list_terms[i][offset:]
                    res.append(new_term)
                    combined.append(list_terms[i])
                    combined.append(list_terms[j])
                    c_minterms.append((f_minterms[i], f_minterms[j]))
                    del list_terms[j]
                    del f_minterms[j]
                    loop_max-=1
                    break
            if j == (len(f_minterms)-1):
                res.append(list_terms[i])
                original.append(list_terms[i])
                c_minterms.append((None, f_minterms[i]))
        i+=1
    if ((list_terms[len(list_terms)-1]) not in combined) and ((list_terms[len(list_terms)-1]) not in res):
        res.append(list_terms[len(list_terms)-1])
        c_minterms.append((None, f_minterms[len(list_terms)-1]))

    # aAlone = [4,5,6,7]
    # anotAlone = [0,1,2,3]
    # bAlone = [2,3,6,7]
    # bnotAlone = [0,1,4,5]
    # cAlone = [1,3,5,7]
    # cnotAlone = [0,2,4,6]

    l_minterms = []
    i = 0
    ans = []
    l_minterms= []
    loop_max = len(c_minterms)
    while i < loop_max:
        (termi1, termi2) = c_minterms[i]
        if termi1 is None:
            ans.append(res[i])
            l_minterms.append((c_minterms[i]))
            i+=1
            continue
        flag = False
        for j in range(i+1, len(c_minterms)):
            (termj1, termj2) = c_minterms[j]
            if (termj1 is None):
                continue
            flag = True
            min_list = [termi1, termi2, termj1, termj2]
            match min_list:
                case [4,5,6,7]:
                    ans.append("a")
                    combined.append(res[i])
                    combined.append(res[j])
                    l_minterms.append((c_minterms[i], c_minterms[j]))
                    del res[j]
                    del c_minterms[j]
                    loop_max -=1
                    break
                case [0,1,2,3]:
                    ans.append("a'")
                    combined.append(res[i])
                    combined.append(res[j])
                    l_minterms.append((c_minterms[i], c_minterms[j]))
                    del res[j]
                    del c_minterms[j]
                    loop_max -=1
                    break
                case [2,3,6,7]:
                    ans.append("b")
                    combined.append(res[i])
                    combined.append(res[j])
                    l_minterms.append((c_minterms[i], c_minterms[j]))
                    del res[j]
                    del c_minterms[j]
                    loop_max -=1
                    break
                case [0,1,4,5]:
                    ans.append("b'")
                    combined.append(res[i])
                    combined.append(res[j])
                    l_minterms.append((c_minterms[i], c_minterms[j]))
                    del res[j]
                    del c_minterms[j]
                    loop_max -=1
                    break
                case [1,3,5,7]:
                    ans.append("c")
                    combined.append(res[i])
                    combined.append(res[j])
                    l_minterms.append((c_minterms[i], c_minterms[j]))
                    del res[j]
                    del c_minterms[j]
                    loop_max -=1
                    break
                case [0,2,4,6]:
                    ans.append("c'")
                    combined.append(res[i])
                    combined.append(res[j])
                    l_minterms.append((c_minterms[i], c_minterms[j]))
                    del res[j]
                    del c_minterms[j]
                    loop_max -=1
                    break
                case _:
                    flag = False
                    break
        if flag == False:
            ans.append(res[i])
        i+=1
    return (ans)

# # # EXAMPLE USE
# import random
# product_term = [
#             "a'b'c'",
#             "a'b'c",
#             "a'bc'",
#             "a'bc",
#             "ab'c'",
#             "ab'c",
#             "abc'",
#             "abc"
#             ]

# num_minterms = random.randint(3,5)
# mt = random.sample( range(8), num_minterms )
# print(f"Minterms: {mt}")
# terms = [product_term[i] for i in mt] 
# print(f"Bool: {terms}")
# print(three_var_bool_optimization(mt))