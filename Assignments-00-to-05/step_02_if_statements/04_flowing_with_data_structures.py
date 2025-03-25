def Three_Data(lists , data):
    for items in range(3):
        lists.append(data)

def main():
    message = input("Enter a message to copy: ")  
    lists = []  

    print("List before:", lists) 
    Three_Data(lists , message)
    print(lists)

if __name__ == "__main__":
    main()            
    