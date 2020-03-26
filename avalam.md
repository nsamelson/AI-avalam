# Avalam

## Règles

[http://www.oya.fr/?post/2014/12/09/73-avalam-est-a-oya](http://www.oya.fr/?post/2014/12/09/73-avalam-est-a-oya)

## Intelligence Artificielle

Votre IA doit être un serveur web basé sur ceux que l'on trouve dans le répertoire `ai`.

Ce serveur a une route, `move`. Cette route recevra le `body` JSON suivant:

```json
{
	"game": [
		[ [],  [],  [], [0], [1],  [],  [],  [],  []],
		[ [],  [],  [], [1], [0], [1], [0], [1],  []],
		[ [],  [], [1], [0], [1], [0], [1], [0], [1]],
		[ [],  [], [0], [1], [0], [1], [0], [1], [0]],
		[ [], [0], [1], [0],  [], [0], [1], [0],  []],
		[[0], [1], [0], [1], [0], [1], [0],  [],  []],
		[[1], [0], [1], [0], [1], [0], [1],  [],  []],
		[ [], [1], [0], [1], [0], [1],  [],  [],  []],
		[ [],  [],  [],  [], [1], [0],  [],  [],  []]
	],
	"moves": [],
	"players": ["LUR", "LRG"],
	"you": "LUR"
}
```

La clé `game` contient l'état du jeu. Il s'agit d'une liste de liste représentant le plateau de jeu qui comporte 9x9 cases.

Chaque case contient une liste qui représente la pile de pions se trouvant sur la case. Le premier pion de la liste est celui du bas de la pile, le dernier est celui du haut. Les listes vides représentent les cases où il n'y a pas de pion.

Les pions `0` sont les pion du premier joueur, les pions `1` sont les pions du second joueur. La liste des joueurs est fournie à la clé `players`.

La clé "you" vous indique quel joueur vous êtes.

La clé `moves` contient la liste de tout les mouvements joués depuis le début de la partie.

Cette route devra répondre par un JSON comme celui-ci:

```json
{
	"move": {
		"from": [0, 3],
		"to": [1, 4]
	},
	"message": "I'm Smart"
}
```

Où `from` indique la pile de pions que vous voulez déplacer et `to` indique sa destination.

La clé `message` est optionnelle. Les message sont affichés durant la partie.

Si votre `move` ne respecte pas le format, n'est pas autorisé par les règles ou n'est pas renvoyé dans les 10 secondes, il sera considéré comme un `Bad Move`. Si vous faites 3 `Bad Moves` dans une partie vous perdez par abandon.

Le serveur aura aussi une route `ping` qui doit répondre quelque chose. Elle sera utilisée pour tester la connectivité avec [README.md](le superviseur de partie).

## Inscription

Le jour de la compétition, il faudra vous inscrire auprès du [README.md](superviseur de partie).

Le superviseur de partie accepte des connexions TCP sur le port 3001 et attend un JSON du format suivant:

```json
{
	"matricules": ["11111", "22222"],
	"port": 1234,
	"name": "Terminator"
}
```

## Modalités de remise

Le projet est à réaliser seul ou par binôme.

Votre projet doit être remis via **GitHub**. Nous vous conseillons de créer une *repository* séparée de celle-ci. Elle devra contenir au minimum:
- Le script python de votre Server IA
- Un `README.md` expliquant la stratégie et les bibliothèques utilisées (Et les noms des deux étudiants si fait en binôme)

## Grille de notation

- Le serveur démarre correctement: **2**
- Le serveur a une route `move`: **2**
- La route `move` renvoie un `JSON` correspondant aux spécifications: **2**
- L'état du jeu intervient dans la génération du `move`: **2**
- Le code est convenable (noms des variables et fonctions, commentaires, ...): **2**
- Le fichier `README.md` explique la stratégie et les bibliothèques utilisées: **2**
- La stratégie utilisée est avancée/originale: **1**
- Durant le championnat:
	- L'IA est mieux classée que Random: **2**
	- L'IA génère moins de 3 `Bad Move` par partie (en moyenne): **0.5**
	- L'IA génère moins de 2 `Bad Move` par partie (en moyenne): **0.5**
	- L'IA génère moins de 1 `Bad Move` par partie (en moyenne): **0.5**
	- L'IA n'a généré aucun `Bad Move`: **1**
	- Bonus classement (1<sup>er</sup>: **2.5**, 2<sup>e</sup>: **2**, 3<sup>e</sup>: **1.5**, 4<sup>e</sup>: **1**, 5<sup>e</sup>: **0.5**)

**En cas de plagiat entre groupe, tout les étudiants impliqués auront 0**