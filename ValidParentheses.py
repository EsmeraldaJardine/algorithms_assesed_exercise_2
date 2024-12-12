def process_string(s):
    bracket_pairs = {'{': '}', '[': ']', '(': ')'}
    stack = []
    if s == "":
        print("The expression is not valid")
        return
    for bracket in s:
        #pushing opening brackets to stack
        if bracket in bracket_pairs.keys():
            stack.append(bracket)
        else:
            #if closing bracket is found, check the stck is not empty
            if stack == []:
                print("The expression is not valid")
                return
            #check the last element in stack is the opening bracket for the closing bracket
            elif bracket_pairs[stack[-1]] == bracket:
                    stack.pop()
            else:
                print("The expression is not valid")
                return
    #check if stack is empty after intreating through the string
    if stack != []:
        print("The expression is not valid")
    else:
        print("The expression is valid")



def main():
    s = input("Enter a parentheses string: ")
    process_string(s) 
if __name__ == "__main__":
    main()
        
