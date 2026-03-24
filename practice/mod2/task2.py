import re

email_pattern = re.compile(r"[\d\w+_\-#]+@[\d\w]+\.\w{2,3}")

if __name__ == "__main__":
    print("Введите текст в котором есть email-ы:")
    TEXT = input()
    emails = email_pattern.findall(TEXT)
    print(*emails, sep="\n")

