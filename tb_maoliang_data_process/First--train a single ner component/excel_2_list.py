import xlrd


def read_data_from_xlsx():

    a = xlrd.open_workbook('aning(1).xlsx')
    table = a.sheet_by_index(0) #通过索引顺序获取,0表示第一张表
    train_words = [table.cell(i,ord('A')-ord('A')).value for i in range(0, 5060)]
    train_label=[table.cell(i,ord('A')-ord('B')).value for i in range(0, 5060)]
    valid_words = [table.cell(i,ord('A')-ord('A')).value for i in range(5060, 8441)]
    valid_label=[table.cell(i,ord('A')-ord('B')).value for i in range(5060, 8441)]
    test_words = [table.cell(i,ord('A')-ord('A')).value for i in range(8441, 11770)]
    test_label=[table.cell(i,ord('A')-ord('B')).value for i in range(8441, 11770)]



    ############################################################################
    list(enumerate(train_words))
    a2 = [i for i, x in enumerate(train_words) if x == ' ']
    # print(a2)
    # print(range(len(a2)))
    train_words_list =[train_words[0:86]]
    # print(train_words_list)
    for j in range(len(a2)):
        if j + 1 >= len(a2):
            break;
        # print(a2[j+1])
        a3=train_words[a2[j]+1 :a2[j+1]]
        train_words_list.append(a3)
    # print(train_words_list)

    train_label_list =[train_label[0:86]]
    for k in range(len(a2)):
        if k+1 >= len(a2):
            break;
        b3=train_label[a2[k]+1:a2[k+1]]
        train_label_list.append(b3)
    # print("len(train_label_list)")
    # print(len(train_label_list))

    tuple_train=[]
    for i in range(len(train_words_list)):
        tuple=(train_words_list[i],train_label_list[i])
        tuple_train.append(tuple)
    # print(tuple_train)




    ####################################################################3

    list(enumerate(valid_words))
    m = [i for i, x in enumerate(valid_words) if x == ' ']
    # print(m)
    valid_words_list =[valid_words[0:42]]
    for j in range(len(m)):
        if j + 1 >= len(m):
            break;
        mm=valid_words[m[j]+1 :m[j+1]]
        valid_words_list.append(mm)
    # print(len(valid_words_list))

    valid_label_list = [valid_label[0:42]]
    for k in range(len(m)):
        if k + 1 >= len(m):
            break;
        m1 = valid_label[ m[k]+1 : m[k+1] ]
        valid_label_list.append( m1 )

    # print("len(valid_label_list)")
    # print(len(valid_label_list))

    tuple_valid=[]
    for i in range(len(valid_words_list)):
        tuple=(valid_words_list[i],valid_label_list[i])
        tuple_valid.append(tuple)
    # print(tuple_valid)

    #############################################################
    list(enumerate(test_words))
    n = [i for i, x in enumerate(test_words) if x == ' ']
    test_words_list =[test_words[0:42]]
    for j in range(len(n)):
        if j + 1 >= len(n):
            break;
        nn=test_words[n[j]+1 :n[j+1]]
        test_words_list.append(nn)
    test_label_list =[test_label[0:42]]
    for k in range(len(n)):
        if k + 1 >= len(n):
            break;
        n1=test_label[n[k]+1:n[k+1]]
        test_label_list.append(n1)


    # print("len(test_label_list)")
    # print(len(test_label_list))

    tuple_test=[]
    for i in range(len(test_words_list)):
        tuple=(test_words_list[i],test_label_list[i])
        tuple_test.append(tuple)
    # print(tuple_test)

    data={"train":tuple_train, "valid":tuple_valid,"test":tuple_test}

    return data
    # print(data)
    # print(train_words)
    # print(train_label)
    # print(valid_words)
    # print(valid_label)
    # print(test_words)
    # print(test_label)

read_data_from_xlsx()