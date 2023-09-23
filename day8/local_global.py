player_health = 10

def drink_potion():
    potion_strength=2
    print(player_health)
    return

drink_potion()
print(player_health)

#having a global and we can refer them in func using global keywords

print('before the initial update')
def print_var():
    global player_health 
    player_health+=1 #this is one way to do
    print(player_health)

print_var()

def increase_val():
    val = player_health
    return val+5 

print('before the second update')
player_health = increase_val()
print(player_health)