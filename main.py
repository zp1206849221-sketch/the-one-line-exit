import os

ENTRY = "Dear all, I quit as your panda matchmaker — every panda is paired off, and I want someone who looks at me like they look at bamboo."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
