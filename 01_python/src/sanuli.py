import sys
import re

_, regex, vaaditut, kielletyt = sys.argv

[print(sana.strip()) for sana in sys.stdin if re.match(f'^{regex}$', sana) and all(
    v in sana for v in vaaditut) and not any(k in sana for k in kielletyt)]
