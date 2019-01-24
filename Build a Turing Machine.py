import numpy as np
import csv


# Open the file

file = open(r'C:\Users\Elias\Documents\Berkeley 2018-2019\Fall Semester\Technical\CEE 290I Civil Systems Control and Information Management\Assignment 2\Compiler.txt',encoding='utf8')


# Create a list containing lists of each lines of the file

L = file.readlines()
l = len(L)


# Create new empty lists

List1 = []
Machines = []
Inputs = []
Output = []


# List1: Take only the lines that we want 

for i in range (0,l) :
    M = L[i]
    if M[0] == '{' :
        if M[1] == '{' :
            List1.append(M)
        else :
            Output.append(M)

print("\n The list of machines and inputs is:", List1)
print("\n The outputs are:", Output)
    

# List2: Create a list of several lists

list1 = len(List1)
List2 = []
for i in range(0,list1) :
    P = [List1[i]]
    List2.append(P)
print("\n List2 :", List2)


# List T: Find the position of the triple } in each lists of the list2

list2 = len(List2)
a = 0
T = []
for i in range(0,list2) :
    P = List2[i]
    p = len(P[0])
    for j in range(0,p-3) :
        if P[0][j] == '}' and P[0][j+1] == '}' and P[0][j+2] =='}' :
            a = j
            T.append(a)
print("\n T list:",T)


# List3: Create a list which separates the machine and input elements

List3 = []
a = ''
b = ''
for i in range(0,list2) :
    P = List2[i][0]
    p = len(P)-2
    c = T[i]
    a = [P[13:c]]
    b = [P[c+5:p]]
    List3.append(a)
    List3.append(b)
print("\n List3:" , List3)


# List4: Delete the wrong elements in List3

List4 = []
a = ''
b = ''
list3 = len(List3)
for i in range(0,list3) :
    P = List3[i][0]
    a = P.replace('{','')
    b = [a.replace('}','')]
    List4.append(b)
print("\n List4:", List4)


# List 5: Create an appropriate list which would be used by the TuringMachine programm

list4 = len(List4)
List5 =[]
for i in range(0,list4):
    P = []
    list4=len(List4[i][0])
    for j in range(0,list4):
        if List4[i][0][j] != ',' and List4[i][0][j] != '{' and List4[i][0][j] != '}' :
            P.append(List4[i][0][j])
    List5.append(P)
print("\n List 5:",List5)


# Create a general list of machines and a general list of inputs

list5 = len(List5)
for i in range(0,list5) :
    if i%2 == 0 :
        Machines.append(List5[i])
    else :
        Inputs.append(List5[i])
print("\n Machines:",Machines)
print("\n Inputs:", Inputs)


# Create several lists of machines and inputs

Input1 = Inputs[0]
Input2 = Inputs[1]
Input3 = Inputs[2]
Input4 = Inputs[3]

Machine1 = Machines[0]
Machine2 = Machines[1]
Machine3 = Machines[2]
Machine4 = Machines[3]

print("\n Machine1:", Machine1)
print("\n Machine2:", Machine2)
print("\n Machine3:", Machine3)
print("\n Machine4:", Machine4)

print("\n Input1:", Input1)
print("\n Input2:", Input2)
print("\n Input3:", Input3)
print("\n Input4:", Input4)


# Turing Machine programm

def TuringMachine(M,I) :
    # Separate the different transitions of a machine
    m = len(M)
    C = []
    Mach = []
    for i in range(0,m) :
        if M[i] == 'q' :
            C.append(i)
    c = len(C)
    for i in range(0,c-1) :
        if i%2 == 0 :
            P = M[C[i]:C[i+1]+2]
            Mach.append(P)
    print("\n Machine:",Mach)
    # Do the movements
    r = 0
    mach = len(Mach)
    for i in range(0,mach) :
        if I[0] == Mach[i][2] and Mach[i][1] == '0' :
            I[0] = Mach[i][3]
            if Mach[i][4] == 'R' :
                r = r+1
            else :
                r = r-1
            R = Mach[i][-1]
        for j in range(0, len(I)):
            for k in range(0,mach):
                if Mach[k][1] == R and I[r] == Mach[k][2] :
                    I[r] = Mach[k][3]
                    if Mach[k][4] == 'R' :
                        r = r+1
                    else:
                        r = r-1
                    R = Mach[k][-1]
    print("\n Result:",I," q",R)