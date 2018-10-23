from matplotlib import pyplot as plt

time_step = []
list1 = []
list2 = []
list3 = []

lists = []
lists.append(list1)
lists.append(list2)
lists.append(list3)

max_num = 0

t = 0

with open("out.txt", "r") as F: #change based on directory of output file
	for line in F:
		time_step.append(t)
		t = t + 1
		w = 0
		for word in line.split():
			num = int(word)
			if(num > max_num):
				max_num = num

			lists[w].append(num)
			w = w + 1

time_step_len = len(time_step)

#print("time_step size: ", len(time_step))
#print("list 1 size: ", len(lists[1]))
#print("max num is: ", max_num)

plt.plot(time_step, lists[0], 'r--', time_step, lists[1], 'bs', time_step, lists[2], 'g^')
plt.axis([0, time_step_len, 0, max_num])
plt.show()
