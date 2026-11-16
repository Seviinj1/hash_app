
import sys
import os
import xxhash

n = int(sys.argv[1])
s = int(sys.argv[2])

if n <= 0 or s <= 0:
    print("It must be positive")
    sys.exit()

print("Started")
print("Buckets:", n)
print("Size:", s)

for i in range(1, n + 1):
    f_name = str(i) + ".txt"
    f = open(f_name, "a", encoding="utf-8")
    f.close()

while True:
    try:
        text = input("Please enter the string: ")

        if len(text) == 0:
            print("Not allowed")
            continue

        if len(text) > s:
            print("It is bigger")
            continue

        h = xxhash.xxh64(text.encode("utf-8")).intdigest()
        b = (h % n) + 1

        main_file = f"{b}.txt"
        link_file = f"{b}.chain"

      
        if os.path.exists(link_file):
            f = open(link_file, "r", encoding="utf-8")
            current_file = f.read().strip()
            f.close()
        else:
            current_file = main_file

        
        if os.path.exists(current_file):
            f = open(current_file, "r", encoding="utf-8")
            content = f.read()
            current_size = len(content)
            f.close()
        else:
            current_size = 0

        
        if current_size + len(text) <= s:
            fname = current_file

        else:
            
            overflow_number = 1

            while True:
                fname = str(b) + "_" + str(overflow_number) + ".txt"
                if not os.path.exists(fname):
                    break
                overflow_number += 1

        
        f = open(fname, "a", encoding="utf-8")
        f.write(text)
        f.close()

       
        if fname != main_file and fname != current_file:
            f = open(link_file, "w", encoding="utf-8")
            f.write(fname)
            f.close()

        print(f"Added to {fname}")

    except KeyboardInterrupt:
        print("\nStopped")
        break
