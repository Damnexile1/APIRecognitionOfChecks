import json

from NalogRuPython import NalogRuPython

client = NalogRuPython()
# qr_code = "t=20211115T2140&s=179.90&fn=9285440300373666&i=29355&fp=3129069236&n=1"
# qr_code = "t="
qr_code = "t=20210206T1741&s=1037.60&fn=9282440300658937&i=5880&fp=37375757&n=1"
ticket = client.get_ticket(qr_code)
print(json.dumps(ticket, indent=4, ensure_ascii=False))
