import pickle

def copydb():
    with open('tasks.pkl', 'rb') as f:
        db = pickle.load(f)
    return db

def savedb(db):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(db, f)

db = copydb()
db['active'] = db['actpgs']
del db['actpgs']
savedb(db)
