# Given a list of (positive integer) latencies, a number of buckets and bucket width, calculate how frequently each range of latencies occurs

# The first bucket always starts at 0. For instance, the ranges for 11 buckets of width 10 are: 0-9, 10-19, 20-29, 30-39, 40-49, 50-59, 60-69, 70-79, 80-89, 90-99, >=100

# For example:

latencies = [90, 11, 3, 35, 17, 28, 64, 53, 52, 87, 63, 46, 40, 50, 31, 92, 45, 32, 22, 54, 87, 108, 62, 33, 87, 12, 67, 56, 94, 119, 96, 23, 21, 25, 86, 5, 32, 77, 3, 16, 8, 61, 105, 88, 49, 57, 114, 118, 20, 79, 44, 55, 113, 23, 13, 86, 16, 81, 1, 111, 84, 76, 24, 54, 110, 7, 100, 40, 3, 37, 96, 37, 67, 48, 79, 47, 108, 36, 15, 112, 37, 13, 40, 66, 39, 110, 47, 87, 34, 50, 55, 112, 70, 88, 2, 86, 110, 20, 2, 57]
number_of_buckets = 11
bucket_width = 10
# >>> calc_buckets(latencies, number_of_buckets, bucket_width)
#   0- 9: 9
#  10-19: 8
#  20-29: 9
#  30-39: 11
#  40-49: 10
#  50-59: 11
#  60-69: 7
#  70-79: 5
#  80-89: 11
#  90-99: 5
#  100+ : 14

def calc_buckets(latencies, number_of_buckets, bucket_width):
    count = [0]*number_of_buckets

    for n in latencies:
        div = n//bucket_width
        if div > number_of_buckets - 1:
            count[-1] += 1
        else:
            count[div] += 1

    return count


calc_buckets(latencies, number_of_buckets, bucket_width)


# Given a file system structure representing directories and files,
# Return the total size of files in the structure.

# home/
# ├── me/
# │   ├── foo.txt : 416
# │   ├── metrics.txt : 5892
# │   └── src/
# │       ├── site.html : 6051
# │       ├── site.css : 5892
# │       └── data.csv : 332789
# └── you/
#     └── dict.json : 4913364
# bin/
# ├── bash: 618416
# ├── cat: 23648
# └── ls: 38704
# var/
# └── log/
#      ├── dmesg : 1783894
#      ├── wifi.log : 924818
#      └── httpd/
#          ├── access.log : 17881
#          └── access.log.0.gz : 4012

# total_size(file_system) -> 8675777


file_system = {
    'home': {
        'me': {
            'foo.txt': 416,
            'metrics.txt': 5892,
            'src': {
                'site.html': 6051,
                'site.css': 5892,
                'data.csv': 332789,
            },
        },
        'you': {
            'dict.json': 4913364,
        },
    },
    'bin': {
        'bash': 618416,
        'cat': 23648,
        'ls': 38704,
    },
    'var': {
        'log': {
            'dmesg': 1783894,
            'wifi.log': 924818,
            'httpd': {
                'access.log': 17881,
                'access.log.0.gz': 4012,
            },
        },
    },
}

def  total_size(file_system):
    total = 0

    if isinstance(file_system, int):
        total += file_system
    
    else:
        for f in file_system.values():
            total += total_size(f)
        
    return total 

print(total_size(file_system))