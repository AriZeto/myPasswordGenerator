# Name: Ariel Zeto
# Project: MyPasswordGenerator
# Version 1.0
# Designed for CS361

# Import library and functionality for CLI GUI and rich-content display.
import typer
from rich import print
from rich.table import Table
from rich.console import Console

import secrets # Import library and functionality for secure content.
import string # Import to access ascii content.

###### Necessary as per microservice communication guidelines. ######
import socket

HEADER = 64
PORT = 5051
SERVER = 'localhost'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    """
    This function sends the password over to the microservice.
    Takes the string 'msg' (password generated) as a parameter.
    Returns nothing.
    """
    # Encode the msg to UFT-8 format and store it into variable message
    message = msg.encode(FORMAT)
    # Get the length of the message
    msg_length = len(message)
    # Encode the length
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    print("Sending the message from project to microservice........")
    client.send(send_length)
    print(f"sending the message 1: {send_length}")
    client.send(message)
    print(f"sending the message 2: {message}")

def response():
    """
    This function serves the purpose as the response for the project and microservice implementation.
    Takes no parameters.
    Returns nothing.
    """
    print("entering the response")
    response = client.recv(int(1)).decode(FORMAT)
    print(f"Response: {response}")
    return response
###### Necessary as per microservice communication guidelines. ######

# Global constants.
EASY = 'easy'
MEDIUM = 'medium'
STRONG = 'strong'
VERY_STRONG = 'very strong'

# Define variables that contain all digits, letters, and special characters.
digitCharacters = string.digits
letterCharacters = string.ascii_letters
specialCharacters = string.punctuation

# Define string variable that contains all digits, letters, and special characters.
accessibleCharacters = specialCharacters + letterCharacters + digitCharacters

app = typer.Typer()

# Welcome Screen commands columns
welcomeScreen = Table(title="Startup commands:")
welcomeScreen.add_column("Command", justify="center", style="cyan", no_wrap=True)
welcomeScreen.add_column("Description", justify="left", style="magenta")

# Welcome Screen commands rows
welcomeScreen.add_row("generate", "Generates requested password.")
welcomeScreen.add_row("docs", "View the documentation of the application.")
welcomeScreen.add_row("quit", "Quits the application.")

# Password commands columns
passwordTable = Table(title="Password strength commands:")
passwordTable.add_column("Command", justify="center", style="cyan", no_wrap=True)
passwordTable.add_column("Description", justify="left", style="magenta")

# Password commands rows
passwordTable.add_row("easy", "Generates an easy password (not recommended). (Password length is 8 chars, all lowercase, one number)")
passwordTable.add_row("\nmedium", "\nGenerates a medium password (not recommended). (Password length is 10 chars, all lowercase, one uppercase, one number).")
passwordTable.add_row("\nstrong", "\nGenerates a strong password. (Password length is 16 chars, mix of uppercase and lowercase, few numbers, special character).")
passwordTable.add_row("\nvery strong", "\nGenerates a very strong password. (Password length is 20 chars, mix of uppercase, lowercase, numbers, and special characters).")
passwordTable.add_row("\nspecify", "\nThe user can specify length, as well as how many characters of each type they want.")
passwordTable.add_row("\nask", "\nWhy does a secure password matter? Find out by using this command.")

# Basic commands columns
table = Table(title="myPassGenerator Commands:")
table.add_column("Command", justify="center", style="cyan", no_wrap=True)
table.add_column("Description", justify="left", style="magenta")

# Basic commands rows
table.add_row("get_help", "Provides help with using the software.")
table.add_row("docs", "Provides user documentation (you are on this page)")
table.add_row("faqs", "Provides FAQS to user.")
table.add_row("generate", "Prompt to begin generating password")
table.add_row("quit", "Close the program")

# Advanced commands columns
advScreen = Table(title="Startup commands:")
advScreen.add_column("Command", justify="center", style="cyan", no_wrap=True)
advScreen.add_column("Description", justify="left", style="magenta")

# Advanced commands rows
advScreen.add_row("undo", "Undoes a prior command in the password generator screen")
advScreen.add_row("redo", "Redoes a command in the password generator screen")
advScreen.add_row("credits", "Displays credits for the application")
advScreen.add_row("save", "Saves password to a text file after password is generated.")

# For displaying the table to the console.
console = Console()


# Splash / Welcome Screen. Set as default command.
@app.callback(invoke_without_command=True)
def home():
    """
    This function command is the home screen for the command line based password generator.
    Takes no parameters.
    Returns nothing.
    """
    print("\nWelcome to [bold green]myPassGenerator![/bold green] "
          "\nThis password generator application is designed to be simple to use"
          " and design a secure password for your applications. To get started, we have provided some basic, most common commands.\n")

    # Print table welcome screen commands.
    console.print(welcomeScreen)

    print("\nTo get started, type 'python mypass.py' along with a command. For example, 'python mypass.py docs', "
          "which will take you to the documents page.\n")


