import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="parser name")
    parser.add_argument('--arg1', type=str, help='first arg')
    parser.add_argument('--arg2', type=str, help='second arg')
    return parser.parse_args()

args=parse_args()
arg1=args.arg1
arg2=args.arg2
print(arg1,arg2)