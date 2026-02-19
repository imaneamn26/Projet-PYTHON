AMINOU IMANE 



# SUJET 1  Gestion des Étudiants et des Classes – API FastAPI

## Description

Ce projet est une API développée avec FastAPI permettant de gérer des classes et des étudiants.

L’application permet de :

* Créer, modifier et supprimer des étudiants
* Créer et supprimer des classes
* Associer des étudiants à des classes
* Afficher les détails d’une classe (nombre d’étudiants et liste)
* Obtenir le nombre total d’étudiants


## Technologies utilisées

* Python 3
* FastAPI
* Uvicorn






## Structure des données

### Étudiant

Un étudiant contient :

* id : identifiant unique
* nom : nom de l’étudiant
* age : âge de l’étudiant
* classe_id : identifiant de la classe associée

### Classe

Une classe contient :

* id : identifiant unique
* nom : nom de la classe
* niveau : niveau de la classe
* students : liste des identifiants des étudiants

---



### Classes

* POST /creer_classe
* DELETE /supprimer_classe/{id}
* GET /details_classe/{id}

### Étudiants

* POST /creer_etudiant
* PUT /modifier_etudiant/{id}
* DELETE /supprimer_etudiant/{id}
* GET /afficher_etudiant/{id}

### Statistiques

* GET /nombre_total_etudiants
* GET /nombre_etudiants_par_classe/{classe_id}



## Fonctionnalités implémentées

* Gestion complète des classes
* Gestion complète des étudiants
* Modification partielle des informations d’un étudiant
* Calcul du nombre total d’étudiants
* Calcul du nombre d’étudiants par classe


## Limites du projet

* Les données ne sont pas persistées (perdues au redémarrage)
* Aucune base de données n’est utilisée
* Pas d’authentification


## Améliorations possibles


* Utilisation de Pydantic pour la validation avancée
* Ajout de la gestion des notes
* Ajout d’une authentification
* Ajout de tests unitaires




