import sys
import argparse
sys.setrecursionlimit(10000000)
def recursion(coins,target,res,tmp):
    
    for i in coins:
        #print(target,i)
        if target==i:
            tmp+=[i]
            tmp.sort()
            if tmp is not None:
                res.append(tuple(tmp))
        elif target>i:
            #print(target-i,tmp+[i])
            recursion(coins,target-i,res,tmp+[i])   
        else:
            return
        if res!=[]:
            return

def sum(coins, target):
    coins.sort()
    res=[]
    tmp=[]
    recursion(coins,target,res,tmp)
    if(res != []):
        return "true"
    else:
        return "false"


parser = argparse.ArgumentParser()
parser.add_argument("--coins", type=int, nargs = '+', help="list of coins")
parser.add_argument("--amount", type = int, help="certain amount")
args = parser.parse_args()

print(sum(args.coins,args.amount))