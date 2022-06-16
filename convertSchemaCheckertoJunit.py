from junit_xml import TestSuite, TestCase
import sys

# input file name with extension
file = sys.argv[1]

# using try catch except to
# handle file not found error.
  
# entering try block
try:
  
    result1 = "PASSED"
    result2 = "DEFERRED"
    result3 = "FAILED"
    result4 = "NOT PROCESSED"

    # opening and reading the file 
    file_open = open(file, 'r', errors='ignore')
      
    # reading file content line by line.
    lines = file_open.readlines()

    test_cases = []

    # looping through each line in the file
    for line in lines:
        
        # if line have the input string, get the index 
        # of that line and put the
        # line into newly created list 
        if result1 in line:
            word = line.split(" ")
            try:
                test_cases.append(TestCase(word[3] + " " + word[4], status=word[1], log=line))
            except:
                continue
        if result2 in line:
            word = line.split(" ")
            try:
                test_cases.append(TestCase(word[1] + " " + word[2], status=word[0], log=line ))
            except:
                continue
        if result3 in line:
            word = line.split(" ")
            try:
                test_cases.append(TestCase(word[3] + " " + word[4], status=word[1], log=line))
            except:
                continue
        
    # closing file after reading
    file_open.close()
    
    with open('schemaCheckerResults.xml', 'w', errors='ignore') as f:
         ts = TestSuite("UCI Schema Checker Results", test_cases)
         TestSuite.to_file(f, [ts])

    f.close()

    # fix bug in library
    with open("schemaCheckerResults.xml") as f:
        lines = f.readlines()

    lines[1] = "<testsuites>\n"

    with open("schemaCheckerResults.xml", "w") as f:
        f.writelines(lines)


except Exception as e:
    print(e)
    print("\nThe schemaCheckerResults file doesn't exist!")
