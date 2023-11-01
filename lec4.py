#Text, Unicode, and Bytes
in_french = 'Montréal'
type(in_french)

s = 'Montreal'
as_bytes = s.encode('utf8')
type(as_bytes)