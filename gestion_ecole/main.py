from fastapi import FastAPI

app = FastAPI()

db_class = []
db_student = []

@app.get("/")
def gestion_ecole():
    return "Bienvenue sur le système de gestion de l'école !"

# -----------------------------
#GESTION DES CLASSES
# -----------------------------
# Créer une classe

@app.post("/Creer_classe")
def creer_classe(id: int, nom: str, niveau: str):

    for classe in db_class:
        if classe["id"] == id:
            return { "Classe déjà existante"}
        

        

    nouvelle_classe = {
        "id": id,
        "nom": nom,
        "niveau": niveau,
         "students": []

    }

    db_class.append(nouvelle_classe)

    return {"message": "Classe créée", "classe": nouvelle_classe}



# Supprimer une classe

@app.delete("/supprimer_classe/{id}")
def supprimer_classe(id: int):
    for classe in db_class:
        if classe["id"] == id:
            db_class.remove(classe)
            return {"message": "Classe supprimée avec succès"}

    return (  "Aucune classe trouvée")



# Afficher toutes les classes

@app.get("/Affiche_liste_Classe")
def show_class():
    return db_class

#Afficher les details d'une classe
@app.get("/classe_details/{id}")
def afficher_details_classe(id: int):

    
    for classe in db_class:
        if classe["id"] == id:

            
            liste_etudiants = []
            for student in db_student:
                if student["classe_id"] == id:
                    liste_etudiants.append(student)

            return {
                "id": classe["id"],
                "nom": classe["nom"],
                "niveau": classe["niveau"],
                "nombre_etudiants": len(liste_etudiants),
                "etudiants": liste_etudiants
            }

    return {"message": "Classe introuvable"}


# -----------------------------
#GESTION DES ETUDIANTS
# -----------------------------

# Créer un étudiant


@app.post("/creer_etudiant")
def creer_etudiant(id: int, nom: str, age: int, classe_id: int):

    
    for student in db_student:
        if student["id"] == id:
            return {"message": "Un étudiant avec cet ID existe déjà"}

   
    classe_trouvee = None
    for c in db_class:
        if c["id"] == classe_id:
            classe_trouvee = c
            break

    if not classe_trouvee:
        return {"message": "Classe introuvable"}

    new_student = {
        "id": id,
        "nom": nom,
        "age": age,
        "classe_id": classe_id,
        "notes": []
    }

    db_student.append(new_student)
#Ajouter un etudiant a une classe

    classe_trouvee["students"].append(id)

    return {
        "message": "Étudiant créé et ajouté à la classe",
        "etudiant": new_student
    }

   
# Supprimer un etudiant
@app.delete("/supprimer_etudiant/{id}")
def supprimer_etudiant(id: int):

    for student in db_student:
        if student["id"] == id:
            for classe in db_class:
                if classe["id"] == student["classe_id"]:
                    if id in classe["students"]:
                        classe["students"].remove(id)

            db_student.remove(student)

            return {"message": "Étudiant retiré avec succès"}

    return {"message": "Aucun étudiant avec cet ID trouvé"}


#Rechercher un etudiant par ID
@app.get("/Rechercher_etudiant_par_ID/{id}")
def search_student(id: int):
    for student in db_student:
        if student["id"] == id:
            return student

    return("Aucun etudiant avec cet ID ")

#Afficher les informations d'un etudiant
@app.get("/Affiche_info_etudiant/{id}")
def show_info_etudiant(id: int):
 for etudiant in db_student:
     if etudiant["id"] == id:
         return {
    "message": "Information concernant cet étudiant",
    "etudiant": etudiant
}

 return{"message": "Aucun etudiant avec cet ID "}
#Modifier le informations d'un etudiant
@app.put("/modifier_etudiant/{id}")
def modifier_etudiant(id: int, nom: str = None, age: int = None, classe_id: int = None):

    for student in db_student:
        if student["id"] == id:

            if nom is not None:
                student["nom"] = nom

           
            if age is not None:
                student["age"] = age

            
            if classe_id is not None:

                
                classe_trouvee = None
                for classe in db_class:
                    if classe["id"] == classe_id:
                        classe_trouvee = classe
                        break

                if not classe_trouvee:
                    return {"message": "Nouvelle classe introuvable"}

                
                for classe in db_class:
                    if classe["id"] == student["classe_id"]:
                        if id in classe["students"]:
                            classe["students"].remove(id)

                
                classe_trouvee["students"].append(id)

                
                student["classe_id"] = classe_id

            return {
                "message": "Étudiant modifié avec succès",
                "etudiant": student
            }

    return {"message": "Étudiant introuvable"}
#Afficher le nombre total d'etudient
@app.get("/nombre_total_etudiants")
def nombre_total_etudiants():
    total = len(db_student)

    return {
        "nombre_total_etudiants": total
    }



 


