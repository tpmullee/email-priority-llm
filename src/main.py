# Placeholder: scores emails deterministically (no API keys required)
import pandas as pd, re, sys
VIP = {"ceo@company.com","board@fund.com"}
DEADLINE_RE = re.compile(r"\b(due|deadline|eod|by\s+\d{1,2}(:\d{2})?\s*(am|pm)?)\b", re.I)
df = pd.DataFrame([
  {"sender":"ceo@company.com","subject":"Pricing by EOD","body":"Please send final numbers."},
  {"sender":"ally@team.com","subject":"Lunch","body":"today?"}
])
def score(row):
  s=0
  if row.sender in VIP: s+=30
  if DEADLINE_RE.search(row.subject+" "+row.body): s+=20
  if "invite" in row.subject.lower(): s+=10
  return s
df["priority"]=df.apply(score, axis=1)
print(df.sort_values("priority", ascending=False)[["sender","subject","priority"]])
