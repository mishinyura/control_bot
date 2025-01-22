import os
def info(data: dict, indent: int = 0) -> None:
    for key, val in data.items():
        print('\t' * indent, end='')
        if isinstance(val, dict):
            print(f'{key}:')
            info(val, indent + 1)
        else:
            print(f'{key}={val}')


def get_list_from_file(name: str) -> list:
    path = os.path.abspath(os.sep.join(['database', name]))
    print(path)
    with open(path, 'r', encoding='utf-8') as file:
        lst = [word.strip() for word in file]

    return lst
