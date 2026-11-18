import logging
import re
import sqlite3
from flask import Flask, jsonify

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
db = sqlite3.connect(":memory:", check_same_thread=False)
db.row_factory = sqlite3.Row
db.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY, owner TEXT, body TEXT)")
db.executemany("INSERT INTO notes VALUES (?,?,?)",
               [(1, "alice", "note publique"), (2, "bob", "note privee de bob")])

@app.after_request
def headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["Content-Security-Policy"] = "default-src 'none'"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Cache-Control"] = "no-store"
    return resp

@app.route("/notes/<nid>")
def get_note(nid):
    if not re.fullmatch(r"\d+", nid):
        logging.warning("requete suspecte id=%s", nid)
        return jsonify(error="id invalide"), 400
    rows = db.execute("SELECT * FROM notes WHERE id = ?", (nid,)).fetchall()
    return jsonify([dict(r) for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