@app.command()
def close():
    """
    This function command exits the program.
    Takes no parameters.
    Returns nothing.
    """
    exit()


# Command to see frequently asked questions.
@app.command()
def faqs():
    """
    This function command displays the FAQS of the program.
    Takes no parameters.
    Returns nothing.
    """
    print("\nWelcome to the [bold green]Frequently Asked Questions[/bold green] page for myPassGenerator! "
          "Down below you’ll find common frequently asked questions.")
    print("\n[bold red]Who is this application for?:[/bold red]")
    print("This application is designed to be simple and easy to use. The application’s design methods "
          "were implemented with standard heuristic design techniques. We welcome anyone to use "
          "myPassGenerator, including a range of people with low computer confidence, all the way "
          "through those with high confidence.")

    print("\n[bold red]Why a command-line interface?:[/bold red]")
    print("There are numerous password generators with graphical user interfaces. "
          "While these are great, they can often times be bogged down with a lot of on-screen elements"
          " that may hinder the experience. This application is designed to be as simple and intuitive,"
          " thus it was decided that the application would remain command-line based. "
          "However, a web-application is not out of question.")

    print("\n[bold red]Why should a password be secure?:[/bold red]")
    print("A password should be secure due to the concern of password cracking. "
          "In modern days, your digital footprint contains a lot of weight. This includes banking,"
          " social media, message board discussion, college access, shopping,"
          " and confidential information. Without a secure password (and updating it frequently),"
          " you expose risk to your digital footprint – and can compromise others.")

    print("\n[bold red]How can a password be considered 'strong'?:[/bold red]")
    print("Strong passwords typically consist of letters, numbers, a special character, "
          "and are longer (think 15 to 30 characters).\n")

    # Ask if user would like to return to splash screen.
    userPrompt = input("Would you like to return to the home screen?: Type command 'y' to return, 'n' otherwise. ").lower()
    if userPrompt == "y" or userPrompt == "yes":
        home()


# Command to see  documentation for basic user commands.
@app.command()
def docs():
    """
    This function command presents the documentation of the application.
    Takes no parameters.
    Returns nothing.
    """
    print("\n[bold red]'myPassGenerator' v.0.1.0[/bold red]")
    print("[bold green]Copyright Ariel Zeto, 2023.[/bold green]")
    print('[bold green]Designed for: OSU - CS361 - Software Engineering.[/bold green] \n')
    print("[bold blue]Hello![/bold blue] Welcome to the Documentation page.")
    print("Within this page, you will come across the documentation of this application.")
    print("Here is a short list of basic user commands: \n")

    # Displays the table of commands available to the user.
    console.print(table)

    # Remind user that advanced options are available.
    print("Reminder: Advanced command options: Try the command 'advDocs' if you'd like to see advanced user commands.\n")

    # Ask if user would like to go to password generator screen.
    passPrompt = input("Would you like to try generating a password: Type command 'y' to return, 'n' otherwise. ").lower()
    if passPrompt == "y" or passPrompt == "yes":
        generate()


# Command to see  documentation for advanced user commands.
@app.command()
def advDocs():
    """
    This function command displays the advanced documentation of the application.
    Takes no parameters.
    Returns nothing.
    """
    print('\n These commands are typically used within the application "generate" functionality. Use responsibly. \n')

    # Displays the advanced table of commands that are available.
    console.print(advScreen)

    # Ask if user would like to go to password generator screen.
    passPrompt = input(f"\nWould you like to try generating a password: Type command 'y' to return, 'n' otherwise. ").lower()
    if passPrompt == "y" or passPrompt == "yes":
        generate()


def sendPasswordToServer(userPassword):
    """
    This function sends a password to the server, necessary for the project and microservice to communicate.
    Takes the user's password generated as a parameter.
    Returns nothing.
    """
    send(userPassword)
    server_response = response()
    print(f"Response from server: {server_response}")


def createPassword(strength, passwordLength, wantUpper=False, wantSpecial=False):
    """
    This function creates the password.
    Takes parameters - Strength (string, based on user input), passwordLength (int, based on Strength), wantUpper & wantSpecial (bool).
    Returns the Password (string).
    """
    while True:
        userPassword = ""
        for i in range(passwordLength):
            userPassword += ''.join(secrets.choice(accessibleCharacters))
        if isValidPassword(userPassword, strength, wantUpper, wantSpecial):
            break
    print(f"{userPassword}\n")
    sendPasswordToServer(userPassword)
    return userPassword


def wantUpperCase():
    """
    This function provides an input asking if the user wants their password to contain uppercase characters.
    Takes no parameters.
    Returns string.
    """
    getUpperCond = input("\nDo you want your password to contain uppercase characters?: Submit 'y', otherwise press any key. ").lower()
    return getUpperCond == 'y' or getUpperCond == 'yes'


