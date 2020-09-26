s = input()
nach = s.find('h')
rev = s[::-1]
kon = len(s) - rev.find('h')
print(s[:nach], s[kon:], sep='')
