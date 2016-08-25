def printval(**kwargs):
    for key, val in kwargs.items():
        print('{}: {}'.format(key, val))


def printdesc(description, value):
    print('{}: {}'.format(description, value))
