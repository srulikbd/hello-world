import  pandas as pd
import time
start_time = time.time()
import os
import sys
import logging
import platform
# from Utils import clean_text
import pickle

logging.basicConfig(filename='Arabic_ACMS.log', format='%(asctime)s %(name)s (%(levelname)s) - %(message)s', level=logging.INFO)
logger = logging.getLogger('ACMS-Arabic')

def server_connection_mode():


    if (sys.platform == "Windows" or sys.platform == "win32"):
        import pyodbc
        print("running on Windows, Python version ", platform.sys.version)
        # "Driver={ODBC Driver 17 for SQL Server};"
        # server = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=(local);" "Database=Shivat_Prod;" "Trusted_Connection=yes;")
        # server = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" "Server=(10.110.110.9);" "Database=Shivat_Prod;" "UID=sayiqan;" "PSW=Sayiqan17;" "Trusted_Connection=no;")
        server = pyodbc.connect(
            "Trusted_Connection=no;DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.100.110.5;PORT=1433;DATABASE=Shivat_Prod;UID=daniel;PWD=1q2w3e4R;")
    elif (sys.platform == "linux"):
        import pymssql
        print("running on Linux, Python version ", platform.sys.version)
        server = pymssql.connect(server="10.100.110.5", database="Shivat_Prod", port="1433", user="daniel", password="1q2w3e4R")

    # logger.info(
    #     "--- BERT Starting at %s seconds, %s posts to check ---" % (time.time() - start_time, df_server.shape[0]))

    return server

import re

def build_text_files(text, dest_path):
    f = open(dest_path + 'en_tw_for_DL_training_large.txt', 'w',  encoding='utf8')

    for row in text:
        # print(row)
        row+='\n'
        f.write(row)
    f.close()

def clean_text(text):
    eng_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # english_free = ''.join([ch for ch in doc if ch not in eng_letters])
    # stop_free = ' '.join([i for i in punc_free.split() if i not in arb_long_sw])
    try:
        stop_free = re.sub("^RT:", "", text)
        stop_free = re.sub("User Location:.*", "", stop_free)
        # stop_free = re.sub(r'http\S+', "", stop_free)
        stop_free = re.sub(r'\bhttps?://\S+', "", stop_free)
        stop_free = re.sub("@.*:", "", stop_free)
        # stop_free = re.sub("@.*", "", stop_free)
        stop_free = stop_free.strip()
    except:
        stop_free = ''
        print('cant parse the text')

    return stop_free

# def sql_batch():
#     internalpostid=0
#     for i in range(0, 155000000, 1000000)
#     query = "SELECT TOP (40000000) [PostText] FROM [Shivat_Prod].[dbo].[Post] where PostLanguage='en' and InternalPostID>90000000"


# server = server_connection_mode()

# mycursor.execute("SELECT max(InternalPostId) from Post where PostLanguage = 'ar' and AntisemiteLevel > 0")
# minPostId = maxPostId = mycursor.fetchone()[0]

# if (str(minPostId) == 'None'):
#     minPostId = 0
#     print("starting at %s" % minPostId)
# minPostId = 131052185


query = "SELECT TOP (40000000) [PostText] FROM [Shivat_Prod].[dbo].[Post] where PostLanguage='en' and InternalPostID>90000000"

# df_server = pd.read_sql_query(query, server)
# df_server = df_server.drop_duplicates(subset='PostText')
# df_server = df_server['PostText'].tolist()
# df_server = [clean_text(text) for text in df_server]
# pickle.dump(df_server, open('en_tw_for_DL_training.pickle', 'wb'))
df_server = pickle.load(open('en_tw_for_DL_training.pickle', 'rb'))
print(len(df_server))
build_text_files(df_server, r'C:\Users\user\Google Drive\סאיקאן\GitHub\DB_read_write\MsSQL\data\\')
print(len(df_server))
