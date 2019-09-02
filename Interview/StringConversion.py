'''The 'a' key on the keyboard is not working correctly. Instead of typing 'a' or 'A', it toggles the CapsLock. 
Return the value of a string that is typed into a keyboard on such a faulty keyboard.
Note: If shift is pressed when CapsLock is on characters will be printed in lower case

e.g. 
Input: "Help, my keyboard is not working"
Output: "Help, my keyboRD IS NOT WORKING"

Input: "Hi my name is Adam Levine"
Output: "Hi my nME IS dM lEVINE"
'''



def StringConversion(StringInput):
    StringOutput = ''
    val = 0
    for i in StringInput:
        if (i=='a' or i=='A'):
            if val==1:
                val=0
            else:
                val = 1
            continue
        
        if val==1:
            if (i.isupper()):
                StringOutput = StringOutput +  i.lower()
            else:
                StringOutput = StringOutput + i.upper()
        else:
            StringOutput = StringOutput + i
            
        
    return StringOutput  

 
StringInput = "Hi my name is Adam Levine"
StringConversion(StringInput)
