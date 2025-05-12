### 5. Préparation des données

- ***id*:** colonne inutile pour la classification --> la supprimer
- ***postal_code*:** à voir si une corrélation existe, sinon supprimer la colonne
- ***credit_score*:** 982 valeurs manquantes --> supprimer les données + vérifier si certaines valeurs sont aberrantes (valeurs trop faibles ou trop élevées par ex)
- ***children*:** certaines valeurs sont aberrantes --> les remplacer par la moyenne
Après analyse: on observe que les valeurs aberrantes sont supérieures à 1, 1 étant la valeur médiane. **Il faut donc remplacer ces valeurs aberrantes par 1.**
- ***speeding_violations*:** certaines valeurs sont aberrantes (trop élevées) --> les remplacer par la moyenne
Après analyse: on observe que la valeur la plus haute "qui a du sens" est 22. **Il faut donc remplacer les valeurs supérieures à 22 par la valeur médiane.**