import copy

class CFGSymbol(object):
    def __init__(self):
        self.type = "null" # [terminal | variable]
        self.value = ""

class CFGProduction(object):
    def __init__(self):
        self.name = ""
        self.result = []

def generate_cnf () -> (list, list):
    # FILE MANAGER
    fin = ""
    fileFound = False;
    while not fileFound:
        try:
            fin = open(input("Read from file: "))
        except FileNotFoundError:
            print("File is not found. Check to see if you typed in the correct file and try again.")
            fileFound = False
        else:
            fileFound = True


    # READ CFG
    cfg = []
    lines = fin.readlines()
    for line in lines:
        tokens = line.split(" ")
        production = CFGProduction()
        for token in tokens:
            if (production.name == ""):
                production.name = token
            elif (token == "->" or token == "\n"):
                pass
            elif (token == "|"):
                name = production.name
                cfg.append(production)
                production = CFGProduction()
                production.name = name
            else:
                if (len(token) > 0):
                    if (token[0] == "\"" or token[0] == "\'"):
                        insertVal = token
                        insertVal = insertVal.replace("\n", "")
                        result = CFGSymbol()
                        result.type = "terminal"
                        result.value = insertVal[1:-1]
                        production.result.append(result)
                    else:
                        insertVal = token
                        insertVal = insertVal.replace("\n", "")
                        result = CFGSymbol()
                        result.type = "variable"
                        result.value = insertVal
                        production.result.append(result)
        cfg.append(production)
    fin.close()


    # STEP 1: START
    print("----- STEP 1: ADDING START STATES -----")
    startProd = CFGProduction()
    startProd.name = "S0"
    startProdResult = CFGSymbol()
    startProdResult.type = "terminal"
    startProdResult.value = cfg[0].name
    startProd.result.append(startProdResult)
    cfg.insert(0, startProd)
    print(startProd.name, "->", startProdResult.value)
    print("\n\n")


    # STEP 2: TERM
    print("STEP 2: REMOVE TERMINAL + VARIABLE PRODUCTIONS")
    for prod in cfg:
        for result in prod.result:
            if (result.type == "terminal" and len(prod.result) != 1):
                print(prod.name, "->", prod.result[0].value, end=" ")
                for i in range(len(prod.result) - 1):
                    print(prod.result[i + 1].value, end=" ")
                print()
                
                newProd = CFGProduction()
                newProd.name = "Term" + result.value
                newProd.result.append(CFGSymbol())
                newProd.result[0].type = "terminal"
                newProd.result[0].value = result.value
                cfg.append(newProd)
                result.type = "variable"
                result.value = newProd.name

                print("\t", prod.name, "->", prod.result[0].value, end=" ")
                for i in range(len(prod.result) - 1):
                    print(prod.result[i + 1].value, end=" ")
                print("\n")
    print("\n")

    # STEP 3: BIN
    print("STEP 3: SPLITTING PRODUCTIONS", end = "")
    binString = 0
    for prod in cfg:
        if (len(prod.result) > 2):
            print()
        while (len(prod.result) > 2):
            print(prod.name, "->", prod.result[0].value, end=" ")
            for i in range(len(prod.result) - 1):
                print(prod.result[i + 1].value, end=" ")
            print()

            newProd = CFGProduction()
            newProd.name = "Bin" + str(binString)
            binString += 1
            newProd.result.append(CFGSymbol())
            newProd.result[0].type = "variable"
            newProd.result[0].value = prod.result[-2].value
            newProd.result.append(CFGSymbol())
            newProd.result[1].type = "variable"
            newProd.result[1].value = prod.result[-1].value
            cfg.append(newProd)
            prod.result.pop()
            prod.result.pop()
            prod.result.append(CFGSymbol())
            prod.result[-1].type = "variable"
            prod.result[-1].value = newProd.name
            
            print("\t", prod.name, "->", prod.result[0].value, end=" ")
            for i in range(len(prod.result) - 1):
                print(prod.result[i + 1].value, end=" ")
            print()
            print("\t", newProd.name, "->", newProd.result[0].value, newProd.result[1].value)
    print("\n\n")

    # STEP 4: DEL
    print("STEP 4: REMOVING EPSILON PRODUCTIONS")
    epsilonless = False
    while not epsilonless:
        epsilonless = True
        for prod in cfg:
            for result in prod.result:
                if result.type == "variable" and result.value == "e":
                    print(prod.name, "->", prod.result[0].value, end=" ")
                    for i in range(len(prod.result) - 1):
                        print(prod.result[i + 1].value, end=" ")
                    print()

                    prod.result.remove(result)

                    if (len(prod.result) > 0):
                        print("\t", prod.name, "->", prod.result[0].value, end=" ")
                        for i in range(len(prod.result) - 1):
                            print(prod.result[i + 1].value, end=" ")
                        print()
            if len(prod.result) == 0:
                epsilonless = False
                for delEProd in cfg:
                    for delERes in delEProd.result:
                        if delERes.type == "variable" and delERes.value == prod.name:
                            print(delEProd.name, "->", delEProd.result[0].value, end=" ")
                            for i in range(len(delEProd.result) - 1):
                                print(delEProd.result[i + 1].value, end=" ")
                            print()

                            delERes.value = "e"

                            print("\t", delEProd.name, "->", delEProd.result[0].value, end=" ")
                            for i in range(len(delEProd.result) - 1):
                                print(delEProd.result[i + 1].value, end=" ")
                            print()
                cfg.remove(prod)
    print("\n\n")

    # STEP 5: UNIT
    print("STEP 5: REMOVING UNIT PRODUCTIONS")
    unitless = False
    while not unitless:
        unitless = True
        deleteBuffer = []
        for prod in cfg:
            if len(prod.result) == 1 and prod.result[0].type == "variable":
                print(prod.name, "->", prod.result[0].value + ":")
                unitless = False
                delName = prod.result[0].value
                prod.result.pop()
                for delUProd in cfg:
                    if delUProd.name == delName:
                        if len(delUProd.result) == 0:
                            deleteBuffer.append(delUProd)
                        else:
                            newProd = CFGProduction()
                            newProd.name = prod.name
                            newProd.result = copy.deepcopy(delUProd.result)
                            print("\t", newProd.name, "->", newProd.result[0].value, end=" ")
                            if (len(newProd.result) == 2):
                                print(newProd.result[1].value)
                            else:
                                print()
                            cfg.append(newProd)
                deleteBuffer.append(prod)
                print()
        for item in deleteBuffer:
            if (item in cfg):
                cfg.remove(item)
    print("\n")

    # STEP 6: REMOVE DUPES
    print("STEP 6: REMOVING DUPLICATES")
    for prod in cfg:
        for prod2 in cfg:
            if prod is not prod2:
                if (prod.name == prod2.name):
                    if (len(prod.result) == len(prod2.result)):
                        isExact = True;
                        for i in range(len(prod.result)):
                            if prod.result[i].value != prod2.result[i].value:
                                isExact = False
                                break
                            if prod.result[i].type != prod2.result[i].type:
                                isExact = False
                                break
                        if isExact:
                            print(prod2.name, "->", prod2.result[0].value, end=" ")
                            if (len(prod2.result) == 2):
                                print(prod2.result[1].value)
                            else:
                                print()
                            cfg.remove(prod2)
    print("\n\n")

    # STEP 7: SORT
    print("STEP 7: SORTING")
    cfg.sort(key = lambda x:x.name)
    print("\n\n")
    term = []
    var = []
    for prod in cfg:
        if len(prod.result) == 1:
            term.append(prod)
        else:
            var.append(prod)
    return (term, var)


if __name__ == "__main__":
    term, var = generate_cnf()
    fileFound = False;
    fout = "";
    while not fileFound:
        try:
            fout = open(input("Export to file: "), mode="w+")
        except FileNotFoundError:
            print("File is not found. Check to see if you typed in the correct file and try again.")
            fileFound = False
        else:
            fileFound = True
    # PRINT RESULT
    print("TERIMINAL:")
    for x in term:
        writeStringToFile = x.name + " -> " + x.result[0].value
        for y in x.result[1:]:
            writeStringToFile += " " + y.value
        writeStringToFile += " "
        print(writeStringToFile)
        fout.write(writeStringToFile + "\n")
    print()

    print("VARIABLE:")
    for x in var:
        writeStringToFile = x.name + " -> " + x.result[0].value
        for y in x.result[1:]:
            writeStringToFile += " " + y.value
        writeStringToFile += " "
        print(writeStringToFile)
        fout.write(writeStringToFile + "\n")
    fout.close()