from matplotlib import pyplot as plt

time_step = []
list1 = []
list2 = []
list3 = []

lists = []
lists.append(list1)
lists.append(list2)
lists.append(list3)


t = 0

with open("../demo/out", "r") as F:
    for line in F:
        time_step.append(t)
        t = t + 1
        for word in line.split():
            w = 0;
            lists[w].append(word)
            w = w + 1
