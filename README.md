# 🟡 Vitality CS2 – Calendrier Automatique (ICS)

Ce dépôt génère automatiquement un calendrier ICS contenant tous les matchs de Team Vitality sur Counter‑Strike 2, avec les scores mis à jour dès qu’ils sont disponibles.

Le calendrier est mis à jour **toutes les heures** grâce à GitHub Actions.  
Google Calendar récupère automatiquement les nouvelles données via l’URL RAW du fichier `vitality.ics`.

---

## 📅 Fonctionnalités

- Ajout automatique des nouveaux matchs Vitality (HLTV)
- Mise à jour automatique des scores finaux
- Format ICS compatible Google Calendar, iPhone, Android, Outlook, etc.
- Mise à jour toutes les heures
- Aucun clic manuel nécessaire une fois installé

---

## 📁 Structure du dépôt
vitality-calendar/
│
├── vitality.ics                 # Calendrier ICS généré automatiquement
├── README.md                    # Ce fichier
│
├── scripts/
│   ├── fetch_matches.py        # Récupère les matchs Vitality depuis HLTV
│   └── generate_ics.py         # Génère le fichier ICS complet
│
└── .github/
└── workflows/
└── update.yml           # GitHub Action qui met à jour le calendrier

---

## 🔧 Installation (Google Calendar)

### 1. Récupérer l’URL RAW du fichier ICS

Dans GitHub :

1. Ouvrir `vitality.ics`
2. Cliquer sur **Raw**
3. Copier l’URL :
https://raw.githubusercontent.com/brazatlant/vitality-calendar/main/vitality.ics


### 2. Ajouter le calendrier dans Google Calendar

1. Ouvrir Google Calendar  
2. Dans la colonne de gauche, cliquer sur **Autres agendas**  
3. Choisir **S’abonner à un agenda via URL**  
4. Coller l’URL RAW  
5. Valider

Google Calendar va maintenant surveiller automatiquement ton fichier ICS.

---

## 🔄 Fonctionnement automatique

Toutes les heures :

1. GitHub Actions exécute `fetch_matches.py`
2. Les matchs Vitality (à venir + passés) sont récupérés
3. Les scores finaux sont détectés
4. `generate_ics.py` régénère le fichier `vitality.ics`
5. Le fichier est mis à jour dans le dépôt
6. Google Calendar récupère automatiquement les changements

Tu n’as rien à faire.

---

## 🧪 Déclenchement manuel

Tu peux aussi lancer la mise à jour manuellement :

- Aller dans l’onglet **Actions** du dépôt
- Choisir **Update Vitality Calendar**
- Cliquer sur **Run workflow**

---

## 📝 Notes techniques

- Le fichier ICS doit rester **public** pour que Google Calendar puisse y accéder.
- Le champ `UID:` de chaque événement reste constant pour permettre la mise à jour des scores.
- Les heures sont générées en UTC (`Z`) pour compatibilité maximale.

---

## 📬 Support

Si tu veux ajouter :
- d’autres équipes,
- d’autres jeux,
- un calendrier multi‑équipes,
- un flux ICS séparé par tournoi,

tu peux étendre ce dépôt ou ouvrir une issue.

---

## 🟡 Auteur

Automatisation conçue pour **Brazatlant**, passionné de Vitality et d’optimisation technique.
