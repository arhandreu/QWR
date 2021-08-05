def count_str_file(names):
    dict_file = {}
    for name in names:
        with open(name, 'rt', encoding='utf-8') as file:
            count_str = len(file.readlines())
            dict_file[name] = count_str
    sorted_dict = {}
    sorted_keys = sorted(dict_file, key=dict_file.get)
    for w in sorted_keys:
        sorted_dict[w] = dict_file[w]
    return sorted_dict


def write_file(names, file):
    sorted_dict = count_str_file(names)
    with open(file, 'at', encoding='utf-8') as w_file:
        for key, value in sorted_dict.items():
            with open(key, 'rt', encoding='utf-8') as r_file:
                w_file.write(key + "\n")
                w_file.write(str(value) + "\n")
                for i in range(value):
                    w_file.write(r_file.readline().strip() + "\n")


write_file(['1.txt', '2.txt', '3.txt'], '4.txt')
