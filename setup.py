import pickle

tasks = [False, [], []]
f = open("tasks.pkl", "wb")
pickle.dump(tasks, f)
f.close()
