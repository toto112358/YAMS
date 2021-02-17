# YAMS

## TO-DO

Priorité : transformer YAMS en un module python3, l'uploader sur Pypi

1. Système de nom d'utilisateurs : base de donnée plain text (ntp ?) avec nom
d'utilisateur + ip courante (server).
2. Client : annonce son nom d'utilisateur.

Plus tard :
- authentification mot de passe non encrypté plain text
- cram md5
- on donne un texte aléatoire. Le client le crypte avec sa clef et
le renvoie.

Utiliser les modules `socket` et `socketserver`

maybe yams should be itself a python module
