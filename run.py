import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey-result')




def get_survey_data():
    """
    Get survey data input from user and update the Google Sheets spreadsheet.
    """
    print("Please enter your Name")
    NAME = str.capitalize(input("Name:\n "))
    print("Please enter your Age")
    AGE = int(input("Age:\n "))
    print("Please enter your Gender:")
    GENDER = str.capitalize(input("Gender:\n "))
    print("Please give your Rating")
    while True:
        try:
            RATING = int(input("Rating: "))
            if RATING > 5:
                raise ValueError("Rating cannot be greater than 5")
            break  # Exit the loop if valid rating entered
        except ValueError:
            print("Rating cannot be greater than 5")
            print("Invalid rating. Please enter a valid rating.")
    return NAME, AGE, GENDER, RATING


def update_sheet(name, age, gender, rating):
    """
    Update the Google Sheets spreadsheet with survey data.
    """
    # Open the first sheet of the spreadsheet
    sheet = SHEET.get_worksheet(0)
    
    # Append the survey data to the spreadsheet
    new_row = [name, age, gender, rating]
    sheet.append_row(new_row)
    
    print(f"Your name is: {name}, Your gender is: {gender}, Your age is: {age}, Your rating is: {rating}")
    print("Survey data appended to the spreadsheet.")

if __name__ == "__main__":
    main()  
