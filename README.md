# API pour activer PowerVision S1

Ce dépôt contient une simple API Flask qui simule l'api d'activation de PowerVision S1.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Docker
- Docker Compose

## Démarrage

### 1. Cloner le dépôt

```bash
git clone https://github.com/cedric-guadalupe/powervision-s1.git
cd powervision-s1
```

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
