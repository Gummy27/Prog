from signature_message import SignatureMessage
from message import Message


msg1 = Message("John Hurt", "Susan Field")

msg1.append("The first line of the message")

msg1.append("the second line.")

msg2 = Message("Margaret Hamilton", "Joe Peters")  

msg2.append("First line")

msg2.append("Second line")

msg2.append("Third line")

actual = msg1 > msg2

expected = True

print(f"\nExpected:\n{expected}\nActual:\n{actual}")
assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"

actual = msg2 > msg1

expected = False

assert actual == expected, f"\nExpected:\n{expected}\nActual:\n{actual}"