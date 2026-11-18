#!/bin/bash
# Envoie 9 requetes suspectes vers l'API
for p in "1%20OR%201=1" "1;DROP%20TABLE%20notes" "abc" "1'--" "../etc/passwd" "1%20UNION%20SELECT%201" "%27%20OR%20%271" "99999999999x" "<script>"; do
  curl -s -o /dev/null "localhost:5000/notes/$p"
done
echo "9 requetes envoyees"
