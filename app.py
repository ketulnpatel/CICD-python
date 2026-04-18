from flask import Flask, render_template, jsonify

app = Flask(__name__)

SQUAD = [
    {"name": "David Raya",       "number": 22, "position": "GK",  "nationality": "🇪🇸", "goals": 0,  "assists": 0},
    {"name": "Ben White",        "number": 4,  "position": "DEF", "nationality": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "goals": 2,  "assists": 3},
    {"name": "William Saliba",   "number": 12, "position": "DEF", "nationality": "🇫🇷", "goals": 2,  "assists": 1},
    {"name": "Gabriel Magalhães","number": 6,  "position": "DEF", "nationality": "🇧🇷", "goals": 5,  "assists": 1},
    {"name": "Oleksandr Zinchenko","number":35,"position": "DEF", "nationality": "🇺🇦", "goals": 0,  "assists": 4},
    {"name": "Thomas Partey",    "number": 5,  "position": "MID", "nationality": "🇬🇭", "goals": 1,  "assists": 2},
    {"name": "Martin Ødegaard",  "number": 8,  "position": "MID", "nationality": "🇳🇴", "goals": 8,  "assists": 10},
    {"name": "Declan Rice",      "number": 41, "position": "MID", "nationality": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "goals": 7,  "assists": 8},
    {"name": "Bukayo Saka",      "number": 7,  "position": "FWD", "nationality": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "goals": 16, "assists": 11},
    {"name": "Kai Havertz",      "number": 29, "position": "FWD", "nationality": "🇩🇪", "goals": 13, "assists": 5},
    {"name": "Leandro Trossard", "number": 19, "position": "FWD", "nationality": "🇧🇪", "goals": 9,  "assists": 6},
    {"name": "Gabriel Martinelli","number": 11,"position": "FWD", "nationality": "🇧🇷", "goals": 10, "assists": 7},
    {"name": "Jorginho",         "number": 20, "position": "MID", "nationality": "🇮🇹", "goals": 0,  "assists": 1},
    {"name": "Raheem Sterling",  "number": 30, "position": "FWD", "nationality": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "goals": 4,  "assists": 3},
]

RESULTS = [
    {"opponent": "Manchester City",  "score": "2-2", "result": "D", "date": "Mar 31, 2025", "venue": "Home"},
    {"opponent": "Chelsea",          "score": "3-1", "result": "W", "date": "Mar 16, 2025", "venue": "Away"},
    {"opponent": "Liverpool",        "score": "1-2", "result": "L", "date": "Mar 1,  2025", "venue": "Home"},
    {"opponent": "Brentford",        "score": "3-0", "result": "W", "date": "Feb 22, 2025", "venue": "Away"},
    {"opponent": "West Ham",         "score": "5-1", "result": "W", "date": "Feb 8,  2025", "venue": "Home"},
]

STATS = {
    "played": 34, "won": 22, "drawn": 6, "lost": 6,
    "goals_for": 74, "goals_against": 35, "points": 72, "position": 2
}

@app.route("/")
def index():
    return render_template("index.html", squad=SQUAD, results=RESULTS, stats=STATS)

@app.route("/squad")
def squad():
    return render_template("squad.html", squad=SQUAD)

@app.route("/results")
def results():
    return render_template("results.html", results=RESULTS)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "club": "Arsenal FC", "deployed_by": "Ketul"})

@app.route("/api/squad")
def api_squad():
    return jsonify(SQUAD)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
