import re
# platelist = list()                    # Malo

def platesformat(txt):
    # stuff = re.findall('^[A-Z]{3}\s[0-9]{2}[A-Z0-9]',txt)
    stuff = re.findall('^[A-Z]{3}.[0-9]{2}[A-Z0-9]',txt)
    # if len(stuff) !=1: continue       # Malo
    for i in stuff:
        plate = str(stuff[0])
        # platelist.append(plate)       # Malo
        # print(platelist)              # Malo
        print(plate, "reg-exp")
        return(plate)

# platesformat("a")
# platesformat("QAZsb")
# platesformat("AaaQWA")
# platesformat("AAA 123")
# platesformat("AAA 12A")
# platesformat("AAAA12A")
