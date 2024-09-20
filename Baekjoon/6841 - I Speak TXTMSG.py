#B4_6841_I Speak TXTMSG

trans = {
    "CU": "see you",
    ":-)": "I’m happy",
    ":-(": "I’m unhappy",
    ";-)": "wink",
    ":-P": "stick out my tongue",
    "(~.~)": "sleepy",
    "TA": "totally awesome",
    "CCC": "Canadian Computing Competition",
    "CUZ": "because",
    "TY": "thank-you",
    "YW": "you’re welcome",
    "TTYL": "talk to you later"
}

while True:
    a = input()
    if a == "TTYL":
        print(trans[a])
        break
    if a in trans:
        print(trans[a])
    else:
        print(a)
