import re

text0 = """
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""

results = re.split("</[^<]+>", text0)

for r in results:
    print(r)

print(results)



