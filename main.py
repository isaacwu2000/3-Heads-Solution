from random import randint
def main():
    print("10 run average:", average_for_runs(10))
    print("100 run average:", average_for_runs(100))
    print("1,000 run average:", average_for_runs(1000))
    print("10,0000 run average:", average_for_runs(10000))
    print("100,000 run average", average_for_runs(100000))
    print("1,000,000 run average:", average_for_runs(1000000))
    print("10,000,000 run average:", average_for_runs(10000000))

# Simulating 1 'run' until obtaining 3 heads in a row, then returning the total number of coin-flips
def run():
    heads_streak = 0
    flips = 0
    while heads_streak < 3:
        if randint(0,1) == 1:
            heads_streak += 1
        flips += 1
    return flips

# Finding the average for 'n' runs
def average_for_runs(n):
    n_run_sum = 0
    for i in range(n):
        n_run_sum += run()
    return n_run_sum / n

if __name__ == "__main__":
    main()