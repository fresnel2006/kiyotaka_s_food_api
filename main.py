from typing import Optional
from fastapi import FastAPI,Request
from pydantic import BaseModel
import time
import mysql.connector


app=FastAPI()

clients={}

fenetre_de_temps=60
limite=5


@app.get("/")
def teste(request: Request):
    ip = request.client.host
    temps_client = int(time.time())

    if ip not in clients:
        clients[ip] = {"temps": temps_client, "nombre de requette": 1}
    else:
        if clients[ip]["nombre de requette"]>limite :
            if int(time.time())-clients[ip]["temps"]>fenetre_de_temps:
                clients[ip]["nombre de requette"]=1
            else:
                return {"resultat":"trop de requette petit hacker"}
        else:
            clients[ip]["nombre de requette"]=clients[ip]["nombre de requette"]+1
            clients[ip]["temps"]=int(time.time())
            print(clients[ip])
            return {"resultat":"valide"}
#definition de la classe Utilisateur
class Utilisateur(BaseModel):
    nom:Optional[str]=None
    numero:Optional[str]=None
    mot_de_passe:Optional[str]=None
    numero_utilisation:Optional[str]=None
    
#definition de la classe Commande
class Commande_produit(BaseModel):
    nom:str
    numero:str
    produit:str
    quantite:str
    prix_produit:str

#requette pour ajouter un utilisateur
@app.post("/ajouter_utilisateur")


#fonction pour ajouter un uilsateur
def ajouter_utisateur(request:Request,utilisateur:Utilisateur):
    ip = request.client.host
    temps_client = int(time.time())

    if ip not in clients:
        clients[ip] = {"temps": temps_client, "nombre de requette": 1}
        pass
    else:
        if clients[ip]["nombre de requette"] >= limite:
            if int(time.time()) - clients[ip]["temps"] > fenetre_de_temps:
                clients[ip]["nombre de requette"] = 1
                pass
            else:
                return {"resultat": "trop de requette petit hacker"}
        else:
            clients[ip]["nombre de requette"] = clients[ip]["nombre de requette"] + 1
            clients[ip]["temps"] = int(time.time())
            print(clients[ip])
            pass
    sql="INSERT INTO utilisateurs (nom,numero,mot_de_passe) VALUES (%s,%s,%s);"
    try:
        connecter=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kiyotaka_s_food"
        )
        conn=connecter.cursor()
        conn.execute(sql,(utilisateur.nom,utilisateur.numero,utilisateur.mot_de_passe,))
        connecter.commit()
    finally:
        conn.close()
        connecter.close()
    return {"statut":"ajouter"}
    
#requette pour verifier l'etat d'un utilisateur dans la base
@app.post("/verifier_utilisateur")

#fonction pour verifier l'etat d'un utilisateur dans la base
def verifier_utilisateur(request:Request,utilisateur:Utilisateur):
    ip = request.client.host
    temps_client = int(time.time())

    if ip not in clients:
        clients[ip] = {"temps": temps_client, "nombre de requette": 1}
        pass
    else:
        if clients[ip]["nombre de requette"] >= limite:
            if int(time.time()) - clients[ip]["temps"] > fenetre_de_temps:
                clients[ip]["nombre de requette"] = 1
                pass
            else:
                return {"resultat": "trop de requette petit hacker"}
        else:
            clients[ip]["nombre de requette"] = clients[ip]["nombre de requette"] + 1
            clients[ip]["temps"] = int(time.time())
            print(clients[ip])
            pass
    sql="SELECT * FROM utilisateurs WHERE numero=%s ;"
    try:
        connecter=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kiyotaka_s_food"
        )
        conn=connecter.cursor()
        conn.execute(sql,(utilisateur.numero,))
        resultat=conn.fetchall()
        if resultat==[]:
            return {"resultat":"existe pas"}
        else:
            return {"resultat":resultat}
    finally:
        conn.close()
        connecter.close()


#fonction pour reconnecter un utilisateur
@app.post("/reconnecter_utilisateur")

