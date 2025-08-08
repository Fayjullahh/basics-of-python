#strng literals

a = 'Hello'
b = "World"
c = """
    Hello
    world
"""
import sys
import io

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

unicode_emoji = u"\U0001F600\u2764"  # 😀❤ 
print(unicode_emoji)