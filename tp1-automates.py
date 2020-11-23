#!/usr/bin/env python3
"""
Read an automaton and a word, returns:
 * ERROR if non deterministic
 * YES if word is recognized
 * NO if word is rejected
"""

import automaton
import sys
import pdb # for debugging

if len(sys.argv) != 3:
  usagestring = "Usage: {} <automaton-file.af> <word-to-recognize>"
  automaton.error(usagestring.format(sys.argv[0]))

automatonfile = sys.argv[1]  
word = sys.argv[2]

#a = automaton.Automaton("abc")
#a.add_transition("0","x","2 ")
#a.add_transition("0","y","3")
#a.make_accept("3")
#a.to_graphviz("abc-test")
#print(a)

fileName="Document.txt"
crimefile = open(fileName, 'r')
#yourResult = [line.split(' ') for line in crimefile.readlines()]
yourResult = [line.strip("\n") or line.split(" ") for line in crimefile.readlines()]

i=-1
for x in yourResult:
    i=i+1
    for y in yourResult[i]:
        if y != "0":
            print("YES")            
        else:
            print("ERROR")
            

#print("TODO: faire le TP 1")  