#!/usr/bin/python3
print('{}'.format(''.join(chr(char) for char in range(ord('a'), ord('z') + 1)
                          if chr(char) not in ['e', 'q'])), end="")
