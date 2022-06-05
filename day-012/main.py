# Local and Global variables

enemies = 1

# 'enemies' will return 2
def increase_enemies():
    # This is a local variable so it is different than the outer scope of 'enemies'
    enemies = 2
    print(f"enemies inside function: {enemies}")

def increase_global_enemies():
    global enemies
    enemies += 2
    print(f"enemies outside the function: {enemies}")

increase_enemies()
# 'enemies' will return 1 because 2 was the local scope
print(f"enemies outside the function: {enemies}")
increase_global_enemies()

player_health = 10

def drink_potion(potion_strength):
    print(player_health + potion_strength)

drink_potion(2)

game_level = 3
enemies_array = ["skeletons", "zombies", "aliens"]

# Conditional Statements do not affect scope
if game_level < 5:
    new_enemy = enemies_array[0]
print(new_enemy)

# Global Constants

# Make your constants all upper case
PI = 3.1459

def calc():
    print(PI)
calc()