import json
import sys
from unique import Unique
from cm_timer import cm_timer_1
from print_result import print_result
from get_random_ import get_random
from field import field

path = sys.argv[1] if len(sys.argv) > 1 else "data_light.json"

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted([item for item in Unique(field(arg, "job-name"))])

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист"), arg))

@print_result
def f3(arg):
    return list(map(lambda x: f"{x} с опытом Python", arg))

@print_result
def f4(arg):
    #return [f"{job}, зарплата {random.randint(100000, 200000)} руб." for job in arg]
    return [f"{job}, зарплата {next(get_random(len(arg), 100000, 200000))} руб." for job in arg]
    
if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))