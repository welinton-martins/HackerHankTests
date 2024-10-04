def print_full_name(first: str, last: str) -> None:
    # Create the greeting message
    message = f"Hello {first} {last}! You just delved into python."
    # Print the message
    print(message)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)