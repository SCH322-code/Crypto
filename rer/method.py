import hashlib
y=207827294#1100011000110011000101011110
y=y^y>>18
y=y^((y<<15)&4022730752)
temp=y^y<<7&2636928640
temp=y^temp<<7&2636928640
y=y^temp<<7&2636928640
temp=y^y>>11
y=y^temp>>11
print(f"VIDAR{{{__import__('hashlib').md5(str(y).encode()).hexdigest()}}}")