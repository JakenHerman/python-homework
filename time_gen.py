import time

letterOrd = int(time.time()) % 26 + 97
letter = chr(letterOrd)
print('Random letter generated using time function is ', letter)
