import re

text0 = """
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""
text = re.search(r"<from>([^<]+)</from>", text0).group(1)

print(text)


