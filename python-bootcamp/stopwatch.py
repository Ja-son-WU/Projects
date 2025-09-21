import time

def fmt(count):
    m, s = divmod(count, 60)
    return f"{m:02d}:{s:02d}"


count = int(input("Enter countdown time: "))

print()
while count > 0:
    print("\r⏳ " + fmt(count), end="", flush=True)
    time.sleep(1)
    count -=1

print("\ntime is up")