import os
import argparse
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument("--stage", type=str, help="Stage you want to deploy")
parser.add_argument("--functions", type=str, help="List of functions you want to package")
args = parser.parse_args()

func_list = (args.functions).split(",")

if __name__ == "__main__":
    #sls_data = get_sls_data()
    for func in func_list:
        print(f"Downloading dependencies for  {func} ...")
        download_deps(func,args.stage)

    
