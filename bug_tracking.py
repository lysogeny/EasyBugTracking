class BugResolutionException(Exception):
    """Exception for bugs not resolvable by this software"""
    def __init__(self, name: str, description: str):
        msg = self.format_message(name, description)
        super().__init__(msg)

    @staticmethod
    def format_message(name, description):
        return f"Sorry we cannot help you with {name}, please consult the physical bug tracking."

def bug_tracking():
    print("Welcome to EmilyOS digital bug tracking")
    bug_title = input("Give your bug a title: \n")
    bug_description = input("Please describe your issue: \n")
    raise BugResolutionException(bug_title, bug_description)
    


if __name__ == "__main__":
    bug_tracking()
