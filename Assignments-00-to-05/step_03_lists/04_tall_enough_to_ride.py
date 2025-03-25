maximum_height = 50
def main():
     while True:
        user = input("Enter Your Height : ")
        if user == "":
            print("Good Bye")
            break
        try :
            user_con = float(user)
            if user_con >= maximum_height:
                print("You are tall enough to ride")
            else:
                print("You are not tall. Please Try may be Next Year")        
        except ValueError:
            print("Please Input Your Height")

            
if __name__ == '__main__':
    main()
        