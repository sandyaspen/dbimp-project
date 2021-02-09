#Author: Sandy Wood  
#github.com/sandyaspen

#Wisconsin Database Benchmark Scalable Data Generator
import random
import argparse

class Columns:
    #unique1, unique integers in a random order
    unique1 = []
    #unique2, sequential integers 
    unique2 = []
    #two, unique1 mod 2
    two = []
    #four, unique1 mod 4
    four = []
    #ten, unique1 mod 10
    ten = []
    #twenty, unique1 mod 20
    twenty = []
    #one_percent, unique1 mod 100
    one_percent = []
    #ten_percent, unique1 mod 10
    ten_percent = []
    #twenty_percent, unique1 mod 5 
    twenty_percent = []
    #fifty_percent, unique1 mod 2
    fifty_percent = []
    #unique3, unique1 copy
    unique3 = []
    #even_one_percent, one_percent * 2
    even_one_percent = []
    #odd_one_percent, one_percent * 2 + 1
    odd_one_percent = []
    stringu1 = []
    stringu2 = []
    string4 = []

def make_unique_random_list(size):
    """Create a randomly-arranged list of size integers.
    
    Written using ideas from: 
    https://stackoverflow.com/questions/44857817/how-can-i-shuffle-a-very-large-list-stored-in-a-file-in-python
    """
    numbers = list(range(size))

    for i in range(size):
        rand = random.randint(i, size-1)
        numbers[i], numbers[rand] = numbers[rand], numbers[i]
        yield numbers[i]

def unique_to_string(number):
    """Convert a number into a string as per proceedure in wisconsin paper"""

    num = number
    count = 0
    result = list(("A" * 7) + ("x" * 45))

    while num > 0:
        char_value = ord(result[count])
        char_value += num % 26
        result[count] = chr(char_value)
        num = num // 26
        count += 1

    return "".join(result)

def generate_data(args):
    t_size = int(args.table_size)
    columns = Columns()
    string4_choices = [
        ("A" * 4) + ("x" * 48),
        ("H" * 4) + ("x" * 48),
        ("O" * 4) + ("x" * 48),
        ("V" * 4) + ("x" * 48),
    ]

    n = 0
    for number in make_unique_random_list(t_size):
        columns.unique1.append(number)
        columns.unique3.append(number)
        columns.unique2.append(n)
        columns.two.append(number % 2)
        columns.four.append(number % 4)
        columns.ten.append(number % 10)
        columns.twenty.append(number % 20)
        columns.one_percent.append(number % 100)
        columns.ten_percent.append(number % 10)
        columns.fifty_percent.append(number % 2)
        columns.even_one_percent.append(columns.one_percent[-1] * 2)
        columns.odd_one_percent.append((columns.one_percent[-1] * 2) + 1)
        columns.stringu1.append(unique_to_string(number))
        columns.stringu2.append(unique_to_string(n))
        columns.string4.append(string4_choices[n % 4])
        n += 1
    
    return columns


if __name__ == "__main__":
    #argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("table_size", help="Size of the table to create")
    parser.add_argument("file_name", help="Name of the output file")
    args = parser.parse_args()

    random.seed()

    print(generate_data(args))