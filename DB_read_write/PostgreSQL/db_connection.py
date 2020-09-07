import time
start_time = time.time()
import sys
import logging
# import sqlalchemy
# from sqlalchemy import text,create_engine
import pandas
import psycopg2

# def logging():
#     logging.basicConfig(filename='ML TF-IDF Anxiety.log', format='%(asctime)s %(name)s (%(levelname)s) - %(message)s',
#                         level=logging.DEBUG)
#     logger = logging.getLogger('ML TF-IDF Anxiety')
#     ch = logging.StreamHandler()
#     logger.addHandler(ch)
# logging()
# minPostId = 0


mode='latest'
print(mode)
maxInternalPostID=1
# split_dates=sys.argv[1]
split_dates="2019-10-07 12:29:51.000"
# split_dates.append(sys.argv[1])
# if('rerun' in sys.argv ):
#     mode = 'rerun'

# def db_connection():
print (sys.platform)
if(sys.platform == "Windows" or sys.platform == "win32"):

    # connect to PostGreSQL database on AWS

    aws_posgre = psycopg2.connect(
        "host=posgre-stage-lights.clmhtjp98p9t.us-east-2.rds.amazonaws.com dbname=Stage_Lights user=sayiqan password=Haim1946!")
    server = aws_posgre
    aws_posgre.autocommit = True

    aws = aws_posgre.cursor()
    print("aws encoding is ", aws_posgre.encoding)

    aws.execute("""SELECT count(*) from Stage_Lights."post" """)
    print("starting count is ", aws.fetchone()[0])
    query = """SELECT top(1000) "internalpostid","posttext","isviolent" FROM Stage_Lights."post" WHERE "postlanguage"='ar' and "postdate">'{}'"""
    df_server = pandas.read_sql_query(query.format(split_dates) ,server)



    import pyodbc
    print("running on Windows")
    #"Driver={ODBC Driver 17 for SQL Server};"
    #server = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=(local);" "Database=Shivat_Prod;" "Trusted_Connection=yes;")
    #server = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" "Server=(10.110.110.9);" "Database=Shivat_Prod;" "UID=sayiqan;" "PSW=Sayiqan17;" "Trusted_Connection=no;")
    # server = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=10.110.110.6;"
    #                 "Database=Stage_Lights2;" "uid=srulikbb;pwd=Srulik3141;")
elif (sys.platform == "linux"):
    import pymssql
    print("running on Linux")
    server = pymssql.connect(server="10.110.110.6", database="stage_lights", port="1433", user="ELI.TA", password="Sayiqan17")
server = aws_posgre
mycursor = aws
# if (mode == 'latest'):
    # mycursor.execute("SELECT max(InternalPostId) from vwPost where PostLanguage = 'ar'  ")
    # mycursor.execute("SELECT max(InternalPostId) from vwPost where PostLanguage = 'ar' and PostDate>'{}'".format(split_dates))
    # mycursor.execute("SELECT max(InternalPostId) from vwPost where PostLanguage = 'ar' and PostDate<'{}'".format(split_dates))
# minPostId=mycursor.fetchone()[0]
# print("minpostid")
# print(minPostId)
# if(str(minPostId) == 'None') :
#     minPostId = 0
# minPostId=None
#print("Min post Id found is %s" % minPostId)
# logger.info("Min post Id found is %s" % minPostId)
# if(mode == 'latest'):
#     par={}
    # par['min']=minPostId
    # query = "SELECT [InternalPostID],[PostText] FROM [vwPost] WHERE PostLanguage='ar' and InternalPostId > " + str(minPostId)
    # query = "SELECT [InternalPostID],[PostText],[IsViolent] FROM [vwPost] WHERE PostLanguage='ar' and PostDate>'{}'"
    # query = "SELECT [InternalPostID],[PostText],[IsViolent] FROM [Post] WHERE PostLanguage='ar' and PostDate>'{}'"
    # query = """SELECT top(1000) "InternalPostID","PostText","IsViolent" FROM Stage_Lights."Post" WHERE "PostLanguage"='ar' and "PostDate">'{}'"""
    # df_server=pandas.read_sql_query(query.format(split_dates) ,server)
    # print('len:')
    # print(len(df_server))
# if (mode == 'rerun'):
    #go from end backwards
    # mycursor.execute("SELECT max(InternalPostId) from vwPost where PostLanguage = 'ar'")
    # maxPostId=mycursor.fetchone()[0]
    # minPostId = maxPostId
    # logger.info("Max post Id found is %s" % maxPostId)
    # query = "SELECT top(1000) InternalPostID,PostText,IsViolent FROM stage_lights.vwPost WHERE PostLanguage='ar' and InternalPostId <= " + str(maxPostId) + " order by InternalPostId desc"
    # df_server = pandas.read_sql_query(query ,server)
    # df_ = df_server.drop_duplicates(subset='PostText', keep="first")
if(df_server.shape[0]==0):
    print("Nothing to do")
    sys.exit()

