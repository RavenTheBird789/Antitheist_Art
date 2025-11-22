# Antitheist Art

def red(text: str) -> str: 
    # Wrap text in ANSI codes for red color
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str: 
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def main():
    # Pentacle Symbol
    pentacle = " ⛧⃝ "

    # Construct the art piece
    art = [
        "    |    ",
        "    |    ",
        "    |    ",
        " ---|---",
        "    |    ",
    ]

    # Quote to display
    quote = "Religion is the antithesis of egalitarianism and enlightenment. Embrace secularism, rationality and reason."
    author = "- RavenTheBird"

    # Print the artwork in red, then quote in bold
    print()
    for line in art:
        print(red(line))
    print()
    print(bold(red(pentacle + " " + quote)))
    print(red(author))
    print()

if __name__ == "__main__":
    main();