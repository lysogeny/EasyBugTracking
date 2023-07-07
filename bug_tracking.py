"""EmilyOS Bug tracking system"""

class BugResolutionException(Exception):
    """Exception for bugs not resolvable by this software"""
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        msg = self.format_message(name)
        super().__init__(msg)

    @staticmethod
    def format_message(name: str):
        """Formats the exception with a way to address it"""
        return f"Sorry we cannot help you with {name}, please consult the physical bug tracking."

def receive_bug():
    """Receive a bug from user input"""
    title = input("Give your bug a title: \n")
    description = input("Please describe your issue: \n")
    return title, description

def bug_tracking():
    """Bug tracking main function"""
    print("Welcome to EmilyOS digital bug tracking")
    title, description = receive_bug()
    raise BugResolutionException(title, description)

def main():
    """Run bug tracker and handle errors"""
    try:
        bug_tracking()
    except BugResolutionException as exception:
        print(exception)

if __name__ == "__main__":
    main()