def reconnecter_utilisateur(request:Request,reconnexion:Utilisateur):
    ip = request.client.host
    temps_client = int(time.time())

    if ip not in clients:
        clients[ip] = {"temps": temps_client, "nombre de requette": 1}
        pass
    else:
        if clients[ip]["nombre de requette"] >= limite:
            if int(time.time()) - clients[ip]["temps"] > fenetre_de_temps:
                clients[ip]["nombre de requette"] = 1
                pass
            else:
                return {"resultat": "trop de requette petit hacker"}
        else:
            clients[ip]["nombre de requette"] = clients[ip]["nombre de requette"] + 1
            clients[ip]["temps"] = int(time.time())
            print(clients[ip])
            pass
    sql="SELECT nom,numero FROM utilisateurs WHERE numero=%s AND mot_de_passe=%s"
    try:
        connecter=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kiyotaka_s_food"
        )
        conn=connecter.cursor()
        conn.execute(sql,(reconnexion.numero,reconnexion.mot_de_passe))
        resultat=conn.fetchall()
        if resultat==[]:
            return {"resultat":"existe pas"}
        else:
            return {"resultat":resultat}
    finally:
        conn.close()
        connecter.close()

#fonction pour enregistrer les commandes dans la base de donnees
@app.post("/enregistrer_commande")
def enregistrer_commande(request:Request,commande:Commande_produit):
    ip = request.client.host
    temps_client = int(time.time())

    if ip not in clients:
        clients[ip] = {"temps": temps_client, "nombre de requette": 1}
        pass
    else:
        if clients[ip]["nombre de requette"] >=limite:
            if int(time.time()) - clients[ip]["temps"] > fenetre_de_temps:
                clients[ip]["nombre de requette"] = 1
                pass
            else:
                return {"resultat": "trop de requette petit hacker"}
        else:
            clients[ip]["nombre de requette"] = clients[ip]["nombre de requette"] + 1
            clients[ip]["temps"] = int(time.time())
            print(clients[ip])
            pass
    sql="INSERT INTO commande (numero,quantite,produit,nom,prix_produit) VALUES (%s,%s,%s,%s,%s);"
    try:
        connecter = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kiyotaka_s_food"
        )
        conn=connecter.cursor()
        conn.execute(sql,(commande.numero,commande.quantite,commande.produit,commande.nom,commande.prix_produit))
        connecter.commit()
        return {"resultat":"commande ajoutée"}
    finally:
        conn.close()
        connecter.close()

@app.post("/modifier_utilisateur")
def modifier_utilisateur(request:Request,modifier:Utilisateur):

    ip = request.client.host
    temps_client = int(time.time())

    if ip not in clients:
        clients[ip] = {"temps": temps_client, "nombre de requette": 1}
        pass
    else:
        if clients[ip]["nombre de requette"] >= 3:
            if int(time.time()) - clients[ip]["temps"] > fenetre_de_temps:
                clients[ip]["nombre de requette"] = 1
                pass
            else:
                return {"resultat": "trop de requette petit hacker"}
        else:
            clients[ip]["nombre de requette"] = clients[ip]["nombre de requette"] + 1
            clients[ip]["temps"] = int(time.time())
            print(clients[ip])
            pass
    sql=("UPDATE utilisateurs SET nom=%s, mot_de_passe=%s WHERE numero=%s;")
    try:
        connecter = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kiyotaka_s_food"
        )
        conn=connecter.cursor()
        conn.execute(sql,(modifier.nom,modifier.mot_de_passe,modifier.numero_utilisation))
        connecter.commit()
        return {"resultat":"modifications ajoutées"}
    finally:
        conn.close()
        connecter.close()

#fonction pour envoyer les commandes
@app.get("/ensemble_des_commandes")
def envoie_des_commandes():
    sql="SELECT * FROM commande;"
    try:
        connecter = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kiyotaka_s_food"
        )
        conn=connecter.cursor()
        conn.execute(sql)
        resultat = conn.fetchall()
        if resultat == []:
            return {"resultat": "existe pas"}
        else:
            return {"resultat": resultat}
    finally:
        conn.close()
        connecter.close()

