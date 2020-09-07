
antisemite_cat = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def write(test_text_InternalPostId,  test_text_cat, dic_score, mycursor, server, mode, df_server, tagger, y_probability):
    # minPostId = 0
    # cnt = cnt_cat = 0
    # ins_cat = []
    # del_list = set()
    # dic_ins_val = dict((v, set()) for v in dic_score.values())
    # for i in range(len(test_text_cat)):
    #     cnt += 1
    #     intID = str(test_text_InternalPostId[i])
    #     cat = str(test_text_cat[i])
    #
    #     del_list.add("'" + intID + "'")
    #     score = dic_score[cat]
    #     dic_ins_val[score].add("'" + intID + "'")
    #
    #     if (cat != '0'):
    #         ins_cat.append('(' + intID + ",'" + str(cat) + "')")
    #         cnt_cat += 1
    #         if (int(intID) < minPostId):
    #             minPostId = int(intID)
    #
    #     if (cnt > 999 or cnt_cat > 999):
    #         sql_del = "delete from xPost_Category where InternalPostID in (" + ','.join(del_list) + ')'
    #         mycursor.execute(sql_del)
    #         for score in dic_ins_val.keys():
    #             if (len(dic_ins_val[score]) > 0):
    #                 id_list = ','.join(dic_ins_val[score])
    #                 sql_100 = "update Post set Antisemitelevel=" + str(score) + " where InternalPostID in (" + id_list + ")"
    #                 mycursor.execute(sql_100)
    #         if (len(ins_cat) > 0):
    #             sql_ins = "insert into xPost_Category (InternalPostID, CategoryID) values " + ','.join(ins_cat)
    #             mycursor.execute(sql_ins)
    #
    #         server.commit()
    #
    #         ins_cat = []
    #         del_list = set()
    #         dic_ins_val = dict((v, set()) for v in dic_score.values())
    #         cnt = cnt_cat = 0
    #
    # if (cnt > 0):
    #     sql_del = "delete from xPost_Category where InternalPostID in (" + ','.join(del_list) + ')'
    #     mycursor.execute(sql_del)
    # for score in dic_ins_val.keys():
    #     if (len(dic_ins_val[score]) > 0):
    #         id_list = ','.join(dic_ins_val[score])
    #         sql_100 = "update Post set Antisemitelevel=" + str(score) + " where InternalPostID in (" + id_list + ")"
    #         mycursor.execute(sql_100)
    # if (len(ins_cat) > 0):
    #     sql_ins = "insert into xPost_Category (InternalPostID, CategoryID) values " + ','.join(ins_cat)
    #     mycursor.execute(sql_ins)
    #
    # server.commit()

    ####  new version    #####################################################

    PostLanguage = 'ar'
    InternalPostID_cou = 0
    cou = 0
    ins_tag = []
    print("num of persons:")
    for i in range(len(test_text_cat)):
        if(test_text_cat[i]!=0):
            InternalPostID = test_text_InternalPostId[i]
            Tagger=tagger
            TagType='Null'
            TagTypeID=test_text_cat[i]
            TagValue=y_probability[i]
            TagData='Null'
            variables = [InternalPostID ,Tagger, TagType, TagTypeID, TagValue, TagData]
            variables = [str(var) for var in variables]
            ins_tag.append("'" + "','".join(variables) +"'")
            InternalPostID_cou = InternalPostID_cou + 1
            if (len(ins_tag) > 0 and (InternalPostID_cou % 1000) == 999):
                sql_ins = "insert into 'PostTag' ('InternalPostID', 'Tagger', 'TagType', 'TagTypeID', 'TagValue', 'TagData') VALUES " + '(' + '),('.join(
                    ins_tag) + ')'
                sql_copy_PostTag_to_xPostCat = "insert into xPost_Category(InternalPostID, CategoryID) " \
                                               "select  InternalPostID, TagTypeID from [Stage_Lights2].[dbo].[PostTag]"
                # print(sql_ins)
                mycursor.execute(sql_ins)
                # try:
                #     mycursor.execute(sql_copy_PostTag_to_xPostCat)
                # except:
                #     print('error')
                server.commit()
                ins_tag = []
                sql_ins = []

    if (len(ins_tag) > 0):
        sql_ins = """insert into Stage_Lights."PostTag" ("InternalPostID", "Tagger", "TagType", "TagTypeID", "TagValue", "TagData") VALUES""" + '(' + '),('.join(
            ins_tag) + ')'
        mycursor.execute(sql_ins)
        server.commit()
        ins_tag = []
        sql_ins = []

    server.commit()
    mycursor.close()




    # print("--- Person Update at %s seconds ---" % (time.time() - start_time))

    relevantPosts = 0
    if (mode == 'latest'):
        relevantPosts = 0

    # sql_upd = """UPDATE Person SET AntisemiteTypeID = 1
    #       WHERE InternalPersonID IN
    #
    # (SELECT InternalPersonID FROM person WHERE AntisemiteTypeID IN (0,2,3) and InternalPersonID IN
    # (SELECT InternalPersonID FROM post WHERE
    # (
    #  AntisemiteLevel > 0
    # AND PostLanguage = 'ar'
    # and InternalPostID >= """ + str(minPostId - relevantPosts) + """)
    # GROUP BY InternalPersonID HAVING SUM(antisemiteLevel) >= 10 AND count(*) >= 1
    # )
    #
    # )"""

    # mycursor.execute(sql_upd)
    # server.commit()
    #
    # mycursor.close()
    # last_post_cou = df_server['InternalPostID'][text_num - 1]
    # F = open("InternalPostID test counter.txt", 'w')
    # F.write(str(last_post_cou))
    # F.close()