import time
start_time = time.time()
import sys
import platform
import re
import  pandas as pd
import numpy as np
from os import path



def timeStamped(fname, fmt='{fname} %d.%m.%Y %H.%M.xlsx'):
    import datetime
    # This creates a timestamped filename so we don't overwrite our good work
    return datetime.datetime.now().strftime(fmt).format(fname=fname)



def server_connection_mode(mode, ):
    if ('rerun' in sys.argv):
        mode = 'rerun'

    if (sys.platform == "Windows" or sys.platform == "win32"):
        import pyodbc
        print("running on Windows, Python version ", platform.sys.version)
        # "Driver={ODBC Driver 17 for SQL Server};"
        # server = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=(local);" "Database=Shivat_Prod;" "Trusted_Connection=yes;")
        # server = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" "Server=(10.110.110.9);" "Database=Shivat_Prod;" "UID=sayiqan;" "PSW=Sayiqan17;" "Trusted_Connection=no;")
        server = pyodbc.connect(
            "Trusted_Connection=no;DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.110.110.9;PORT=1433;DATABASE=Shivat_Prod;UID=sayiqan;PWD=Sayiqan17;")
    elif (sys.platform == "linux"):
        import pymssql
        print("running on Linux, Python version ", platform.sys.version)
        server = pymssql.connect(server="10.110.110.9", database="Shivat_Prod", port="1433", user="sayiqan",
                                 password="Sayiqan17")

    mycursor = server.cursor()

    # read existing categories and their scores
    print("Reading data")
    dic_score = {}
    sql_cats = """SELECT [CategoryID]
    	  ,[CategoryName]
          ,[CategoryScore]
          FROM [Category]"""
    df_cats = pd.read_sql_query(sql_cats, server)
    for k in range(len(df_cats)):
        dic_score[df_cats['CategoryID'][k]] = df_cats['CategoryScore'][k]
    dic_score['0'] = 0

    # F = open("InternalPostID test counter.txt",'r')
    # minPostId = int(F.read())
    # F.close()
    maxPostId = minPostId = 0
    # mycursor = server.cursor()
    print(mode)
    # load selection of posts to check
    if (mode == 'latest'):
        mycursor.execute("SELECT max(InternalPostId) from Post where PostLanguage = 'ru' and AntisemiteLevel > 0")
        minPostId = maxPostId = mycursor.fetchone()[0]
        logger.info("Latest, Min post Id found is %s" % minPostId)
        if (str(minPostId) == 'None'):
            minPostId = 0
            print("starting at %s" % minPostId)
        # minPostId = 131052185
        par = {}
        par['min'] = minPostId
        query = "SELECT TOP (25000) [InternalPostID],[PostText] FROM [Post] WHERE PostLanguage='ru' and InternalPostId > " + str(
            minPostId)
        df_server = pd.read_sql_query(query, server)

    if (mode == 'rerun'):
        # go from end backwards
        if (os.path.isfile("Next InternalPostID for rerun.txt")):
            F = open("Next InternalPostID for rerun.txt", 'r')
            maxPostId = int(F.read())
            F.close()

            # if (maxPostId < 950000000):
            #     print("Stopping: rerun limit reached")
            #     sys.exit()
            logger.info("In Rerun, Top post Id is %s" % maxPostId)
        else:
            mycursor.execute("SELECT max(InternalPostId) from Post where PostLanguage = 'ru'")
            maxPostId = mycursor.fetchone()[0]
            logger.info("Max post Id found is %s" % maxPostId)

        minPostId = maxPostId
        query = "SELECT top(320000) [InternalPostID],[PostText] FROM [Post] WHERE PostLanguage='ru' and InternalPostId <= " + str(
            maxPostId) + " order by InternalPostId desc"
        df_server = pd.read_sql_query(query, server)

    if (df_server.shape[0] == 0):
        print("Nothing to do")
        sys.exit()

    # print('starting')
    # print(minPostId)
    # sys.exit()a
    logger.info("--- FOCS Starting at %s seconds, %s posts to check ---" % (time.time() - start_time, df_server.shape[0]))

    return df_server, dic_score, minPostId, mycursor, server, mode, maxPostId
    print("--- FOCS Starting at %s seconds, %s posts to check ---" % (time.time() - start_time, df_server.shape[0]))


