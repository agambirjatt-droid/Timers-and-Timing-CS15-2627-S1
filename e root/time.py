import time
import random

fastest_time = None

for attempt in range(1, 6):
    print(f"Attempt {attempt}")
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    print("GO!")
    start_time = time.monotonic()
    input()
    end_time = time.monotonic()

    reaction_time = end_time - start_time
    print(f"Your reaction time was {reaction_time:.3f} seconds")

    if fastest_time is None or reaction_time < fastest_time:
        fastest_time = reaction_time

print(f"Your fastest reaction time was {fastest_time:.3f} seconds")