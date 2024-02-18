
**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**
**Description:** My check is so secure!
**Type:** Web
**Level:** Beginner
**━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━**

En allant sur l'URL donnée,nous atterrsissons sur une page,avec une alerte nous demandant le flag:

![[Capture d’écran (113).png]]

Rendons nous dans la console pour plus d'éléments:

![[Capture d’écran (114).png]]

Nous avons une très longue ligne que nous allons rendre *plus visible* grâce à
https://beautifier.io/:

![[Capture d’écran (115).png]]

Seul 3 lignes sont importantes:
`l = s.split("").reverse().join("");`
`h.map(t => String.fromCharCode(t)).join("")`
`j.map(t => String.fromCharCode(t)).join("")
`
Nous allons pouvoir *interpréter* ces résultats dans la console:
![[Capture d’écran (116).png]]

Nous avons ainsi le flag décomposé !
Il faut savoir que le `l` est reverse: `l = s.split("").reverse().join("");`,donc nous devons décoder son résultat à l'envers:
`3s{MR  ━━> RM{s3`
Puis nous avons qu'à compléter avec les autres parties du flag:
`RM{s3` + `cur1ty_thr0ugh_0b` + `scur1ty}`  ━━>  `RM{s3cur1ty_thr0ugh_0bscur1ty}`
Plus qu'à tester:

![[Capture d’écran (117).png]]

Le flag est correct: **RM{s3cur1ty_thr0ugh_0bscur1ty}**