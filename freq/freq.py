#!/usr/bin/env python3
from rich.console import Console
from rich.table import Table
import argparse
import sys

console=Console()

#function to print freq_list in table
def showTable(freq_list,total):
    if len(freq_list)>0:
        table=Table(show_header=True, header_style="bold #ffd717")
        table.add_column("char")
        table.add_column("count")
        table.add_column("%")
        for k in freq_list:
            perct=round((freq_list[k]/total)*100,2) #percentage
            table.add_row(k,str(freq_list[k]),str(perct)) 
        
        console.print(table)
            
    else:
        console.print("> nothing to count",style="bold red")

#function to preprocess input
# strips carriage return from the string(just a workaround)
def preprocess(line):
    tmp=line.strip("\n")
    tmp=tmp.strip("\r\n")
    tmp=tmp.strip("\r")
    return tmp

banner="""
░█▀▀░█▀▀▄░█▀▀░█▀▀█
░█▀░░█▄▄▀░█▀▀░█▄▄█
░▀░░░▀░▀▀░▀▀▀░░░░█ 
"""

parser=argparse.ArgumentParser()
parser.add_argument('-n','--ngram',nargs='?',default=1,type=int,help='no of steps (default=1)')
parser.add_argument('-a','--alphabets',action='store_true',help='only analyses the frequency of alphabets(A-Z,a-z)')
parser.add_argument('-d','--digit',action='store_true',help='only analyses the frequency of digits')
parser.add_argument('-s','--symbols',action='store_true',help='only analyses the frequency of special characters')
parser.add_argument('-k','--suggest',action='store_true',help='only analyses the frequency and suggests possible cypher')
arg=parser.parse_args()

freq_list=dict()


print("\nanalysing...\n")

for line in sys.stdin:
    freq_list=dict()
    if len(line)>0:
        line=preprocess(line)
        if not arg.alphabets and not arg.digit and not arg.symbols:
            #include all chars
            for c in line:
                if " " in c:
                    if "space" in freq_list:
                        freq_list["space"]+=1
                    else:
                        freq_list["space"]=1
                elif c in freq_list:
                    freq_list[c]+=1
                else:
                    freq_list[c]=1
            console.print("> analysing alphabets,digits and special characters",style="bold #fc00a3") 

        if arg.alphabets:
            #add only aplhabets in the inp_data
            for c in line:
                #is alphabet
                if c.isalpha():
                    if c in freq_list:
                        freq_list[c]+=1
                    else:
                        freq_list[c]=1

            console.print("> analysing alphabets",style="bold #fc00a3")        
            
        if arg.digit:
            #add only digit in the inp_data
            for c in line:
                #if digit
                if c.isdigit():
                    if c in freq_list:
                        freq_list[c]+=1
                    else:
                        freq_list[c]=1

            console.print("> analysing digits",style="bold #fc00a3")        

        if arg.symbols:
            #add only symbols in the inp_data
            #use regexp
            for c in line:
                if not c.isalpha() and not c.isdigit():
                    if c==" ":
                        if "space" in freq_list:
                            freq_list["space"]+=1
                        else:
                            freq_list["space"]=1
                    elif c in freq_list:
                        freq_list[c]+=1
                    else:
                        freq_list[c]=1

            console.print("> analysing special characters",style="bold #fc00a3")

        if arg.suggest:
            #analyse the input
            print("-k used")

    showTable(freq_list,len(line))

