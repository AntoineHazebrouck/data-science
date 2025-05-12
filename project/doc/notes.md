### 5. Préparation des données

- ***id*:** colonne inutile pour la classification --> la supprimer
- ***postal_code*:** à voir si une corrélation existe, sinon supprimer la colonne
- ***credit_score*:** 982 valeurs manquantes --> supprimer les données + vérifier si certaines valeurs sont aberrantes (valeurs trop faibles ou trop élevées par ex)
- ***children*:** certaines valeurs sont aberrantes --> les remplacer par la moyenne
- ***speeding_violations*:** certaines valeurs sont aberrantes (trop élevées) --> les remplacer par la moyenne