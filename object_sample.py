from moderndict import Object

data = Object({"quake": {"mw": "3.7"}})
data2 = Object({"quake": {"ml": "3.9"}})

print("first quake:", data.quake.any(["mw", "ml", "md"], key=True)) # first quake: {mw: 3.7}
print("second quake:", data2.quake.any(["mw", "ml", "md"], key=True)) # second quake: {ml: 3.9}

data.haskey("quake") # has data 'quake' key?
data.only() # bring only values that are not none
data.only(lambda k, v: k[:2] == "is") # bring only values that are start with 'is' substring

info = Object({"info": {"quake": {"magnitude": 3.9}}})

print(info.info.quake.magnitude) # 3.9
