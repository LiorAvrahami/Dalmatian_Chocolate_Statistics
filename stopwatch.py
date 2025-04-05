import time as _time
_cur_start_times = []
_toc_times_hist = []
_b_stopwatch_print_by_default = True
_b_stopwatch_total_silence = False

def set_default__b_stopwatch_print(val):
    global _b_stopwatch_print_by_default
    _b_stopwatch_print_by_default = val
def set_default__b_stopwatch_total_silence(val):
    global _b_stopwatch_total_silence
    _b_stopwatch_total_silence = val

def tic(name=None):
    _cur_start_times.append((_time.time(), name))


def toc(b_print = None):
    global _b_stopwatch_print_by_default
    b_print = _b_stopwatch_print_by_default if b_print is None else b_print

    start_time,name = _cur_start_times.pop()
    T = _time.time()-start_time
    _toc_times_hist.append((T, name))
    if(b_print):
        if name is None:
            print(T)
        else:
            print("runtime of {0}:\t\t\t{1}".format(name,T))
    elif name is not None and _b_stopwatch_total_silence is not True:
        print("{0} done.".format(name))
    return T


def toctic(name=None, b_print = None):
    toc(b_print)
    tic(name)


def tic_toc_statistics(b_print = None):
    b_print = _b_stopwatch_print_by_default if b_print is None else b_print

    ret = "index\tmesured time\tprecent of max time\tname"

    max_time = max([mes[0] for mes in _toc_times_hist])
    for hist_index in range(len(_toc_times_hist)):
        time,name = _toc_times_hist[hist_index]
        if name is None:
            name = ""
        new_line = "{0}\t{1}\t{2}\t{3}".format(hist_index,time,time/max_time,name)
        ret += '\n'+new_line
    if b_print:
        print(ret)
    return ret