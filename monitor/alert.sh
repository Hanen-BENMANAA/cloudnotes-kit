#!/bin/bash
# Alerte si plus de 5 lignes "suspecte" dans les logs du conteneur "app"
N=$(docker logs app 2>&1 | grep -c "suspecte")
if [ "$N" -gt 5 ]; then
  echo "ALERTE : $N requetes suspectes (> 5)"; exit 1
else
  echo "OK : $N requetes suspectes"
fi
