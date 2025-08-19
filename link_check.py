import sys, requests


TIMEOUT = 10


urls = [
"https://moto555.com",
"https://yes855.org",
"https://daya138.com",
]


ok, bad = [], []
for u in urls:
try:
r = requests.get(u, timeout=TIMEOUT, allow_redirects=True)
(ok if 200 <= r.status_code < 400 else bad).append((u, r.status_code))
except Exception as e:
bad.append((u, str(e)))


print("OK:")
for u, s in ok:
print(f" {u} -> {s}")
print("\nIssues:")
for u, s in bad:
print(f" {u} -> {s}")
