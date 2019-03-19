#!/usr/local/bin/python3
import pandas as pd
import numpy as np
from itertools import islice
import numpy as np

def get_unique_otus(otutable):
    uniqueOtus = []
    for name, values in otutable.iterrows():
        if 0 in values.unique() and len(values.unique()) == 2:
            uniqueOtus.append(name)
    return uniqueOtus

def filter_value(value, name, filterPercentage):
    print(value)

def filter_table(otutable, uniqueOtus):
    newOtutable = otutable
    uniqueOtusInfo = []
    for name, values in otutable.iteritems():
        #print(name)
        filterPercentage = values.sum()*0.05
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
    otutable = pd.read_csv('otu_table.tabular', sep="\t", header=0, index_col=0)
    uniqueOtus = get_unique_otus(otutable)
    filtered_table, logDict = filter_table(otutable, uniqueOtus)
    filtered_table.to_csv("filtered_table.txt", sep='\t')
    with open("log.txt", "a") as log:
        for x in logDict:
            log.write(x)

if __name__ == "__main__":
    main()
