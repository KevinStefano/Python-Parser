symbol = ['{', '}', '(', ')', '[', ']', '.', '"', ',']
operator = ['+','-',':','*','/','=','>','<','?','|','&','^','%','$','#','!']
KEY= symbol+operator

space = ' '
conc = ''
list = []

string = '''
public class Test {

    5+8
    print(5+8)
   public static void main(String args[]) {

'''
for i,y in enumerate(string):
    if y != '\n' and y != space :
        conc += y
    if (i+1 < len(string)): 
        if string[i+1] == space or string[i+1] in KEY or conc in KEY: # if next y == ' '
            if conc != '':
                list.append(conc)
                conc = ''

print(list)
