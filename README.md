
# hash_app

A basic Python program that saves text into different text files (buckets) using hashing.

## What it does

When the user enters a word or sentence, the program calculates its hash value using the `xxhash` library and saves it into one of the numbered `.txt` files. The number of buckets and bucket size are given through command-line arguments.

## How to Run

Run the application using:

    python hash_app.py n s

- n = Number of buckets
- s = Bucket size in symbols

Example:

    python hash_app.py 5 20

## How It Works

1. The program creates n empty text files (1.txt, 2.txt, etc.)
2. The user enters a string.
3. The string is hashed using xxHash64.
4. The hash value is used to select a bucket.
5. The string is added to the selected file.
6. Multiple strings can be stored in the same bucket.

It keeps asking for more strings until the user press Ctrl+C to stop it.
