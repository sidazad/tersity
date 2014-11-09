import fileinput
import traceback


verbs = ["show", "call"]
# separator used to separate var name and type for ex. signup:popup
type_sep = ":"

try:
    for line in fileinput.input("../data/sample1.txt"):
        for c in line:
            if c == '\t':
                print "tab"
            else:
                print c

except Exception, ex:
    print ex.__str__()
    traceback.print_exc()