import pickle

def copydb():
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def savedb(db):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(db, f)

def listtodict(dblist):
    dbdict = {}  
    dbdict["isdone"] = dblist[0]
    dbdict["actpgs"] = dblist[1]
    dbdict["pages"] = dblist[2]
    return dbdict

dblist = copydb()
dbdict = listtodict(dblist)
savedb(dbdict)
