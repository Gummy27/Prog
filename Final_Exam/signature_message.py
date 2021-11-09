from message import Message

class SignatureMessage(Message):
    def __init__(self, sender: str, receiver: str, signature: str) -> None:
        """
            The constructor takes in sender, receiver and a signature.
        """
        super().__init__(sender, receiver)
        self.signature = signature

    def __str__(self) -> str:
        """
            This is the same as the parent except it also prints out
            the signature.
        """
        return_string = super().__str__()
        return_string += f"\n{self.signature}"

        return return_string