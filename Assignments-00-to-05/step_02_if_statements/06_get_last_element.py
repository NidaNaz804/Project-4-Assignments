def Last_Number(lst):
    return lst[-1] 

def Get_list():
    lst = [] 
    user_input = input("Enter Your Text here: ")
    
    while user_input != "":
        lst.append(user_input)
        user_input = input("Enter Your Text here: ")
    
    return lst 

def Main():
    user_list = Get_list()  
    print("Last element:", Last_Number(user_list)) 

if __name__ == '__main__':
    Main()
