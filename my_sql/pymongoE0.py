import csv

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test
collection = db['premier_league_19_20']
with open("E0.csv") as f1:
    records = csv.reader(f1, delimiter=",")
    li=[]
    i=0
    for record in records:
        dict={}
        if(i>0):
            Div=record[0]
            Date = record[1]
            Time = record[2]
            HomeTeam= record[3]
            AwayTeam= record[4]
            FTHG= record[5]
            FTAG= record[6]
            FTR= record[7]
            HTHG= record[8]
            HTAG= record[9]
            HTR= record[10]
            Referee= record[11]
            dict={"Div":Div,"Date":Date,"Time":Time,"HomeTeam":HomeTeam,"AwayTeam":AwayTeam
                     ,"FTHG":FTHG,"FTAG":FTAG,"FTR":FTR,"HTHG":HTHG,"HTAG":HTAG,"HTR":HTR,"Referee":Referee}
            li.append(dict)
        i=i+1
xx=collection.insert_many(li)
xx.inserted_ids

