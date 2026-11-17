
# hash_app

A basic Python program that saves text into different text files (buckets) using hashing.

## Requirements
Python and xxhash library

## What it does

When the user enters a word or sentence, the program calculates its hash value using the `xxhash` library and saves it into one of the numbered `.txt` files. The number of buckets and bucket size are given through command-line arguments.

## How to Run

Run the application using:

    python hash_app.py n s

- n = Number of buckets
- s = Bucket size in symbols

Example:

    python hash_app.py 5 20

## Hashing Algorithm

The application uses the **xxHash64** algorithm with the Python `xxhash` library.

The hash value is calculated for each input string and used to select a bucket:

b = (h % n) + 1

The selected bucket file is named from `1.txt` to `n.txt`.

## Overflow Bucket Management

Each bucket has a maximum size of `s` symbols.

When a bucket does not have enough space for a new string, the application creates an overflow file.

For example:

- `1.txt` - original bucket
- `1_1.txt` - first overflow file
- `1_2.txt` - second overflow file

A reference file named `1.chain` stores the name of the latest overflow file.

When the application starts again, it reads this reference file to find the last overflow file and continue writing there. If that file becomes full, a new overflow file is created and the reference is updated.

Strings are stored without separators.
