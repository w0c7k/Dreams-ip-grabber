import webbrowser
import time
import sys

INVITE_LINK = "https://grabify.link/RA7SEJ"

def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_banner():
    print("=" * 50)
    slow_print("🚀 Welcome to My Discord Server Inviter 🚀")
    print("=" * 50)

def show_menu():
    print("\nChoose an option:")
    print("1) Open Discord invite in browser")
    print("2) Exit")

def open_invite():
    slow_print("Opening invite link...")
    webbrowser.open(INVITE_LINK)

def main():
    show_banner()

    while True:
        show_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            open_invite()
        elif choice == "2":
            slow_print("Goodbye 👋")
            break
        else:
            slow_print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
