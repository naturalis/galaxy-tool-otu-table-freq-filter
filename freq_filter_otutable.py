#!/usr/bin/python3
import pandas as pd
import numpy as np
from itertools import islice
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='')
requiredArguments = parser.add_argument_group('required arguments')
requiredArguments.add_argument('-i', metavar='input otutable', dest='input', type=str,required=True)
requiredArguments.add_argument('-f', metavar='filter frequency', dest='frequency', type=str, required=True)
requiredArguments.add_argument('-ot', metavar='output otutable', dest='output', type=str, required=True)
requiredArguments.add_argument('-ol', metavar='output log', dest='log', type=str, required=True)
args = parser.parse_args()


def get_unique_otus(otutable):
    uniqueOtus = []
    for name, values in otutable.iterrows():
        counts = values.value_counts(sort=True)
        counts = counts.sort_index()
        if 0 in counts.index and len(counts) < 3:
            if counts.iloc[1] == 1:
                uniqueOtus.append(name)
    return uniqueOtus

def filter_table(otutable, uniqueOtus):
    newOtutable = otutable
    uniqueOtusInfo = []
    for name, values in otutable.iteritems():
        #print(name)
        filterPercentage = values.sum()*float(args.frequency)
        #newOtutable[name] = otutable[name].apply(filter_value, axis=1, name=name, filterPercentage=filterPercentage)
        for index, value in otutable[name].items():
            if index not in uniqueOtus:
                if value < filterPercentage:
                    otutable.at[index,name] = 0
            else:
                if value > 0:
                    if value < filterPercentage:
                        uniqueOtusInfo.append(str(index)+" from sample "+str(name)+" is unique with an abundance of "+str(value)+" and saved from filtering\n")
                    else:
                        uniqueOtusInfo.append(str(index)+" from sample "+str(name)+" is unique with an abundance of "+str(value)+" but comes above the treshold ("+str(filterPercentage)+")\n")

    return otutable, uniqueOtusInfo

def main():
    otutable = pd.read_csv(args.input, sep="\t", header=0, index_col=0)
    uniqueOtus = get_unique_otus(otutable)
    filtered_table, logDict = filter_table(otutable, uniqueOtus)
    filtered_table.to_csv(args.output, sep='\t')
    with open(args.log, "a") as log:
        for x in logDict:
            log.write(x)

if __name__ == "__main__":
    main()
