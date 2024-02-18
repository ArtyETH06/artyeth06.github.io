
**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**
**Description:** Your friend says he loves to 'encrypt' his passwords. Fearing that you might crack it, he has decided not to tell you the hash function he used! Find his password to punish him for hiding his passwords from you!

Format: RM{the_password}

**Type:** Crypto

**Level:** Easy
**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

En téléchargant le fichier `encrypt.enc`, nous obtenons la chaine de caractère suivante:`621ec23e9e9bc5a442c280eb8ff66e0c6a6d571f69c155bbc53015e1195feaee9c918be1507554c8efff680446f32eebff74d0d907e0fc239da947849b049811`
A l'aide d'outils simple et puissants, comme https://crackstation.net/, nous pouvons cracker le Hash


![[Capture d’écran (106).png]]

Nous obtenons ainsi le password: `p@ssw0rd!`

Ainsi le flag est: **RM{p@ssw0rd!}**

