print("********** Round Robin ************")

p = int(input("Enter number of processes: "))
q = int(input("Enter quantum Time: "))

l = []
rem_bt = [0] * p
ct = [0] * p
tat = [0] * p
total_tat = 0
avg_tat = 0
wt = [0] * p
total_wt = 0
avg_wt = 0

for i in range(p):
    process = f"p{i+1}"
    a = int(input(f"Enter Arrival time of p{i+1}: "))
    b = int(input(f"Enter Burst time of p{i+1}: "))
    l.append([process, [a, b]])

l  =sorted(l, key=lambda item: item[1][0])

for i in range(p):
    rem_bt[i] = l[i][1][1]

t = 0
while True:
    done = True
    for i in range(p):
        if rem_bt[i] > 0:
            done = False
            if rem_bt[i] > q:
                t += q
                rem_bt[i] -= q
            else:
                t = t + rem_bt[i]
                wt[i] = t - l[i][1][1]
                rem_bt[i] = 0
    
    if done:
        break

for i in range(p):
    tat[i] = wt[i] + l[i][1][1]
    ct[i] = tat[i] + l[i][1][0]
    total_tat += tat[i]
    avg_tat = total_tat/p

for i in range(p):
    total_wt += wt[i]
    avg_wt = total_wt/p

print("Processes    ArrivalTime    BurstTime   CompletionTime   TurnAroundTime   WaitingTime")

for i in range(p):
    print("{0:>4} {1:>12} {2:>14} {3:>15} {4:>16} {5:>17}".format(l[i][0], l[i][1][0], l[i][1][1], ct[i], tat[i], wt[i]))


print("Average Turn-around time: {:.2f}".format(avg_tat))
print("Average Waiting time: {:.2f}".format(avg_wt))