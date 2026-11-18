# CloudNotes kit v2 - TP DevSecOps (9 etapes)

Contenu : app.py (vulnerable), Dockerfile (naif), tf/ et k8s/ (infra fautive),
monitor/ (attaque + alerte), ci/security.yml, solutions/ (versions corrigees).

TP 0 : docker network create devsecops ; docker build -t cloudnotes:naive . ; voir le deck.
TP 2 : corriger app.py en vous inspirant de solutions/app_fixed.py.
TP 3 : docker build -f solutions/Dockerfile.durci -t cloudnotes:secure .
TP 6 : checkov -d tf ; comparer avec solutions/main.fixed.tf et deployment.fixed.yaml.
TP 8 : bash monitor/attack.sh puis bash monitor/alert.sh (necessite l'image secure).

Note : kit non execute de bout en bout. Les options cosign
(--allow-insecure-registry, --tlog-upload=false) et les noms de checks Checkov
peuvent varier selon les versions.