def DB_write(dic_score, text_predict, df_server, minPostId, mycursor, server, mode, maxPostId):
    print("--- FOCS ratings at %s seconds ---" % (time.time() - start_time))
    antisemite_num_cat = len(list(set(y_train)))
    antiesemite_cou = 0
    antisemite_cat = [0, 1.01]#1.01, 1.02, 1.05, '1.06.01', 3.01, 3.03, 1.03, 2.01, 1.07, 2.09, 2.02, 2.06, 2.11]

    count = 0
    # for i in range(len(x_test)):
    #     count += 1


        # print("im here")
        # for j in range(1, antisemite_num_cat): #for mult labeling classification
        #     try:
        #         if (y_test_labels_pred_prob[i][j] > 0.2):
        #             test_text_cat.append(antisemite_cat[j])
        #             test_text_InternalPostId.append(test_InternalPostID[i])
        #     except:
        #         print("Exception with item " + str(count) + ", cat is " + str(j))
    test_text_cat = text_predict
    label_dic = {'0': '0',
                 '1': '1.01'}
    test_text_cat = [label_dic[label] for label in test_text_cat]
    test_text_InternalPostId = df_server['InternalPostID'].tolist()
    # print("--- SQL prepare at %s seconds, %s categories to mark ---" % (time.time() - start_time, len(test_text_cat)))

    cnt = cnt_cat = 0
    ins_cat = []
    del_list = set()
    dic_ins_val = dict((v, set()) for v in dic_score.values())
    for i in range(len(test_text_cat)):
        cnt += 1
        intID = str(test_text_InternalPostId[i])
        cat = str(test_text_cat[i])

        del_list.add("'" + intID + "'")
        score = dic_score[cat]
        dic_ins_val[score].add("'" + intID + "'")

        if (cat != '0'):
            ins_cat.append('(' + intID + ",'" + str(cat) + "')")
            cnt_cat += 1
            if (int(intID) < minPostId):
                minPostId = int(intID)

        if (cnt > 999 or cnt_cat > 999):
            sql_del = "delete from xPost_Category where InternalPostID in (" + ','.join(del_list) + ')'
            mycursor.execute(sql_del)
            for score in dic_ins_val.keys():
                if (len(dic_ins_val[score]) > 0):
                    id_list = ','.join(dic_ins_val[score])
                    sql_100 = "update Post set Antisemitelevel=" + str(
                        score) + " where InternalPostID in (" + id_list + ")"
                    mycursor.execute(sql_100)
            if (len(ins_cat) > 0):
                sql_ins = "insert into xPost_Category (InternalPostID, CategoryID) values " + ','.join(ins_cat)
                mycursor.execute(sql_ins)

            server.commit()

            ins_cat = []
            del_list = set()
            dic_ins_val = dict((v, set()) for v in dic_score.values())
            cnt = cnt_cat = 0

    if (cnt > 0):
        sql_del = "delete from xPost_Category where InternalPostID in (" + ','.join(del_list) + ')'
        mycursor.execute(sql_del)
    for score in dic_ins_val.keys():
        if (len(dic_ins_val[score]) > 0):
            id_list = ','.join(dic_ins_val[score])
            sql_100 = "update Post set Antisemitelevel=" + str(score) + " where InternalPostID in (" + id_list + ")"
            mycursor.execute(sql_100)
    if (len(ins_cat) > 0):
        sql_ins = "insert into xPost_Category (InternalPostID, CategoryID) values " + ','.join(ins_cat)
        mycursor.execute(sql_ins)

    server.commit()

    # get minimum InternalPostId from

    print("--- Person Update at %s seconds ---" % (time.time() - start_time))

    relevantPosts = 200000
    if (mode == 'latest'):
        relevantPosts = 400000
    sql_upd = """UPDATE Person SET AntisemiteTypeID = 1
    WHERE InternalPersonID IN (

        SELECT InternalPersonID FROM person WHERE AntisemiteTypeID IN (0,2,3) and InternalPersonID IN (
    	    SELECT DISTINCT InternalPersonID FROM post WHERE (
                AntisemiteLevel > 0 
                AND PostLanguage = 'ru'
                and InternalPostID BETWEEN """ + str(minPostId - relevantPosts) + """ AND """ + str(
        maxPostId + relevantPosts) + """
    		)
            GROUP BY InternalPersonID HAVING count(*) >= 1
        )
    )"""

    mycursor.execute(sql_upd)
    server.commit()

    mycursor.close()
    text_num = df_server.shape[0]
    last_post_cou = df_server['InternalPostID'][text_num - 1]
    F = open("InternalPostID test counter.txt", 'w')
    F.write(str(last_post_cou))
    F.close()

    # logger.info("Min post Id affected is %s" % minPostId)

    if (mode == 'rerun'):
        F = open("Next InternalPostID for rerun.txt", 'w')
        F.write(str(minPostId))
        F.close()


df_server, dic_score, minPostId, mycursor, server, mode, maxPostId = server_connection_mode(mode='latest')


DB_write(dic_score, text_predict, df_server, minPostId, mycursor, server, mode, maxPostId)