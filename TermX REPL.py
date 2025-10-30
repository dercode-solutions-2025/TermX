import sys
import os
import platform

tempvars = []

def evaluate_condition(condition):
    if "==" in condition:
        var, val = condition.split("==", 1)
        var = var.strip()
        val = val.strip()
        if var in tempvars:
            index = tempvars.index(var)
            if index + 1 < len(tempvars):
                return tempvars[index + 1] == val
        return False
    else:
        var = condition.strip()
        if var in tempvars:
            index = tempvars.index(var)
            if index + 1 < len(tempvars):
                return bool(tempvars[index + 1])
        else:
            return True
    return False

def execute_command(line):
    global tempvars
    if 'if_stack' not in globals():
        globals()['if_stack'] = []
    if 'skip_block' not in globals():
        globals()['skip_block'] = False

    line = line.strip()

    if line.startswith("if | "):
        condition = line.replace("if | ", "").strip()
        if_cond = evaluate_condition(condition)
        globals()['if_stack'].append(if_cond)
        globals()['skip_block'] = not if_cond
        return

    elif line == "else |":
        if globals()['if_stack']:
            current = globals()['if_stack'][-1]
            globals()['skip_block'] = current
            globals()['if_stack'][-1] = not current
        return

    elif line == "endif":
        if globals()['if_stack']:
            globals()['if_stack'].pop()
        if not globals()['if_stack']:
            globals().pop('skip_block', None)
        return

    if globals().get('skip_block', False):
        return

    if line.startswith("uvar | "):
        line = line.replace("uvar | ", "").strip()
        parts = line.split()
        tempvars = parts if parts else []

    elif line.startswith("displaytext | "):
        line = line.replace("displaytext | ", "").strip()
        line = line.replace('"', "")
        print(line)

    elif line.startswith("readinput | "):
        line = line.replace("readinput | ", "").strip()
        line = line.replace('"', "")
        input(line)

    elif line.startswith("printput | "):
        line = line.replace("printput | ", "").strip()
        line = line.replace('"', "")
        print(input(f"""{line}
"""))

    elif line.startswith("displayvar | "):
        print(", ".join(tempvars))

    elif line.startswith("easteregg"):
        print("error -> solvable.issue -> nobody likes you.")

    elif line.startswith("displayfile | "):
        line = line.replace("displayfile | ", "").strip()
        try:
            with open(line, "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"error -> name.error -> {line} was not found.")
        except Exception as e:
            print(f"Error -> {e}")

    elif line.startswith("writefile | "):
        line = line.replace("writefile | ", "").strip()
        parts = line.split(":", 1)
        if len(parts) > 1:
            filename = parts[0]
            content_to_write = parts[1]
            try:
                with open(filename, "w") as file:
                    file.write(content_to_write)
            except Exception as e:
                print(f"Error -> {e}")
        else:
            print("error -> syntax.error -> writefile requires a filename and content, separated by a colon (e.g., writefile | filename:content).")

    elif line.startswith("runtx | "):
        line = line.replace("runtx | ", "").strip()
        try:
            with open(line, "r") as file:
                for script_line in file:
                    execute_command(script_line)
        except FileNotFoundError:
            print(f"error -> name.error -> {line} was not found.")
        except Exception as e:
            print(f"Error -> {e}")

    elif line == "exitrepl":
        sys.exit()

    elif line.startswith("addint | "):
        line = line.replace("addint | ", "").replace(" ", "")
        digits = [int(digit) for digit in line]
        total_sum = sum(digits)
        print(total_sum)

    elif line.startswith("convertctf | "):
        line = line.replace("convertctf | ", "").replace(" ", "")
        celsius = float(line)
        fahrenheit = (celsius * 9/5) + 32
        print(f"{fahrenheit:.2f}")

    elif line.startswith("help "):
        line = line.replace("help ", "")
        if "runtx" in line:
            print("runtx runs a .termx file, simply enter the target directory.")
        if "exitrepl" in line:
            print("exitrepl exits the TermX REPL.")
        if "writefile" in line:
            print("writefile writes text to a file in this format: writefile | filename:content")
        if "uvar" in line:
            print("uvar creates a temporary variable with an associated value. When uvar is used again, the previous variable is replaced.")
        if "displaytext" in line:
            print("displaytext displays the text associated with it (eg. 'Hello world!')")
        if "readinput" in line:
            print("readinput reads input from the user of the associated value (eg. 'What is 2+2?')")
        if "displayvar" in line:
            print("displayvar displays a variable by its name.")
        if "printput" in line:
            print("printput prints user input.")
        if "displayfile" in line:
            print("displayfile displays a file. Simply enter the file directory.")
        if "dispmachine" in line:
            print("dispmachine displays system information.")

    elif line.startswith("dispmachine"):
        print(os.name)
        print(platform.system())
        print(platform.machine())
        print(platform.version())
        print(platform.release())

while True:
    line = input(" ")
    execute_command(line)
