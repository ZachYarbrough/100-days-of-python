# Dictionaries

code_dictionary = {
    "Bug": "An error in your code.",
    "Function": "A block of code that you can call an reuse."
}

code_dictionary["Loop"] = "A block of code that allows you to repeat code until a requirement is met."

# For loops only pass the key in a loop

for key in code_dictionary:
    print(key)
    print(code_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = [
    { 
        "country": "France", 
        "cities_visited": ["Paris", "Dijon"],
        "total_visits": 3
    }
]