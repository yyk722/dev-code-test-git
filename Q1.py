import numpy as np
import argparse

def check_div(num,divider):
    if int(num) % divider == 0:
        return True

def add_change(change,string):
    if change == "":
        change = string
    else:
        change += " " + string
    return change

parser = argparse.ArgumentParser()
parser.add_argument("n", type=int,help="total number of kid")
args = parser.parse_args()

n = args.n

output = np.arange(1,n+1)
output = output.astype(np.str)
for i in range(len(output)):
    change = ""
    fizz = check_div(output[i],3)
    buzz = check_div(output[i],5)
    woof = check_div(output[i],7)
    if fizz:
        change = add_change(change,"Fizz")
    if buzz:
        change = add_change(change,"Buzz")
    if woof:
        change = add_change(change,"Woof")
    if fizz or buzz or woof:
        output[i] = change
print(output)