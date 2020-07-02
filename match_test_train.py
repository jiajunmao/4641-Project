import os
import sys

path = sys.argv[1]
f = open("match_test_train.sh", "w")
f.write("#!/bin/bash\n")

classes = []
i=0

for root, subdirs, files in os.walk(path + "Training"):    
    # print("folder ", root)
    current_class = root[root.rfind("Training/") + 9:]
    print(current_class)
    classes.append(current_class)

for root, subdirs, files in os.walk(path + "Test"):    

    current_class = root[root.rfind("Training/") + 9:]
    if current_class not in classes:
        f.write("rm -r \"datasets" + current_class + "\";\n")

f.close()

