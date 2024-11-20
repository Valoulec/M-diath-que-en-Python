Notre livre, notre média 

Créer un logiciel de gestion de médiathèque 
Ces instructions vous guideront pour faire une copie sur votre machine.
Pour assurer d'avoir les versions de python a jour
ensuite copier les dossiers du GitHub

Mise en place

Installation et configuration :
1.	Cloner le dépôt :

git clone https://github.com/Valoulec/M-diath-que-en-Python
cd mediatheque
git remote remove origin

2.	Installer les dépendances :
   
pip3 install -r requirements.txt - Unix/macOS
pip install -r requirements.txt - Windows

3.	Démarrer le serveur de développement :

cd mediatheque
python3 manage.py runserver - Unix/macOS
python manage.py runserver – Windows

* Accéder aux identifiants pour le SUPER UTILISATEUR afin d'accéder à l'interface de gestion de la base de données

http://127.0.0.1:8000/admin/ 
Nom d'utilisateur : Admin 
Mot de passe : 142536Admin

