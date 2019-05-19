import re

text0 = """
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""

#text = re.sub("<[^<]+>", "", text0)

text = re.search(r"<from>([^<]+)</from>", text0).group(1)


#<div3 type="article" n="4" org="uniform" sample="complete">    </div3>

#re.search(r"<div3 type="article".>([^<]+)</div3>", data).group(1)

print(text)

#print(text)



