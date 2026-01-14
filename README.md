# Vitality CS2 – Calendrier Automatique

Ce dépôt contient un calendrier ICS mis à jour manuellement, auquel Google Calendar peut s’abonner pour afficher automatiquement les matchs de Team Vitality CS2.

## 📁 Fichiers

- `vitality.ics` : le calendrier principal
- `events/template.txt` : modèle d’événement ICS à copier-coller

## 🛠️ Ajouter un match

1. Ouvrir `vitality.ics`
2. Ajouter un bloc `BEGIN:VEVENT ... END:VEVENT` juste avant `END:VCALENDAR`
3. Commit + push

Google Calendar mettra automatiquement à jour le calendrier dans les minutes suivantes.

## 🔗 S’abonner au calendrier dans Google Calendar

1. Aller sur Google Calendar
2. Dans la colonne de gauche, cliquer sur **"Autres agendas"**
3. Choisir **"S'abonner à un agenda via URL"**
4. Coller l’URL RAW du fichier `vitality.ics`, par exemple :

