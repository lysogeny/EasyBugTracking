def bug_tracking():
    print("Welcome to EmilyOS digital bug tracking")
    bug_title = input("Give your bug a title: \n")
    bug_description = input("Please describe your issue: \n")
    print(f"Sorry we cannot help you with {bug_title}, please consult the physical bug tracking.")
    


if __name__ == "__main__":
    bug_tracking()