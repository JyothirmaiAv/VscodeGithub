
# Kinokarten-Buchungssystem

Ein Python-Skript, das den Endpreis eines Kinotickets berechnet – 
basierend auf Alter, Mitgliedschaftsstatus, Sitzplatztyp und Vorstellungszeit. 
Dabei werden Bedingungen (if/else-Logik) genutzt, um Berechtigung, 
Rabatte und Zuschläge zu prüfen.

## Was das Skript macht
- Prüft, ob der Nutzer alt genug ist, um ein Ticket zu buchen (17+) und ob er Abendvorstellungen buchen darf (21+)
- Wendet einen Mitgliedsrabatt an, wenn der Nutzer Mitglied und mindestens 21 Jahre alt ist
- Berechnet Zuschläge für Wochenend- oder Abendvorstellungen
- Berechnet Servicegebühren je nach Sitzplatztyp (Premium, Gold oder Standard)
- Kombiniert alle Bedingungen, um zu entscheiden, ob die Buchung erlaubt ist, und gibt den Endpreis aus

## Verwendete Konzepte
Bedingte Anweisungen (`if` / `elif` / `else`), logische Operatoren (`and`, `or`), 
Vergleichsoperatoren, Kombination mehrerer Bedingungen

## Beispiel-Ausgabe
