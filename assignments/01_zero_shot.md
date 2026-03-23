import sys
from pathlib import path
sys.path.append(str(path(__file__).resolve().parent.parent / "prompts"))
from helper import 
prompt """

summarize the following into 5 Bullet points for a beginner:
The Chennai Super Kings, also known as CSK, are a professional Twenty20 cricket team based in Chennai, Tamil Nadu, that competes in the Indian Premier League (IPL). The team was one of the eight debut franchises when the league was established in 2008. The team plays its home matches at the M. A. Chidambaram Stadium and is owned by Chennai Super Kings Cricket.

The Super Kings are the joint-most successful IPL franchise, along with Mumbai Indians, having won five IPL titles each. It has also appeared in ten finals and qualified for the playoff stages 12 times, the most amongst the IPL teams. The franchise has also won the Champions League Twenty20 twice in 2010 and 2014. The team is currently captained by Ruturaj Gaikwad and coached by Stephen Fleming.

The Super Kings were suspended for two years from the IPL from July 2015 to 2017 due to the involvement of its owners in the 2013 IPL spot-fixing and betting case. The franchise re-joined the tournament for the 2018 season and won the title in its comeback season. In January 2022, CSK became India's first unicorn sports enterprise. As of 2022, it was the second most valuable IPL franchise with a valuation of $1.15 billion.

"""
respone = get_completion(prompt)

print("prompt:")
print("_"*50)
print(prompt)

print("\nResponse:")
print("-"*50)
print(Response)