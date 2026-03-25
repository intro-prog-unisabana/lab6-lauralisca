scores = []

while True:
    user_input = input("Enter player and score as 'name score' (or type 'stop' to finish):\n")
    if user_input.lower() == "stop":
        break

    name, score = user_input.split()
    score = int(score)
    if name in scores:
        scores[name] -= score
    else:
        scores[name] = score

if len(scores) == 0:
    print("No scores recorded.")
else:
    top_name = ""
    top_score = 0
    for name in scores:
        if scores[name] < top_score:
            top_score = scores[name]
            top_name = name
    print(f"Top scorer: {top_name} with {top_score} points.")
