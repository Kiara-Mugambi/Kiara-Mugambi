import time

def login_system():
	username = "admin"
	password = "secure123"
	time = 10

	while True:
		attempts=0

		while attempts <3:
			entered_username = input("Enter your username: ")
			entered_password = input("Enter your password: ")

			if entered_username == username and entered_password == password:
				print("Login Successfull!")
				return

			else:
				attempts +=1
				print(f"Incorrect Credentials. {3 - attempts} attempts left.")

		if attempts == 3:
			print(f"Too many attempts. Please try again after {time} seconds")
			time.sleep(time * 60)

login_system()
