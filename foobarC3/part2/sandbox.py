import time
import functools
import operator

def timeit_decorator(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts)*1000)
        else:
            print (method.__name__, (te - ts)*1000)
        return result
    return timed


@timeit_decorator
def part_line (start, length):
    l = [[i for i in range(start+length*j, start+length*j + length - j)] for j in range(length)]
    flat = functools.reduce(operator.iconcat, l, [])
    res = functools.reduce(operator.xor, flat, 0)
    return res

@timeit_decorator
def part_line_one (start, length):
    res = 0
    for j in range(length):
        for i in range(start+length*j, start+length*j + length - j):
            res = res^i
    return res

def reduce_line(line):
    new_line = []
    for i in range (4):
        if line[i]%4:
            new_line.append(line[i])
        else:
            for j in range(i,4):
                new_line.append(line[len(line)-4+j])
            break
    return new_line


    


start = 0
length = 10000
#print(part_line(start ,length))
#print(part_line_one(start ,length))
@timeit_decorator
def xor_fun(line):
    line_sum = functools.reduce(operator.xor, line, 0)
    return line_sum

@timeit_decorator
def xor_fun_red(line):
    r_line = reduce_line(line)
    r_line_sum = functools.reduce(operator.xor, r_line, 0)
    return r_line_sum

seed = 17
line = [seed+i for i in range (4000000)]
#print(xor_fun(line))
#print('--->',part_line_one(start, length))
