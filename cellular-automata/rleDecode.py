import numpy as np

def run_length_decode(rle):
    ''' Expand the series of run-length encoded characters.
    '''
    run = ''
    for c in rle:
        if c in '0123456789':
            run += c
        else:
            run = int(run or 1)          # if the run isn't explicitly coded, it has length 1
            v = c if c in 'bo$' else 'b' # treat unexpected cells as dead ('b')
            for _ in range(run):
                yield v
            run = ''

def expand_rle(rle):
    ''' Expand a run-length encoded pattern.
    Returns the pattern name, full name and its cells. http://www.conwaylife.com/wiki/RLE
    '''
    rle_file_name = '%s.rle' % rle
    lines = open(rle_file_name).read().splitlines()
    if lines[0].startswith('#N '):
        name = lines[0][3:]
    else:
        name = rle
    lines = [L for L in lines if not L.startswith('#')]
    header = lines[0]
    xv, yv = header.split(',')[:2]
    x = int(xv.partition('=')[2])
    y = int(yv.partition('=')[2])
    pattern = np.zeros((x, y))
    body = ''.join(lines[1:])
    body = body[:body.index('!')].lower() # '!' terminates the body
    i, j = 0, 0
    for c in run_length_decode(body):
        if c == '$':
            i, j = i+1, 0
        else:
            if c == 'o':
                pattern[i][j] = 1
            j += 1
    return pattern