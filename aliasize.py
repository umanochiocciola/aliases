from sys import argv

def main():
    progr, prefix = setup()
    progr = replace(progr, prefix)
    output(progr)


def setup():
    if len(argv)<2:
        print("missing file argument"); exit(1)

    try:
        with open(argv[1], 'r') as f:
            progr = f.readlines()
    except:
        print("invalid file argument"); exit(1)

    try: prefix = argv[2]
    except: prefix = '#'
    
    return progr, prefix


def Alias(line):
    
    line = line.strip('\n')
    
    #print('line:', line)
    alias = line.split('=')[0].strip(' ')
    value = line.strip(line.split('=')[0]+'=').strip("'")
    #print('alias', repr(alias), '  value', repr(value))
    
    return {alias: value}


def replace(progr, prefix):
    active_aliases = {}

    for line in range(len(progr)):
        #print(repr(progr[line][:5+len(prefix)]))
        if progr[line][:5+len(prefix)] == prefix+'alias':
            alias = Alias(progr[line].strip(prefix+'alias').strip(' '))
            active_aliases.update(alias)
            
            progr[line] = ''
        else:
            for alias, value in active_aliases.items():
                progr[line] = progr[line].replace(alias, value)

    return progr


def output(progr):
    with open('AL_'+argv[1], 'w') as f:
        f.write(''.join(progr))


if __name__ == '__main__': main()