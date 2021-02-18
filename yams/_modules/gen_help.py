import os
def process(files):
    """
    returns list of all commands from du scan of module dir
    """
    result = []
    for el1 in files:
        append = True
        for el2 in files:
            if el1 in el2 and el1 != el2:
                append = False
        if append:
            result.append(el1)
    return '\n'.join(result)


if __name__ == '__main__':
    files = os.popen("""du  | awk '{print $2}' | grep -v _ \
                        | sed 's/\.\///g' | sed 's/\//\./g' \
                        | sed '$d'""").read()
    files = files.split('\n')[:-1]
    print(process(files))
