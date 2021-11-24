#This is a program to perform first come first serve operation.
print("---------First Come First Serve-----------")

p = int(input("Enter Number of processes: "))
d = dict()

for i in range(p):
    key = "p"+str(i+1)
    a = int(input(f"Enter Arrival Time for p{str(i+1)} : "))
    b = float(input(f"Enter Burst Time for p{str(i+1)} : "))
    l = []
    l.append(a)
    l.append(b)
    d[key] = l

d = sorted(d.items(), key = lambda item: item[1][0])

et = []
for i in range(len(d)):
    if (i == 0):
        et.append(d[i][1][1])
    else:
        et.append(et[i-1] + d[i][1][1])

tat =[]
for i in range(len(d)):
    tat.append(et[i] - d[i][1][0])

wt = []
for i in range(len(d)):
    wt.append(tat[i] - d[i][1][1])

avg_wt = 0
for i in wt:
    avg_wt += i
avg_wt = (avg_wt/p)

print("Process   ArrivalTime   BurstTime      ExitTime   TurnAroundTime   WaitingTime  ")
for i in range(p):
    print("   ", d[i][0], " |     ", d[i][1][0], "     |    ", d[i][1][1], "    |    ",et[i], "   |      ", tat[i],"      |    ",wt[i],"      |  ")

print("Average Waiting Time: ", avg_wt)