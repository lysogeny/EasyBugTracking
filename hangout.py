import webbrowser
import time
import bug_tracking

def yes_no(variable):
    yn = False
    if variable == "y" or variable == "n":
        yn = True
    
    return yn

def experience_rating():
    rating_good = False

    while True:
        prior_experience = input("Do you like spending time with emilyOS? y/n \n")
        if not yes_no(prior_experience):
            print("Your input was invalid. Please try again!")
        else:
            break

    while True:
        future_outlook = input("Would you like to spend more time with emilyOS? 👉👈 y/n \n")
        if not yes_no(future_outlook):
            print("Your input was invalid. Please try again!")
        else:
            break
    
    if prior_experience == "y" and future_outlook == "y":
        rating_good = True

    return rating_good

def webpush(bool):
    if bool:
        print("You should ask emilyOS to go out for dinner or something pf that nature!🥺")
        time.sleep(1)
        print("loading ...")
        time.sleep(2)
        try:
            webbrowser.open("https://web.whatsapp.com/", 0, True)
        except:
            print("Something went wrong")
    else:
        print("your experience with emilyOS seems to be disappointing 😔. Please accept our sincerest apologies \n")
        print("you might want to raise a bug with emilyOS")
        bug_tracking.main()

def main():
    webpush(experience_rating())

if __name__ == "__main__":
    main()