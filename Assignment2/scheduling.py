class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct = 0   
        self.tat = 0  
        self.wt = 0   
# -------- Input --------
def input_processes():
    n = int(input("Enter number of processes (>=4): "))
    processes = []
    for i in range(n):
        pid = input(f"Enter Process ID for P{i+1}: ")
        at = int(input(f"Enter Arrival Time for {pid}: "))
        bt = int(input(f"Enter Burst Time for {pid}: "))
        processes.append(Process(pid, at, bt))
    return processes
# -------- Display Input --------
def display_processes(processes):
    print("\nPID\tAT\tBT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}")
# -------- FCFS Scheduling --------
def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x.at)
    time = 0
    gantt = []
    for p in processes:
        if time < p.at:
            time = p.at  
        start = time
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt
        gantt.append((p.pid, start, time))
    return gantt
# -------- SJF Scheduling (Non-Preemptive) --------
def sjf_scheduling(processes):
    processes_copy = processes[:]
    completed = []
    time = 0
    gantt = []
    while processes_copy:
        ready = [p for p in processes_copy if p.at <= time]
        if not ready:
            time += 1
            continue
        p = min(ready, key=lambda x: x.bt)
        start = time
        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt
        gantt.append((p.pid, start, time))
        completed.append(p)
        processes_copy.remove(p)
    return gantt, completed
# -------- Display Results --------
def display_results(processes):
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    total_tat = 0
    total_wt = 0
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")
        total_tat += p.tat
        total_wt += p.wt
    n = len(processes)
    print(f"\nAverage Turnaround Time: {total_tat / n:.2f}")
    print(f"Average Waiting Time: {total_wt / n:.2f}")
# -------- Gantt Chart --------
def display_gantt(gantt):
    print("\nGantt Chart:")
    for p in gantt:
        print(f"|  {p[0]}  ", end="")
    print("|")
    print(gantt[0][1], end=" ")
    for p in gantt:
        print(f"   {p[2]}", end=" ")
    print("\n")
# -------- Main Program --------
def main():
    processes = input_processes()
    print("\n--- Input Table ---")
    display_processes(processes)
    # FCFS
    print("\n===== FCFS Scheduling =====")
    fcfs_processes = [Process(p.pid, p.at, p.bt) for p in processes]
    gantt_fcfs = fcfs_scheduling(fcfs_processes)
    display_results(fcfs_processes)
    display_gantt(gantt_fcfs)
    # SJF
    print("\n===== SJF Scheduling =====")
    sjf_processes = [Process(p.pid, p.at, p.bt) for p in processes]
    gantt_sjf, completed_sjf = sjf_scheduling(sjf_processes)
    display_results(completed_sjf)
    display_gantt(gantt_sjf)
# Run program
if __name__ == "__main__":
    main()
