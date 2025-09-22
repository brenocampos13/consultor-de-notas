# Code a Grade Consultant for any student's name and grade!
# Return the grade and say if student's is approved, is in recovery or rejected!

print("==================")
print("GRADE CONSULTANT")
print("==================")

while True:
        name = input("Enter the student's name: ")
        try:
            searchStudent = float(input("Enter the student's grade: "))
            if searchStudent < 0 or searchStudent > 10.1:
                print("The number must to be greater than 0 and less than 10, try again!")
                continue
            elif searchStudent < 5.1:
                print(f'The student {name} failed due to his {searchStudent} grade!')
            elif searchStudent < 7.1:
                print(f'The student {name} is in recovery due to his {searchStudent} grade!')
            else:
                print(f'The student {name} was approved based on his {searchStudent} grade!')
        except ValueError:
            print('Enter a valid number!')
            continue
        
        while True:
            tryAgain = input("Do you want to search again? Y/N: ").strip().upper()
            if tryAgain in ["yes", "YES", "Y", "y"]:
                break
            elif tryAgain in ["N", "No", "NO", "n"]:
                print("=============================================")
                print("THANKS FOR USING THE GRADE CONSULTANT!")
                print("=============================================")
                exit()
            else:
                (print("Invalid Answer! Enter YES or NO!"))
                continue
