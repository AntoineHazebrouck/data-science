### 5. Préparation des données

#### Données aberrantes :
- ***children*:** certaines valeurs sont aberrantes --> les remplacer par la moyenne
Après analyse: on observe que les valeurs aberrantes sont supérieures à 1, 1 étant la valeur médiane. **Il faut donc remplacer ces valeurs aberrantes par 1.**
- ***speeding_violations*:** certaines valeurs sont aberrantes (trop élevées) --> les remplacer par la moyenne
Après analyse: on observe que la valeur la plus haute "qui a du sens" est 22. **Il faut donc remplacer les valeurs supérieures à 22 par la valeur médiane.**

#### Données manquantes

- ***credit_score*:** 982 valeurs manquantes --> remplir par une donnée moyenne/mediante
- ***annual_mileage*:** 957 valeurs manquantes --> remplir par une donnée moyenne/mediante

#### Données irrelevantes

- ***id*:** colonne inutile pour la classification --> la supprimer
- ***postal_code*:** à voir si une corrélation existe, sinon supprimer la colonne

#### Transformation qualitatif vers numérique