def wantSpecialChars():
    """
    This function provides an input asking if the user wants their password to contain special characters.
    Takes no parameters.
    Returns string.
    """
    getSpecialCond = input("\nDo you want your password to contain special characters?: Submit 'y', otherwise press any key. ").lower()
    return getSpecialCond == 'y' or getSpecialCond == 'yes'


def isValidPassword(userPassword, strength, wantUpper, wantSpecial):
    """
    This function checks if the password is valid.
    Takes parameters - userPassword (string, generated password), strength (string, selected strength), wantUpper & wantSpecial (str, based on inputs).
    Returns number of digits, special characters, validity of password in general.
    """
    numOfDigits = sum(char in digitCharacters for char in userPassword)
    numOfSpecialChars = sum(char in specialCharacters for char in userPassword)
    numOfUppercase = sum(char.isupper() for char in userPassword)
    if strength == EASY:
        return numOfDigits == 1 and userPassword.islower() and numOfSpecialChars == 0
    elif strength == MEDIUM:
        return numOfDigits == 1 and numOfUppercase >= 4 and numOfSpecialChars == 0
    elif strength == STRONG:
        return numOfDigits > 3 and numOfSpecialChars == 1
    elif strength == VERY_STRONG:
        return numOfDigits > 5 and numOfSpecialChars > 4
    else:
        upperCaseCondition = numOfUppercase > 0 if wantUpper else numOfUppercase == 0
        specialCharsCondition = numOfSpecialChars > 0 if wantSpecial else numOfSpecialChars == 0
        return numOfDigits >= 3 and upperCaseCondition and specialCharsCondition


def promptPasswordLength():
    """
    This function prompts the user for a password length (between 8 and 50 characters).
    Takes no parameters.
    Returns passwordLength (int).
    """
    while True:
        try:
            passwordLength = int(input("\nEnter in the number of characters you want the password to be (8 and 50 characters): "))
            while passwordLength < 8 or passwordLength > 50:
                passwordLength = int(input("Error: Please choose a number between 8 and 50 for your password length...Try again: "))
        except ValueError:
            print("Number must be an integer - please try again.")
            continue
        return passwordLength


def promptPasswordStrength():
    """
    This function prompts the user asking them how strong they want their password to be.
    Takes no parameters.
    Returns string input.
    """
    getInput = input("\nWhat strength do you want your new password to be?: ").lower()
    # Reliability purposes, allows user to enter 'y' to generate a default response (strong password).
    if getInput == 'y' or getInput == 'yes':
        getInput = 'strong'
    return getInput


def promptToGoHome():
    """
    This function asks if the user would like to return home.
    Takes no parameters.
    Returns nothing.
    """
    askGoHome = input(f"Would you like to return home? Type 'y' to continue, otherwise any other key: ").lower()
    if askGoHome == 'y' or askGoHome == 'yes':
        home()


def displayGenerateWelcomeScreen():
    """
    This function generates the welcome screen.
    Takes no parameters.
    Returns nothing.
    """
    print("\n You have selected the option to generate a secure password. "
          "You will be asked a prompt for how strong you wish the PASSWORD STRENGTH to be.\n\n")
    console.print(passwordTable)  # Displays table to the console.


def generateSpecificPassword(strength):
    """
    This function generates a specific password based on queries.
    Takes password strength as a parameter.
    Returns nothing.
    """
    passwordLength = promptPasswordLength()
    createPassword(strength, passwordLength, wantUpperCase(), wantSpecialChars())
    promptToGoHome()


def generatePasswordOfStrength(strength):
    """
    This function generates a password of a particular strength, whereas strength is the passed in parameter.
    Takes password strength as a parameter.
    Returns nothing.
    """
    print(f"\nYou have selected '{strength}'. Generating password…: \n")
    strengthToLength = {EASY: 8, MEDIUM: 10, STRONG: 16, VERY_STRONG: 20}
    createPassword(strength, strengthToLength[strength])


# Command to begin generating password.
@app.command()
def generate():
    """
    This command generates the password.
    Takes no parameters.
    Returns nothing.
    """
    displayGenerateWelcomeScreen()
    while True:
        getInput = promptPasswordStrength()
        if getInput in [EASY, MEDIUM, STRONG, VERY_STRONG]:
            generatePasswordOfStrength(getInput)
            break
        elif getInput == "specify":
            generateSpecificPassword(getInput)
            break
        elif getInput == "ask":
            print("\nHaving a secure password is absolutely necessary for securing your digital life. A secure password protects unauthorized users and hackers from accessing any personal "
                  "information that you store in the account. The stronger your password is, the more secure the information in the account remains.\n")
            break
        else:
            print("Invalid input. Please enter in a valid password generator command. ")


if __name__ == "__main__":
    app()