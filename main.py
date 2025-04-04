import time
import sys
import os
from getpass import getpass
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Cross-platform beep sound
def beep():
    try:
        import winsound
        winsound.Beep(1000, 200)
    except ImportError:
        sys.stdout.write('\a')
        sys.stdout.flush()

# ASCII Art
ascii_art = r"""
  ,-~~-.___.
 / |  '     \         Electronic components detection using ar 
(  )         0              
 \_/-, ,----'            
    ====           //                     
   /  \-'~;    /~~~(O)
  /  __/~|   /       |     
=(  _____| (_________|   W<
"""

# Show ASCII Art
print(Fore.CYAN + ascii_art)

# Welcome Message
print(Fore.YELLOW + "\n🔧 Welcome to the AR Electronic Components Detector!\n")

# Spinner Animation
print(Fore.BLUE + "⏳ Initializing system, please wait...", end=" ", flush=True)
spinner = ['|', '/', '-', '\\']
for _ in range(20):
    for symbol in spinner:
        sys.stdout.write(Fore.MAGENTA + symbol)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
print("\n")

# Passcode settings
correct_passcode = "1234"
max_attempts = 3
granted = False

# Retry loop
for attempt in range(1, max_attempts + 1):
    print(Fore.LIGHTYELLOW_EX + f"Attempt {attempt}/{max_attempts}")
    entered_passcode = getpass("🔐 Enter 4-digit passcode (input hidden): ")

    if entered_passcode == correct_passcode:
        beep()
        print(Fore.GREEN + "\n✅ Access Granted! Welcome, Admin.")
        print(Fore.CYAN + "🔗 Project Link: https://hub.ultralytics.com/projects/KhQLcOGmbDeYFSbPNQig\n")
        granted = True
        break
    else:
        beep()
        print(Fore.RED + "❌ Incorrect passcode.")
        if attempt < max_attempts:
            print(Fore.YELLOW + "🔁 Please try again.\n")
        else:
            print(Fore.RED + "\n🚫 Maximum attempts reached. Access Denied.\n")

# Hold terminal open for 300 seconds (5 minutes)
print(Fore.LIGHTBLUE_EX + "⌛ Terminal will remain open for 5 minutes...")
time.sleep(300)
