import threading

size = 50

def Display(func, lock1):
	func(lock1)

def thread1(lock1):
	lock1.acquire()
	global size
	
	print("Display 1 to 50 numbers")
	
	for i in range(size):
		print(i+1)

	lock1.release()

def thread2(lock1):
	lock1.acquire()
	global size
	value = size
	
	print("Display 50 to 1 numbers")
	
	for i in range(size):
		print(value - i)
		
	lock1.release()
	
def main():
	print("Inside main")
	
	lock1 = threading.Lock()
	t1 = threading.Thread(target = Display ,args = (thread1,lock1,))
	t2 = threading.Thread(target = Display ,args = (thread2,lock1,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

if __name__ == "__main__":
	main()
