import re
str="abc1def"
if re.match(r"\d",str):
    print("ok")
else:
    print("no")