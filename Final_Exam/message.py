class Message:
    def __init__(self, sender: str, receiver: str) -> None:
        """
            The constructor takes in a sender and receiver.
        """
        self.sender = sender
        self.receiver = receiver
        self.message = ""

    def append(self, line: str) -> None:
        """
            This function appends a line to the message and adds a
            newline break.
        """
        self.message += f"{line}\n"
    
    def __str__(self) -> str:
        """
            This function will return the sender, receiver and message
            in a string.
        """
        return_string = f"From: {self.sender}\n"
        return_string += f"To: {self.receiver}\n"
        return_string += self.message

        return return_string
    
    def __len__(self) -> int:
        """
            This function overloads the len function so it will display
            the length of the message.
        """
        stripped_message = self.message.strip().replace("\n", "")

        return len(stripped_message)

    def __gt__(self, other: object) -> None:
        """
            This function overloads the > operation so it will compare 
            the length of messages.
        """
        return len(self) > len(other)

        