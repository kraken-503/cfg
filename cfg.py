import secrets
import string
import time

print("")
time.sleep(0.7)
with open("art.txt", "r") as art:
    banner = art.read()
print(banner)
chars = string.ascii_letters + string.punctuation + string.digits
time.sleep(0.5)
length = int(input("Needed length for the flag : "))
nos = int(input("Number of flags : "))
text = input(
    """Prefix text to be included before the flag 
        (default: flag{...} ) : """
)


# generates random values for the flag
def flag_gen():
    flag = "".join(secrets.choice(chars) for _ in range(length))
    return flag


# concats generated flag value with the prefix
def out():
    print(
        """

    """
    )
    if text.isalpha():
        for i in range(nos):
            print(f"{text}" + "{" + flag_gen() + "}")
    else:
        print("You didn't enter a prefix value, falling back to defaults...")
        print("")
        for i in range(nos):
            print("flag{" + flag_gen() + "}")


time.sleep(0.5)
out()
