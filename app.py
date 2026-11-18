import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
db = sqlite3.connect(":memory:", check_same_thread=False)
db.row_factory = sqlite3.Row
db.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, owner TEXT, body TEXT)")
db.executemany("INSERT INTO notes VALUES (?,?,?)",
               [(1, "alice", "note publique"), (2, "bob", "note privee de bob")])

@app.route("/notes/<nid>")
def get_note(nid):
    # DEFAUT VOLONTAIRE : injection SQL (concatenation)
    rows = db.execute("SELECT * FROM notes WHERE id = " + nid).fetchall()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    # DEFAUT VOLONTAIRE : debug=True
    app.run(host="0.0.0.0", port=5000, debug=True)
