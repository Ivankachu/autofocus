import pickle

db = {"isdone": False, "active": [], "pages": []}
f = open("tasks.pkl", "wb")
pickle.dump(db, f)
f.close()
