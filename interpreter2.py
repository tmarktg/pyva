import re
# implement a simple interpreter that understands the following
# two statement types:

# For now, just accept the program as a
# String called testProgram

# 1. Assignments
# ASSIGN {var}={val}
# Example: ASSIGN X=4
# These types of statements define a variable

# 2. Prints
# PRINT {var}
# Example PRINT X
# These types of statements will print the current variable
# at that state

# def varmap(targetVar, s):
#     for mapping in s:
#         var, val = mapping[0], mapping[1]
#         if targetVar == var:
#             return val
#     raise ValueError("Variable not found")


def varmap(targetVar, state):
    if targetVar in state:
        return state[targetVar]
    else:
        raise ValueError("Error: Var not found")


state = dict()


def executeProgram(program):
    loop_start_linenum = 0

    lines = program.splitlines()
    lines = list(lines)

    for linenum, line in enumerate(lines):
        instruction, expression = line.split()

        if instruction == "var":
            var, val = expression.split('=')
            state[var] = val
        elif instruction == "print":
            if "'" in expression:
                printed_string = expression.replace("'", "")
                a = printed_string.replace("(", "")
                b = a.replace(")", "")
                print(b)
                continue
            try:
                if "(" in expression:
                    printed_string = expression.replace("(", "")
                    a = printed_string.replace(")", "")
                    val = varmap(a, state)
                    print(val)
            except:
                print("Error: Val not found")
        elif instruction == "NEXT":
            continue
        elif instruction == "for":
            expression = expression.replace(":", "")
            var, myRange = expression.split("=")
            start_val, stop_val = myRange.split(",")
            state[var] = start_val
            for i in range(linenum+1, len(lines)):
                scanLine = lines[i]
                stop_line = 0
                if "NEXT" in scanLine:
                    stop_line = i
                for_body = lines[linenum+1:stop_line]
                for x in range(int(start_val), int(stop_val)+1):
                    state[var] = x
                    newProgram = "".join(for_body)
                    executeProgram(newProgram)
        else:
            print("Error! Instruction not found")


sampleProgram = """ASSIGN X=4
ASSIGN Y=5
PRINT X
PRINT Y
PRINT X
PRINT Z
ASSIGN Z=10
ASSIGN _=2+X/3*Y
Woo hoo!
PRINT X
PRINT Z
PRINT _
"""

fizzBuzz = """ASSIGN I = 0

FOR I FROM 1 TO 100:
    IF I % 15 == 0:
        PRINT 'FizzBuzz'
    ELIF I % 3 == 0:
        PRINT 'Fizz'
    ELIF I % 5 == 0:
        PRINT 'Buzz'
    ELSE:
        PRINT I
    END_IF
    I++
END_FOR
"""

# while_loop = """
# """

for_loop = """for (I=1; I<=100; I++):
print (I)
NEXT I
"""

print_vars = """var I=3
print (I)
"""

print_words = """print ('fizz')"""

prints = print_vars + print_words

if_statement = """
"""

label_and_jump = """
ASSIGN i = 0
i++
Label1:
PRINT i
JUMP Label1
"""


def readLineByLine(program):
    for line in program.splitlines():
        print(line)

# readLineByLine(sampleProgram)


print('---')

# print(prints)

# executeProgram(prints)

executeProgram(print_vars)
