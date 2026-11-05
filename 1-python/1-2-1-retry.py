# 1-2-1 Example of a Retry Loop 

from time import sleep 

TIMES = 5
BACKOFF = 5

print("Starting the retry loop...")
for attempt in range(TIMES):
    print(f"Attempt {attempt + 1} of {TIMES}")
    delay = BACKOFF * attempt
    print(f"sleeping for {delay} seconds...")
    sleep(delay)
    print("Retrying now...")

grocery_item = {}
