# API pour activer PowerVision S1

Ce dépôt contient une simple API Flask qui simule l'api d'activation de PowerVision S1.

## Juste pour les dealabers

Voici un proxy déjà configuré jusqu'à lundi

Host : powervision-s1.duckdns.org
Port : 8888

### 1. Modifier Temporairement le proxy de votre téléphone


#### Iphone
Ouvrez « Paramètres ».
Allez à la section « Wi-Fi ».
À côté du réseau Wi-Fi connecté, vous verrez une icône « i ». Cliquez dessust.
En bas de la page ouverte il y aura une section « proxy HTTP », sélectionnez l’option « Manuellement ».

- Serveur : powervision-s1.duckdns.org
- Port : 8888
- Cliquez sur enregistrer

Sur android, ça doit être pareil

#### Android
Accédez aux Paramètres de votre smartphone Android
Allez dans la rubrique WiFi
Faites un appui long sur le nom du réseau auquel vous souhaitez vous connecter avec un proxy
Appuyez sur Modifier/ Gérer les paramètres du réseau
Au niveau de la boîte de dialogue qui s'ouvre, appuyez sur Afficher les options avancées
Appuyez sur le menu déroulant dans la section proxy puis sélectionnez l'option Manuel(le) pour procéder à une configuration manuelle
- Nom de l'hote ou host : powervision-s1.duckdns.org
- Port : 8888
- Cliquez sur enregistrer


### 2. Activer le gimbal Powervision S1

Lancer l'application et cliquer sur activer et mettez n'importe quoi comme numéro de téléphone et code de vérification

### 3. Important !!!!!!!!!! Désactiver le proxy

Sur Iphone : Réglages > Wi-Fi -> l'icone i (Le nom de votre wifi) > Configurer le proxy > Sélectionnez "Désactivé" & Cliquer sur enregistrer


## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Docker
- Docker Compose

## Démarrage

### 1. Cloner le dépôt ou Télécharger le repos

Mode expert
```bash
git clone https://github.com/cedric-guadalupe/powervision-s1.git
cd powervision-s1
```
Mode facile
https://github.com/cedric-guadalupe/powervision-s1/archive/refs/heads/main.zip
Tu décompresse le fichier dans un répertoire

### 2. Construire et démarrer les services

Utilisez Docker Compose pour construire et démarrer les services.

```bash
docker-compose build
docker-compose up -d
```

### 3. Modifier Temporairement le proxy de votre téléphone

Sur Iphone : Réglages > Wi-Fi -> l'icone i (Le nom de votre wifi) > Configurer le proxy > Manuel :
    - Serveur : IP local de votre PC (Par exemple chez Orange 192.168.1.?? )
    - Port : 80
    - Cliquez sur enregistrer

Sur android, ça doit être pareil

### 4. Activer le gimbal Powervision S1

Lancer l'application et cliquer sur activer et mettez n'importe quoi comme numéro de téléphone et code de vérification

### 5. Important !!!!!!!!!! Désactiver le proxy

Sur Iphone : Réglages > Wi-Fi -> l'icone i (Le nom de votre wifi) > Configurer le proxy > Sélectionnez "Désactivé" & Cliquer sur enregistrer
