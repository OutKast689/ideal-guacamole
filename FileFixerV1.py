import os

from Tools.scripts.ndiff import fopen

invNum = open("InvalidNumbers.txt")
ogNum = fopen("C:\\Users\\eliana.lopez\\OneDrive - JANUS Research Group, LLC\\RealisticExtrema.txt")
fixedNum = open("fixedNumbers.txt", "w")


def fixerUpper():
    with invNum:
        for line in invNum:
            line = line.strip()
            if (len(line)) == 14:
                line = line.replace(line[:2], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')
                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 15:
                line = line.replace(line[:3], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')
                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 16:
                line = line.replace(line[:4], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')
                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 17:
                line = line.replace(line[:5], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')
                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 18:
                line = line.replace(line[:6], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')
                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 19:
                line = line.replace(line[:7], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')

                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 20:
                line = line.replace(line[:8], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')

                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 21:
                line = line.replace(line[:9], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')

                    else:
                        print("invalid: " + str(line))
            if (len(line)) == 22:
                line = line.replace(line[:10], '')
                if len(line) == 12:
                    line = line.replace('/', '')
                    line = line.replace('-', '')
                    if int(len(line)) == 10:
                        fixedNum.write(line + '\n')

                    else:
                        print("invalid: " + str(line))
    os.startfile('fixedNumbers.txt')
