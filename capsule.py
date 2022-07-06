#Diego Monego

import subprocess
import sys

from numpy import empty


file_name = 'test_log1.txt'

def run_texada():
    with open('capsule-output/texada-output.txt', 'w') as output:
        globally = subprocess.run(['bash' , 'run.sh', '-g', file_name], stdout= output, text = True)

        next = subprocess.run(['bash' , 'run.sh', '-x', file_name], stdout= output, text = True)

        finally_ = subprocess.run(['bash' , 'run.sh', '-f', file_name], stdout= output, text = True)

        # always_followed = subprocess.run(['bash' , 'run.sh', '--always-followed', file_name], stdout= output, text = True)
        
        # always_eventualy_followed = subprocess.run(['bash' , 'run.sh', '--always-eventualy-followed', file_name], stdout= output, text = True)
    output.close()

def split_list(inputList):
    # using list comprehension + zip() + slicing + enumerate()
    # Split list into lists by particular value
    size = len(inputList)
    idx_list = [idx + 1 for idx, val in
            enumerate(inputList) if val == '-----\n']
  
  
    splitList = [inputList[i: j] for i, j in
            zip([0] + idx_list, idx_list + 
            ([size] if idx_list[-1] != size else []))]
    return splitList

def read_texada_output():
    texada_output = open('capsule-output/texada-output.txt', 'r')
    specs = texada_output.readlines()
    return specs

def parse_output():
    #Reads alls specifications from texada output
    specs = read_texada_output()

    #Splits Specifications by type (e.g. Globally, Next, etc) and removes markers
    specs_splitList = split_list(specs)
    for i in specs_splitList:
        i.remove('-----\n')

    #Returns List with splitted specifications
    return specs_splitList
        
def create_translation(specs_splitList):

    translation = ""

    #Globalmente
    globalList = specs_splitList[0]
    
    if(globalList):
        translation += "The Following Events are always true: \n" + ''.join(globalList).replace("G", "")

    #Proximo
    nextList = specs_splitList[1]
    
    if(nextList):
        translation += "The Following Event is the second one in the trace: \n" + ''.join(nextList).replace("X", "") 

    #Eventualmente
    finallyList = specs_splitList[2]
    
    if(finallyList):
        translation += "The Following Events Eventually are true: \n" + ''.join(finallyList).replace("F", "") 
    

    return translation  
    
    


## --- MAIN ---
run_texada()
specs_splitList = parse_output()
translation = create_translation(specs_splitList)
print(translation)
