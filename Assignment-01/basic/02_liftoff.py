import time

def countdown():
    for i in range(10, 0, -1):  
        print(i, end=" ", flush=True) 
        time.sleep(0.5) 
    print("\n🚀 Liftoff!")

if __name__ == '__main__':
    countdown()
