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

#dict sorter
def sort(obj):
    ordered_d = sorted(obj.items(), key=lambda z: z[1], reverse=True)
    return dict(ordered_d)

#function to preprocess input
# strips carriage return from the string(just a workaround)
def preprocess(line,n):
    tmp=line.strip("\n")
    tmp=tmp.strip("\r\n")
    tmp=tmp.strip("\r")
    d_list=[tmp[i:i+n] for i in range(0,len(tmp),n)] #splits string in array of n steps
    return d_list

banner="""
░█▀▀░█▀▀▄░█▀▀░█▀▀█
░█▀░░█▄▄▀░█▀▀░█▄▄█
░▀░░░▀░▀▀░▀▀▀░░░░█ V-1.0 

ctrl+D to exit
"""

parser=argparse.ArgumentParser()
parser.add_argument('-n','--ngram',nargs='?',default=1,type=int,help='no of steps (default=1)')
parser.add_argument('-a','--alphabets',action='store_true',help='only analyses the frequency of alphabets(A-Z,a-z)')
parser.add_argument('-d','--digit',action='store_true',help='only analyses the frequency of digits')
parser.add_argument('-s','--symbols',action='store_true',help='only analyses the frequency of special characters')
parser.add_argument('-k','--suggest',action='store_true',help='only analyses the frequency and suggests possible cypher')
arg=parser.parse_args()

freq_list=dict()

console.print(banner,style="bold #44aec2")

nsteps=arg.ngram

for line in sys.stdin:
    freq_list=dict()
    if len(line)>0:
        chunk=preprocess(line,nsteps)
        if not arg.alphabets and not arg.digit and not arg.symbols:
            #include all chars
            for c in chunk:
                #TODO:fix spaces
                if c in freq_list:
                    freq_list[c]+=1
                else:
                    freq_list[c]=1
            console.print("> analysing alphabets,digits and special characters",style="bold #fc00a3") 

        if arg.alphabets:
            #add only aplhabets in the inp_data
            for c in chunk:
                #is alphabet
                if c.isalpha():
                    if c in freq_list:
                        freq_list[c]+=1
                    else:
                        freq_list[c]=1

            console.print("> analysing alphabets",style="bold #fc00a3")        
            
        if arg.digit:
            #add only digit in the inp_data
            for c in chunk:
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
                    #TODO: alias for space
                    if c in freq_list:
                        freq_list[c]+=1
                    else:
                        freq_list[c]=1

            console.print("> analysing special characters",style="bold #fc00a3")

        if arg.suggest:
            #analyse the input
            print("-k used")

    showTable(sort(freq_list),len(line))
    console.print("[cyan]∑ = [/cyan]",len(freq_list))
    console.print("[cyan]Total no of chars in input = [/cyan]",len(line))

