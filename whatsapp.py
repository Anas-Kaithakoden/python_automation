import pywhatkit

phone_number = input("Enter phone number: ")
message = input("Message: ")

# to a number
pywhatkit.sendwhatmsg(phone_number, message, 10, 20) # hour , minute

# to a group
group_link = input("Group_link: ")
pywhatkit.sendwhatmsg_to_group(group_link, message, 10, 20)