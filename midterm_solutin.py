sports = [
    {"num": 1, "name": "Basketball", "category": "Team"},
    {"num": 2, "name": "Volleyball", "category": "Team"},
    {"num": 3, "name": "Badminton", "category": "Individual"},
    {"num": 4, "name": "Chess", "category": "Individual"},
    {"num": 5, "name": "Table Tennis", "category": "Individual"}
]

print("====== INTRAMURALS GAME RESULTS ======")
games = []
points = 0

section = input("Enter class section name: ")
coordinator = input("Enter sports coordinator's name: ")

print(" === AVAILABLE SPORTS ===")
for sport in sports:
    print(f"{sport['num']}. {sport['name']} ({sport['category']})")

print(" === ENTER GAME RESULTS ===")
for i in range(4):
    sport_input = input(f"\nGame {i+1} - Enter sport number (1-5) or 0 to skip: ")
    
    if sport_input == "":
        print("Error! Enter a valid number.")
        continue
    elif sport_input == "0":
        continue
    elif sport_input == "1" or sport_input == "2" or sport_input == "3" or sport_input == "4" or sport_input == "5":
        sport_num = int(sport_input)
        sport = sports[sport_num - 1]
        opponent = input("Enter opposing section: ")
        result = input("Enter result (W/L): ").upper()
        
        game_points = 3 if result == "W" else 0
        points += game_points
             
        games.append({
            "num": len(games) + 1,
            "sport": sport["name"],
            "category": sport["category"],
            "opponent": opponent,
            "result": result,
            "points": game_points
        })
    else:
        print("Invalid! Enter 1-5 or 0 to skip.")

if points >= 9:
    standing = "GOLD CONTENDER"
elif points >= 6:
    standing = "SILVER PUSH"
else:
    standing = "KEEP FIGHTING!"

print("====== ====== ====== ====== ====== ======")
print(f"SECTION: {section.upper()} | COORDINATOR: {coordinator}")
print("====== ====== ====== ====== ====== ======")

for game in games:
    print(f"Game {game['num']}: {game['sport']} ({game['category']}) vs {game['opponent']} - {game['result']} ({game['points']}pts)")

print("====== ====== ====== ====== ====== ======")
print(f"TOTAL POINTS: {points} | STANDING: {standing}")
print("====== ====== ====== ====== ====== ======")
