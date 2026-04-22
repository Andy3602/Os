import os, time, multiprocessing

# ── Task 1: Input ─────────────────────────────────────────────
def get_input():
    n = int(input("Processes: "))
    m = int(input("Resources: "))
    print("Allocation Matrix:")
    alloc = [list(map(int, input(f"  P{i}: ").split())) for i in range(n)]
    print("Maximum Matrix:")
    maxi  = [list(map(int, input(f"  P{i}: ").split())) for i in range(n)]
    avail = list(map(int, input("Available: ").split()))
    return n, m, alloc, maxi, avail

def show_table(n, m, alloc, maxi, avail):
    need = [[maxi[i][j]-alloc[i][j] for j in range(m)] for i in range(n)]
    print(f"\n{'PID':<6} {'Alloc':<20} {'Max':<20} {'Need'}")
    for i in range(n):
        print(f"P{i:<5} {str(alloc[i]):<20} {str(maxi[i]):<20} {need[i]}")
    print(f"Available: {avail}\n")
    return need

# ── Task 2: Need Matrix  (Need = Max - Allocation) ────────────
def calc_need(n, m, alloc, maxi):
    return [[maxi[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

# ── Task 3 & 4: Safety Algorithm + Safe Sequence ─────────────
def bankers(n, m, alloc, need, avail):
    work, finish, seq = avail[:], [False]*n, []
    while len(seq) < n:
        found = False
        for i in range(n):
          
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + alloc[i][j] for j in range(m)]
                finish[i] = True
                seq.append(i)
                print(f"  P{i} runs -> Work = {work}")
                found = True
                break
        if not found:
            break  
    return all(finish), seq

# ── Task 5: Result Analysis ───────────────────────────────────
def analyse(is_safe, seq):
    print("\n" + "="*42)
    if is_safe:
        print("STATE : SAFE")
        print("SEQ   :", " -> ".join(f"P{i}" for i in seq))
        print("All processes complete. No deadlock.")
    else:
        print("STATE : UNSAFE  (deadlock risk)")
        print("OS must deny requests until resources free.")
    print("\nCoffman conditions (Banker prevents Circular Wait):")
    print("  1.Mutual Exclusion  2.Hold&Wait")
    print("  3.No Preemption     4.Circular Wait")
    print(f"\nos.cpu={os.cpu_count()} | pid={os.getpid()} | "
          f"time={time.time():.2f} | mp={multiprocessing.cpu_count()}")
    print("="*42)

# ── Main ──────────────────────────────────────────────────────
def main():
    print("===== BANKER'S ALGORITHM =====")
    n, m, alloc, maxi, avail = get_input()
    need = show_table(n, m, alloc, maxi, avail)   
    need = calc_need(n, m, alloc, maxi)           
    print("--- Safety Check ---")
    is_safe, seq = bankers(n, m, alloc, need, avail)  
    analyse(is_safe, seq)                              

if __name__ == "__main__":
    main()
