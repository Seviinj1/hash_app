
import sys
import xxhash

n = int(sys.argv[1])
s = int(sys.argv[2])

print("Started")
print("Buckets:", n)
print("Size:", s)

for i in range(1, n + 1):
    open(f"{i}.txt", "a").close()

while True:
    try:
        text = input("Please enter the string: ")

        h = xxhash.xxh64(text.encode("utf-8")).intdigest()
        b = (h % n) + 1
        fname = f"{b}.txt"

        with open(fname, "a", encoding="utf-8") as f:
            f.write(text)

        print(f"Added to {fname}")

    except KeyboardInterrupt:
        print("\nStopped")
        break
