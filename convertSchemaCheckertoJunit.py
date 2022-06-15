from junit_xml import TestSuite, TestCase

# input file name with extension
file = '..\\..\\build\\checker\\SchemaCheckerResults.txt'
# using try catch except to
# handle file not found error.
  
# entering try block
try:
  
    result1 = "PASSED"
    result2 = "DEFERRED"
    result3 = "FAILED"
    result4 = "NOT PROCESSED"

    # opening and reading the file 
    file_open = open(str(file), 'r', errors='ignore')
      
    # asking the user to enter the string to be 
    # searched
     
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
                test_cases.append(TestCase(word[3] + " " + word[4], 'UCI Schema', 0, line, word[0]))
            except:
                continue
        if result2 in line:
            word = line.split(" ")
            try:
                test_cases.append(TestCase(word[1] + " " + word[2], 'UCI Schema', 0, line, word[0]))
            except:
                continue
        if result3 in line:
            word = line.split(" ")
            try:
                test_cases.append(TestCase(word[3] + " " + word[4], 'UCI Schema', 0, line, word[0]))
            except:
                continue
        
    # closing file after reading
    file_open.close()
    with open('schemaCheckResults.xml', 'w', errors='ignore') as f:
        ts = TestSuite("UCI Schema Checker Test Suite", test_cases)
        TestSuite.to_file(f, [ts], prettyprint=False)

except Exception as e:
    print(e)
    print("\nThe schemaCheckerResults file doesn't exist!")

