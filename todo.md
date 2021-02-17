# YAMS

## TO-DO

Priorité : transformer YAMS en un module python3, l'uploader sur Pypi

1. Système de nom d'utilisateurs : base de donnée plain text (ntp ?) avec nom
d'utilisateur + ip courante (server).
2. Client : annonce son nom d'utilisateur.
3. fichier de configuration qui dit quel module utiliser pour telle tâche.
e.g. module encryption: None, ou bien PGP_encrypt

fonctionnement:

# client

Liens symbolique pour module par défaut ???

envoi msg:

message -> module de chiffrement(1) -> module de mise en forme du msg(2) -> module d'envoi HOST:PORT

réception msg:

msg reçu -> module de décryptage (-> module base de donnée pour mot de passe) -> module de sauvegarde

Note: le msg peut être enregistré crypté, dans ce cas pas d'appel du module de décryptage

Donc pour le lire on fait appel éventuellement au module de décryptage.

# Serveur

Forwarde bêtement le corps du message au destinataire.

```
Classe XXXX
	> handler : stocke le msg dans `self.data` et c'est tout
	cela permet de modifier facilement la manière de communiquer du serveur.

classe TCPHandler(XXXX):
	handler: utilise le handler de XXXX MAIS ajoute des moyens pour traiter les données
	et les forwarder à l'IP désirée.

	(éventuel)
	@staticmethod
	func forward(IP)
```

# Client et serveur

TRÈS probablement une classe paquet en commun


Plus tard :
- authentification mot de passe non encrypté plain text
- cram md5
- on donne un texte aléatoire. Le client le crypte avec sa clef et
le renvoie.

Utiliser les modules `socket` et `socketserver`

maybe yams should be itself a python module

---

(1) ssi msg n'est pas cmd

(2) on ajoute nom utilisateur, et d'autres infos essentielles (dest)
