no=str(input("Enter mobile no:"))
if no.isdigit():
    if len(no)==10:
        if no.startswith('6') or no.startswith('7') or no.startswith('8') or no.startswith('9') :
            print("Valid Mobile no")
        else:
            print("This no doesn't exist fron India")
    else:
        print("Please 10 digit only")
        
else:
    print("Please enter no in digit format only")
    