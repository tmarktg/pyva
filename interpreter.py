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

keyword = ["print", "var", "for", "}"]


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
        # instruction, expression = line.split()
        if keyword:
            if keyword == "var":
                matches = re.findall("var", program)
                var, val = matches.split('=')
                state[var] = val
            if keyword == "print":
                pattern = rf'{"print"}\((.*?)\)'
                matches = re.findall(pattern, program)[0]
                if "'" in matches:
                    matches = matches.replace("'", "")
                    print(matches)
                    continue
                try:
                    val = varmap(matches, state)
                    print(val)
                except:
                    print("Error: Val not found")

            if keyword == '}':
                continue
            if keyword == 'for':
                pattern = rf'{"for"}\((.*?)\)'
                matches = re.findall(pattern, program)[0]
                matches = matches.replace("'", "")
                var, myRange = matches.split("=")
                # initialize values
                start_val, stop_val = 0
                x = re.findall("<=", matches)
                if x:
                    start_val, stop_val = matches.split(x)
                state[var] = start_val
                for i in range(linenum+1, len(lines)):
                    scanLine = lines[i]
                    stop_line = 0
                    if "}" in scanLine:
                        stop_line = "}"
                    for_body = lines[linenum+1:stop_line]
                    for x in range(int(start_val), int(stop_val)+1):
                        state[var] = x
                        newProgram = "".join(for_body)
                        executeProgram(newProgram)
        else:
            print("Error! Instruction not found")


def readLineByLine(program):
    for line in program.splitlines():
        print(line)


sampleProgram = """var a = 3"""
# readLineByLine(sampleProgram)

executeProgram(sampleProgram)


print('---')
