import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('Cannot open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()