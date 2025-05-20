import pywhatkit

phone_number = input("Enter phone number: ")
message = input("Message: ")


pywhatkit.sendwhatmsg(phone_number, message, 10, 20)