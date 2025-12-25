from typing import Optional
from fastapi import FastAPI,Response,HTTPException
from pydantic import BaseModel
import mysql.connector


app=FastAPI()
connecter=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kiyotaka_s_food"
)

#definition de la classe Utilisateur
class Utilisateur(BaseModel):
    nom:Optional[str]=None
    numero:str
    mot_de_passe:Optional[str]=None
    
#definition de la classe Commande
class Commande(BaseModel):
    numero:str
    produit:str
    quantite:str

#requette pour ajouter un utilisateur
@app.post("/ajouter_utilisateur")

#fonction pour ajouter un uilsateur
def ajouter_utisateur(utilisateur:Utilisateur):
    sql="INSERT INTO utilisateurs (nom,numero,mot_de_passe) VALUES (%s,%s,%s);"
    try:
        connecter=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kiyotaka_s_food"
        )
        conn=connecter.cursor(dictionary=True)
        conn.execute(sql,(utilisateur.nom,utilisateur.numero,utilisateur.mot_de_passe,))
        connecter.commit()
    finally:
        conn.close()
        connecter.close()
    return {"statut":"ajouter"}
    
#requette pour verifier l'etat d'un utilisateur dans la base
@app.post("/verifier_utilisateur")

#fonction pour verifier l'etat d'un utilisateur dans la base
def verifier_utilisateur(utilisateur:Utilisateur):
    sql="SELECT * FROM utilisateurs WHERE numero=%s ;"
    try:
        connecter=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kiyotaka_s_food"
        )
        conn=connecter.cursor(dictionary=True)
        conn.execute(sql,(utilisateur.numero,))
        resultat=conn.fetchall()
        if resultat==[]:
            return {"resultat":"existe pas"}
        else:
            return {"resultat":resultat}
    finally:
        conn.close()
        connecter.close()

