print([(r:=__import__('random')).getrandbits(32),f"VIDAR{{{__import__('hashlib').md5(str(r.getstate()[1][0]).encode()).hexdigest()}}}"][0])
