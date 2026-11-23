import re, random
from colorama import Fore, init
init(autoreset=True)
destinations = {
"beaches": ["Bali", "Maldives", "Phuket"],
"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
"cities": ["Tokyo", "Paris", "New York"],
"chicken": ["Chicken island", "Chickentropolis", "Chickenville"]
}
jokes = [
"Why don't programmers like nature? Too many bugs!",
"Why did the computer go to the doctor? Because it had a virus!",
"Why do travelers always feel warm? Because of all their hot spots!"
"Why did the chicken cross the road? to get to the other side 🐔",
]
def normalize_input(text):
  return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
  print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
  preference = input(Fore.YELLOW + "You: ")
  preference = normalize_input(preference)
  if preference in destinations:
    sug=random.choice(destinations[preference])
    print(Fore.GREEN + "How about",sug)
    print(Fore.CYAN + "do you like:",sug,"Y/N")
    answer=input()
    if answer=="Y":
      print(Fore.GREEN + "Awesome hope you enjoy",sug)
    elif answer=="N":
      print(Fore.RED + "Okay lets try another")
      recommend()
    else:
      print(Fore.GREEN + "Please select Y/N")
      recommend()
  else:
    print("Sorry that destination is unavailable")
    recommend()
def joke():
  print(Fore.GREEN + random.choice(jokes))
def showhelp():
  print(Fore.BLUE + "I can:")
  print(Fore.GREEN + "Recommend a destination(recommend)")
  print(Fore.GREEN + "Tell a joke(joke)")
  print(Fore.GREEN + "Offer packing tips(pack)")
  print(Fore.GREEN + "Exit the algorithm(recommend)")
def chat():
  print(Fore.BLUE + "Hello I am a travel bot")
  name=input(Fore.CYAN + "Enter your name to continue")
  print("Welcome",name)
  showhelp()
  while True:
    user_input = input(Fore.YELLOW + f"{name}: ")
    user_input = normalize_input(user_input)
    if "recommend" in user_input or "suggest" in user_input:
        recommend()
    elif "pack" in user_input or "packing" in user_input:
        pack()
    elif "joke" in user_input or "funny" in user_input:
        joke()
    elif "help" in user_input:
        showhelp()
    elif "chicken" in user_input:
        chicken()
    elif "exit" in user_input or "bye" in user_input:
        print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
        break
    else:
        print(Fore.RED + "TravelBot: Could you rephrase?")
def pack():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")
    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")
def chicken():
  print(Fore.YELLOW + "Congratulations you hav efound the chicken easter egg🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓🐔🐥🥚🐣🐔🐓")
chat()
    