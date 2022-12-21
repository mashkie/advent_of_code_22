import argparse

parser = argparse.ArgumentParser(description='train')
parser.add_argument(
    '--file',
    metavar='F',
    help='input file')

args = parser.parse_args()


def read_file():
    with open(args.file, encoding='utf-8') as input_file:
        return input_file.read()


def split_input(file_content):
    return file_content.split("\n\n")


def sum_groups(split_array):
    return [sum([int(item) for item in group.split('\n')]) for group in split_array]


def get_max(sums: list):
    return max(sums)


def sum_top_x(sums, number):
    sums.sort(reverse=True)
    return sum([sums[i] for i in range(number)])


if __name__ == "__main__":
    content = read_file()
    arrays = split_input(content)
    summed_arrays = sum_groups(arrays)
    print(get_max(summed_arrays))
    print(sum_top_x(summed_arrays, 3))
