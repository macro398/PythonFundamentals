state_capitals = {"Washington":"Olympia", "Oregon":"Salem","Califronia":"Sacramento"}

#print(len(state_capitals))
#print(state_capitals["Washington"])
state_capitals["Washington"] = "Aberdeen"
state_capitals["Texas"] = "Austin"
print(state_capitals)
del state_capitals["Califronia"]
print(state_capitals)
removed_capital = state_capitals.pop("Oregon")
print(state_capitals)
print(removed_capital)