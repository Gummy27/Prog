class Menu:
    """
        This class will hold together a menu that will be displayed to the user.
    """
    def __init__(self) -> None:
        """
            The constructor doesn't take any parameters but initializes a list 
            that will store all the options.
        """
        self.options = []

    def __str__(self) -> str:
        """
            The string method will print out all of the options in a numbered 
            dropdown menu.
        """
        string_menu = ""
        for index, option in enumerate(self.options):
            string_menu += f"{index+1}. {option}\n"
        return string_menu

    def add(self, new_option: str) -> None:
        """
            This function appends new options to the option list in the class.
        """
        self.options.append(new_option)

    def remove(self, del_option: str) -> None:
        """
            This function will delete a desired option out of the option list.
        """
        try:
            delete_index = self.options.index(del_option)

            self.options = self.options[:delete_index] + self.options[delete_index+1:]
        except ValueError:
            pass

    def insert(self, new_option: str, index: int) -> None:
        """
            This function will insert a option into a specific index in the class
            option list.
        """
        if index >= 1:
            index -= 1
            self.options = self.options[:index] + [new_option] + self.options[index:]

    def position(self, option: str) -> str:
        """
            This function will print out the index of a specific option.
        """
        try:
            return self.options.index(option)+1
        except ValueError:
            return 0