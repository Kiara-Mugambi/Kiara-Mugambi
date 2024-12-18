def take_attendance():
	students = ["Alice", "Bob", "Charlie", "Diana"]
	attendance = {}


	for student in students:
		status = input(f"Is {student} present? (yes/no):").lower()
		attendance[student] = "Present" if status == "yes" else "Absent"

	with open("attendance.txt", "w") as file:
		for student, status in attendance.items():
			file.write(f"{student}: {status}\n")
	print("Attendance saved successfully")

def check_attendance():
	try:
		with open("attendance.txt", "r") as file:
			print("Attendance Record:")
			for line in file:
				print(line.strip())
	except FileNotFoundError:
			print("No attendance record found. Please take attendance")

while True:
	print("\nAttendance Tracker")
	print("1. Take Attendance")
	print("2. Check Attendance")
	print("3. Exit")
	choice = input("Enter your choice: ")

	if choice == "1":
		take_attendance()
	elif choice == "2":
		check_attendance()
	elif choice == "3":
		print("Exiting the system")
		break
	else:
		print("Invalid choice. Please try again")
