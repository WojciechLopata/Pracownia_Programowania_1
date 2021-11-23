import re
message="To be, or not to be, that is the question"
vovels=re.findall("[aouiye]",message)
number=len(vovels)
print(number)