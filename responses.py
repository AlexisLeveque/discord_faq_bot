responses = {
    'help': """Pour avoir L'aide dans votre langue tapez "help fr"
To see the help in your language type "help en" """,

'help fr' : """
Bienvenue dand l'aide DOFUCKS.
Pour avoir la liste des questions tapez "questions fr"
Pour avoir la reponse à une question, tapez [le numero de la question] [votre langue] exemple : "1 fr" """,

'help en' : """To see the list of question type "questions en"
To see the answer of a question type [question number] [your language] example: "1 en" """,

'questions fr' : """1. Je peux me connecter mais j’ai un écran noir, que faire ?
2. Comment lancer le bot récolte ou xp ?
3. Comment charger un trajet ?
4. Comment fonctionne le Harvester ?
5. Comment fonctionne le XPer ?
6. Comment faire suivre mes personnages ?
7. Le système d’anti-captcha ne fonctionne pas.
8. Le bot passe des fois son tour sans utiliser toutes les compétences possibles.
9. Comment fonctionnent les « PRIORITIES OPTIONS » dans le Fighter ?
10. Comment fonctionnent les « TIMERS OPTIONS » dans le Fighter ?
11. A quoi sert le Seller ?""",

'questions en' : """1. I can connect but I have a black screen, what should I do?
2. How to launch the harvest or xp bot?
3. How do I load a path?
4. How does Harvester work?
5. How does the XPer work?
6. How do I follow my characters?
7. The anti-captcha system does not work.
8. The bot sometimes passes its turn without using all possible skills.
9. How does "PRIORITIES OPTIONS" work in Fighter?
10. How does "TIMERS OPTIONS" work in Fighter?
11. What's the Seller for?""",

'1 fr' : """Sur windows, allez dans le dossier « %AppData%\Dofucks ». Sur Mac, allez dans « /Users/votreNom/Library/Application Support/Dofucks »
Puis supprimer le dossier Cache.
Redémarrez le client Dofucks.""",

'2 fr' : """Vous devez sélectionner un PATH, un chemin. Pour cela, répertoriez vous à « Comment charger un trajet ».
Une fois votre path sélectionné, vous aurez simplement à cocher dans la rubrique « Farmer » soit le Harvester, qui vous permettra de récolter dans le trajet sélectionné, soit le XPer, qui vous permettra d’attaquer les monstres. Pour en savoir plus sur le Harvester ou le XPer, lisez l’aide associée à ces modules.""",

'3 fr' : """Grâce au bouton « LOAD PATHS » dans la rubrique PATH du bot, vous pouvez charger un fichier au format json qui contiendra les paths (chemins).

Si vous n’avez pas de fichier de paths sous la main, vous pouvez vous rendre sur cette adresse http://dofucks.com/paths.json : téléchargez ce fichier (ne copiez-collez pas) en faisant un clic droit > enregistrer sous.
Vous pourrez alors charger ce fichier dans Dofucks.""",

'4 fr' : """Il va récolter tout ce qui se trouve sur son chemin, sauf l’eau. Vous pouvez configurer quelles ressources vous souhaitez récolter en cliquant sur « HARVESTER OPTIONS » et en cochant/décochant les ressources que vous voulez.""",

'5 fr' : """Il va attaquer les monstres qui se situent entre le level min et le level max et qui respectent vos conditions.
Le lvl min/max est le lvl du groupe entier. Les conditions sont inclusives. Si aucune condition n’est donnée, il peut attaquer n’importe quoi.
Si vous souhaitez exclure/inclure un monstre spécifique, rentrer son nom, cliquez dessus et laissez vous guider.
Par exemple, si vous ne voulez pas de piou rouge, il faudra sélectionner ‘Equals to’ 0
Par exemple, si vous voulez au moins 1 pou rouge, il faudra sélectionner ‘Superior than’ 0 .
Attention à respecter le ‘superior’ et ‘inferior’. « Supérieur à 1 » veut dire « 2 ou plus ». « Inférieur à 1 » est pareil que « égal 0 ».
Si vous mettez plusieurs conditions, elles devront toutes être respectées pour aller attaquer un groupe de monstre.""",

'6 fr' : """Sur tous vos personnages qui devront suivre le leader, veuillez d’abord cocher « Follow party member » qui va activer le fait de pouvoir suivre quelqu’un automatiquement.
Ensuite, groupez vos personnages et cliquez sur le leader et faites « suivre ». A ce moment, votre personnage va se mettre à vouloir rejoindre le leader. S’il est trop éloigné ou qu’il y a des murs pour aller vers lui, il se peut que le follower soit bloqué. Il est donc conseillé d’être sur la même map ou sur une map adjacente avant de cliquer sur « Suivre ». Si jamais vous êtes bloqué, arrêtez de suivre le leader. Ne tentez pas de vous déplacer alors que le follower est activé. Il pourrait se perdre.""",

'7 fr' : """Il vous faut un compte sur anti-captcha.com avec des crédits afin que ceux-ci soient utilisés lorsque le jeu vous demandera d’effectuer une vérification via captcha. (Les crédits ne sont pas gratuits). La clé qui vous permet de résoudre les captchas automatiquement se trouve dans « Settings » / « API Setup »
Lorsqu’un captcha apparaîtra, vous n’aurez rien à faire, attendez simplement, la fenêtre se fermera automatiquement, ou s’il y a un problème, un message d’erreur s’affichera au dessus de votre clé anti-captcha, dans Dofucks""",

'8 fr' : """Il y a plusieurs causes à ce problème. Vérifiez que vous avez mis les valeurs par défaut dans « PRIORITIES OPTIONS » et « TIMERS OPTIONS ». Pour plus d’infos à leur sujet, consultez l’aide correspondante.
Vérifiez que les sorts que vous avez sélectionné sont soit des sorts de dégâts, de boost, d’invocations ou de soins. Si votre sort fait partie d’un changement d’état (picole, …) ou d’un sort de déplacement (téléportation, attirance, bond du félin…) il ne sera pas lancé.
Si la case « Auto skip turn » est cochée, votre personnage va juste passer son tour.""",

'9 fr' : """Avant tout, il est nécessaire de comprendre le « ratio ». Le ratio est un nombre indicatif pour le bot de se rendre compte à quel point c’est rentable (ou pas) de lancer un sort sur une cellule. Le bot va tester chaque cellule de chaque sort qu’il peut lancer sur chaque case à laquelle votre personnage peut aller. Il fait donc des milliers de tests juste sur 1 tour pour trouver quel est le meilleur ratio, c’est à dire, la meilleure chose à faire.
Explication :
Remove ratio (damage multiplicator) : Quand vous touchez un allié et que vous lui faites des dégâts, imaginons 50, le ratio que vous mettez ici sera le nombre par lequel seront multipliés les dommages (ici, 50). Donc si vous avez un ratio de 5, le calcul sera 5x50 = 250. Le résultat final est divisé par 100 pour en faire un vrai ratio. On peut en conclure sur faire 50 de dégâts à un allié avec un ratio de 5 nous enlèverait 2,5 de ratio.
Add ratio on boost spell : le ratio que vous vous verrez ajouté si vous lancez un sort de boost sur vous ou vos alliés.
Add ratio on summon spell : le ratio que vous verrez ajouté si vous lancez un sort d’invocation
Add ratio when an enemy can be killed: le ratio que vous ajouterez si vous pouvez tuer un ennemi. 
De base, quand vous attaquez un ennemi, votre ratio est égal aux dégâts réels que vous faites divisés par 100. 100 dégâts = 1 ratio (inclue les résistances).
Heal ratio : le calcul du ratio de soin est le suivant : soin / 100 * (1 - vie de la cible / vie max de la cible) * heal ratio.
Si vous soignez 100 points de vie à un allié qui a 100 hp  et 1000hp au total, le calcul sera : 100 / 100 * ( 1 - 100 / 1000) * 3 (le 3 est configurable) le ratio sera donc de 0.9*3 soit 2.7. Si vous faites le même calcul alors que la cible a 90% de sa vie, le ratio sera beaucoup plus faible (0.3)
Si la cible est un ennemi, le ratio sera enlevé au lieu d’être ajouté.""",

'10 fr' : """Il ne faut pas jouer avec eux. Commencez par désactiver les animations des sorts dans les options du jeu. Cela permettra au bot de pouvoir jouer sans problème (lancement d’un sort alors que l’ennemi et déjà mort par exemple)
Ce sont les différents timers que le bot utilise pour jouer. Plus ils sont bas, plus il jouera vite (plus vous serez repéré / plus le bot pourra buguer)""",

'11 fr' : """Il sert à vendre vos items une fois que la limite de pods a été atteinte. Vous pouvez la configurer.
Pour vendre un item dès que vous serez plein, mettez le nom de l’item en question et laissez vous guider. Il vous sera demandé si vous souhaitez le vendre par 100, 10 ou à l’unité. Vous pouvez cocher les 3, il vendra d’abord par 100, puis par 10 puis par 1 au moment voulu.""",








'1 en' : """On windows, go to the "%AppData%\Dofucks" folder. On Mac, go to "/Users/YourName/Library/Application Support/Dofucks".
Then delete the Cache folder.
Restart the Dofucks client.""",

'2 en' : """You must select a PATH. To do this, list yourself under "How do I load a path".
Once your path is selected, you will simply have to check in the "Farmer" section either the Harvester, which will allows you to harvest in the selected path, or the XPer, which will allow you to attack monsters.
To learn more about the Harvester or XPer, read the help associated with these modules.""",

'3 en' : """Using the "LOAD PATHS" button in the PATH section of the bot, you can load a json file that will contain the paths.

If you don't have a paths file at hand, you can go to http://dofucks.com/paths.json : download this file (don't copy and paste) by right clicking > save as.
You can then load this file into Dofucks.""",

'4 en' : """It'll harvest everything in his path except the water. You can configure which resources you want to harvest by clicking on "HARVEST OPTIONS" and checking/unchecking the resources you want.""",

'5 en' : """It will attack monsters between level min and level max that meet your requirements.
The lvl min/max is the lvl of the whole group. The conditions are inclusive. If no conditions are given, he can attack anything.
If you want to exclude/include a specific monster, enter its name, click on it and let yourself be guided.
For example, if you do not want a red piwi, you will have to select "Equals to" 0
For example, if you want at least 1 red piwi, you will have to select 'Superior than' 0.
Be careful to respect the 'superior' and 'inferior'. "Greater than 1" means "2 or more". "Less than 1" is the same as "equal 0".
If you put several conditions, they must all be respected to attack a group of monster.""",

'6 en' : """On all your characters who will have to follow the leader, please first check "Follow party member" which will enable you to follow someone automatically.
Then group your characters and click on the leader and " follow ". At this point, your character will start wanting to join the leader. If it is too far away or if there are walls to go towards it, it may be that the follower is blocked. It is therefore recommended to be on the same map or on an adjacent map before clicking on "Follow". If you ever get stuck, stop following the leader. Do not attempt to move while the follower is activated. He could get lost.""",

'7 en' : """You need an account on anti-captcha.com with credits so that these are used when the game asks you to perform a check via captcha. (Credits are not free). The key that allows you to resolve captchas automatically is in "Settings" /"API Setup".
When a captcha appears, you will have nothing to do, just wait, the window will close automatically, or if there is a problem, an error message will be displayed above your anti-captcha key, in Dofucks""",

'8 en' : """There are several causes for this problem. Check that you have set the default values in "PRIORITIES OPTIONS" and "TIMERS OPTIONS". For more information about them, see the corresponding help.
Verify that the spells you have selected are either damage, boost, summon or healing spells. If your spell is part of a change of state (booze,...) or a movement spell (teleportation, attraction, feline leap...) it will not be casted.
If the "Auto skip turn" box is checked, your character will just pass his turn.""",

'9 en' : """First of all, it is necessary to understand the "ratio". The ratio is an indicative number for the bot to realize how profitable (or not) it is to cast a spell on a cell. The bot will test every cell of every spell it can cast on every square your character can go to. So he does thousands of tests just on 1 turn to find the best ratio, that is, the best thing to do.
Explanation :
Remove ratio (damage multiplicator) : When you hit an ally and damage him, imagine 50, the ratio you put here will be the number by which the damage will be multiplied (here, 50). So if you have a ratio of 5, the calculation will be 5x50 = 250. The final result is divided by 100 to make a real ratio. We can conclude on doing 50 damage to an ally with a ratio of 5 would remove us 2.5 ratio.
Add ratio on boost spell: the ratio you will see yourself added if you cast a boost spell on yourself or your allies.
Add ratio on summon spell: the ratio you will see added if you cast an invocation spell
Add ratio when an enemy can be killed: the ratio you will add if you can kill an enemy. 
Basically, when you attack an enemy, your ratio is equal to the actual damage you do divided by 100. 100 damage = 1 ratio (includes resistances).
Heal ratio: the calculation of the heal ratio is as follows: heal / 100 * (1 - target life / max target life) * heal ratio.
If you heal 100 life points to an ally who has 100 hp and 1000hp in total, the calculation will be : 100/100 * ( 1 - 100 / 1000) * 3 (the 3 is configurable) so the ratio will be 0.9*3 or 2.7. If you do the same calculation when the target has 90% of its life, the ratio will be much lower (0.3)
If the target is an enemy, the ratio will be removed instead of added.""",

'10 en' : """You shouldn't play with them. Start by disabling spell animations in the game options. This will allow the bot to play without problem (casting a spell while the enemy is already dead for example)
These are the different timers that the bot uses to play. The lower they are, the faster it will play (the more you will be spotted / the more the bot will bug)""",

'11 en' : """It is used to sell your items once the pod limit has been reached. You can configure it.
To sell an item as soon as you are full, put the name of the item in question and let yourself be guided. You will be asked if you want to sell it by the 100, 10 or unit. You can check all 3, it will sell first by 100, then by 10 then by 1 at the desired time.""",
}