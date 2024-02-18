**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**
**Description**:What is that?
**Type:** Crypto
**Level:** Beginner
**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

En téléchargant le fichier `encrypt.enc`, nous obtenons la suite de caractère suivante:
`%2E%2E%2E%2E%2E%20%2D%2E%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2D%2D%2E%2E%2E%20%2D%2D%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2D%2D%2E%2E%2E%20%2D%2D%2D%2E%2E%20%2E%2E%2E%2E%2D%20%2E%20%2E%2E%2E%2D%2D%20%2E%2D%2D%2D%2D%20%2D%2D%2E%2E%2E%20%2D%2D%2D%2D%2D%20%2E%2E%2E%2E%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2E%2D%20%2E%2E%2E%2E%2E%20%2D%2D%2D%2E%2E%20%2D%2D%2E%2E%2E%20%2D%2D%2D%2D%2D%20%2D%2E%2E%2E%2E%20%2E%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2D%2D%2D%20%2E%2E%2E%2E%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2D%2D%2E%2E%2E%20%2E%2E%2E%2E%2D%20%2E%2E%2E%2E%2D%20%2E%2E%2E%2E%2D%20%2E%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2D%2E%2E%2E%2E%20%2E%2E%2D%2D%2D%20%2E%2E%2E%2D%2D%20%2D%2D%2D%2D%2D%20%2E%2E%2E%2D%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2E%2D%20%2D%2D%2D%2E%2E%20%2E%2E%2E%2E%2D%20%2E%20%2E%2E%2E%2E%2E%20%2D%2D%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2E%2D%20%2E%2E%2E%2E%2D%20%2E%20%2E%2E%2E%2E%2D%20%2D%2E%2E%20%2E%2E%2E%2D%2D%20%2E%2D%2D%2D%2D%20%2D%2E%2E%2E%2E%20%2D%2E%2D%2E%20%2E%2E%2E%2D%2D%20%2D%2E%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2D%2D%2D%2D%2E%20%2E%2E%2E%2D%2D%20%2E%2E%2D%2D%2D%20%2D%2D%2E%2E%2E%20%2D%2D%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2E%2E%2E%2E%2E%20%2D%2E%2E%2E%2E%20%2E%2D%2D%2D%2D%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2D%2D%2D%2D%2D%20%2D%2D%2E%2E%2E%20%2D%2D%2D%2D%2E%20%2E%2E%2E%2E%2E%20%2D%2D%2E%2E%2E%20%2E%2E%2E%2E%2E%20%2D%2D%2D%2E%2E%20%2D%2E%2E%2E%2E%20%2E%2E%2E%2E%2D%20%2D%2E%2E%2E%2E%20%2E%2D%20%2D%2E%2E%2E%2E%20%2E%2D%2D%2D%2D%20%2D%2E%2E%2E%2E%20%2D%2E%2E%2E%20%2E%2E%2E%2D%2D%20%2E%2E%2E%2E%2D%20%2E%2E%2E%2D%2D%20%2E%2E%2E%2E%2E`

Avec l'aide d'un simple outil (https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')Magic(3,false,false,''))nous permettant de détecter la technique d'encodage utilisé,nous pouvons obtenir les résultats suivants:

![[Capture d’écran (102).png]]

Nouvelle chaine de caractère:
`VWsxN1pETXpjRE55WDNSb05HNWZNM1l6Y2w5aU0yWXdjak45`

![[Capture d’écran (103).png]]``
Nouvelle chaine de caractère:
`Uk17ZDMzcDNyX3RoNG5fM3Yzcl9iM2YwcjN9`

![[Capture d’écran (104).png]]

Puis nous en arrivons au flag !
Ainsi,le flag est: **RM{d33p3r_th4n_3v3r_b3f0r3}**