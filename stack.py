import re


class Stack:
    """Implementation of stack using python list"""
    def __init__(self):
        """Initialize items as empty list"""
        self.items = []

    def is_empty(self):
        """If stack return True, False otherwise"""
        return self.items == []

    def push(self, item):
        """Take item and append it to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove item from the top of the stack return it."""
        return self.items.pop()

    def peek(self):
        """Return top item of the stack"""
        return self.items[len(self.items) - 1]

    def size(self):
        """Return the size of the stack"""
        return len(self.items)

    def __str__(self):
        """Return string to print when print() method is evaluated"""
        string = ""
        for i in self.items:
            string += str(i) + ", "
        return string


self_closing_tags = ['<area>', '<base>', '<br>', '<col>', '<embed>', '<hr>', '<img>', '<input>', '<link>', '<meta>',
                     '<param>', '<source>', '<track>', '<wbr>']


def tags_checker(file):
    """Take file to check if tags are correct. Isolate the tags from the file (without the optional settings).
    While there are still tags to check:
    Push every tag that is not a closing or a self-closing tag to a stack. If the tag is a closing tag remove backslash
    and pop first tag from the stack. Compare them and they are not equal return False and two unbalanced tags.
    If html tags are correct and stack is empty return True, False otherwise """
    with open(file, 'r') as f:
        data = f.read()
        tags = re.findall('<[^>]+>', data)  # < everything apart from > >
        tags = [re.sub(r'(<\w+)\s[^>]+(>)', r'\1\2', i) for i in tags]

    s = Stack()
    index = 0
    if_html = [tags[0], tags[-1]]
    print(tags)
    while index < len(tags):
        symbol = tags[index]
        if not ("!" in symbol) and not("/" in symbol) and symbol not in self_closing_tags:
            s.push(symbol)
        elif "/" in symbol and symbol not in self_closing_tags and symbol != "</html>":
            tag = symbol.replace("/", "")
            top = s.pop()
            if tag != top:
                return False, tag, top
        index = index + 1

    if s.is_empty() and if_html == ["<!DOCTYPE html>", "</html>"]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(tags_checker("tags_file.txt"))
