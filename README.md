# Projektarbeit-I-OpenAlex
<br></br>

# Stand 21.12.2022:
* API und Filterung das Gleiche
* Aufteilung der Aufgaben 

* Related Works noch etwas zu oberflächlich beschrieben
* https://docs.openalex.org/about-the-data/work#related_works
* Zwischenbericht am 11.01.2023

<br></br>

# Stand 19.04.2023:
- Autoren bereits aus der OpenAlex Datenbank extrahiert
- eine neue CSV Datei wurde anschließend in Neo4J importiert

In Pycharm:
* HTML Code erstellt
* Flask App 
  - Verbindung mit Neo4J hergestellt
* CSS ertstellt und variiert

Aktueller Stand:
- Web Interface mit Tabelle, welche die related Works und die dazugehörigen Links zu OpenAlex anzeigt, Autoren und eine Suchleiste bei dem das gewünschte Werk gesucht wird
- Suche funktioniert nur über Titel
* Problem: Titel muss richtig geschrieben werden, da ansonsten keine Ergebnisse angezeigt werden
  - mögliche Suchvorschläge 

Vorhaben:
- den Graphen neben der Tabelle anzeigen lassen 
 
<br></br>

# Vorschlag: 
- nach Thema suchen

<br></br>

## Einleitung
Was ist OpenAlex?
* ein offenes System zur Abbildung von Forschungsprozessen anhand der Entitäten
* basierend auf "Fünf-Einheiten-Modelle" Autoren, Werke, Orte (Zeitschriften, Repositorien), Institutionen und Konzepte, die miteinander verbunden sind
* Fokus auf Wissenschaftsdaten
* eigene API-Endpunkte 

Was ist Neo4j?
* eine eingebettete, plattenbasierte, transaktionale Datenbank-Engine, die Daten in Graphen statt in Tabellen speichert

<br></br>
## Projektbeschreibung

Das OpenAlex Katalog bietet eine gute Grundlage dafür, über die API wissenschaftliche Werke zu finden. Darüber hinaus sind  verwandte Werke zu einer bestimmten wissenschaftlichen Arbeit sichtbar.**Auf dieser Basis enstand das Projektziel, über die mit der API verbundenen Werke zu wissenschaftlichen Arbeiten von OpenAlex zu extrahieren und diese in der Graphdatenbank NEO4j visuell dazustellen. Dazu soll ein Web-Interface erstellt werden, welcher den Knowledge Graph darstellt und für die Nutzer des Web Interfaces veranschaulicht.** Vor allem **Studierende, die eine wissenschaftliche Arbeit schreiben sollen die Möglichkeit haben über ein Thema Werke zu finden, die miteinander verbunden sind und zusätzlich dazu weitere Verbindungen zu finden.** Das soll zielgreifend die Recherche der Studierenden erleichtern und sich einfacher in den Themen zu explorieren. Ein **ideales Ergebnis ist ein Minimal Viable Product**, bei dem ein Knowlegde Graph im Web Interface abgebildet ist.



![image](https://user-images.githubusercontent.com/92934375/208732448-cff613fd-4cdd-48c2-97b5-cbe929fc9b42.png)



<br></br>
### SMARTE Ziele
 __S__ :  Schnelle und unkomplizierte Möglichkeit zu haben über ein Thema Werke zu finden, die miteinander verbunden sind und zusätzlich dazu weitere Verbindungen zu finden. <br></br>
__M__ : Es soll vorerst ein kleines Subset von 100 Daten eingestetzt werden um diese visuel in ein Knowledge Graphen darszutellen , die wir dann bei erfolg erweitern. Es soll am ende ein sichbares ergebniss im Webinterface zu sehen sein.<br></br>
__A__ : Einarbeitug in neue Systeme<br></br>
__R__ : Für Wissenschaftler oder Studierende die gerade eine Arbeit verfassen oder danach suchen , sie schnell und präzise zu finden. <br></br>
__T__ : 21.07.2023
### Projektplanung


| Aufgabenname:  |  Status | Start  |   Ziellende  | endgültiges Enddatum  |  Kommentar  |
|---|---|---|---|---|---|
|  Projektkonzeption | In Bearbeitung  |  20.10.2022 |   |  	 | Aufgaben in Bearbeitung sehr viel recherchieren |
|   |   | 04.01.2023  | 04.01.2023  |   | Gruppentreffen zur Konzipierung
|   |   | 05.01.2023  | 07.01.2023  |   | Arbeit in Zweiergruppen
|   |   | 09.01.2023  | 09.01.2023  |   | Zusammenfassung der Rechercheergebnisse
|   |   | 10.01.2023  | 10.01.2023  |   | Zwischenergebnisse
| Daten extrahiert von Open Alex | offen |  01.02.2023 |  01.04.2023 |   | Open-Alex ID , Titel , Releated Work , typ, Published date |
| Daten mit NEO4J verbunden | offen |  10.03.2023 |  10.07.2023 |   | 1000 Daten hochgeladen |
| Einteilung der Aufgaben| Vollständig|  10.03.2023 |  10.07.2023 |   | in 2 Gruppen aufgeteilt |
| Gestaltug des Webinterface  | offen |  01.07.2023 |  10.07.2023 |   | Knowledge Graphen im Webinterface darstellen |
| HTML Seiten wurden erstellt  | offen |  10.03.2023 |  10.07.2023 |   | Single Page App |
| Einarbeitung in FLASK  | offen |  14.03.2023 |  10.07.2023 |   
| NEO4j mit FLASK verbunden  | offen |  17.03.2023 |  10.07.2023 |   
| Einarbeitung in Neovis.js  | offen |  26.03.2023 |  offen |   
|CSS Formatierung | offen |  14.03.2023 |  offen |  
| Github repository erstellen  |  Vollständig |  10.12.2022 |  14.12.2022 |  14.12.2022 |  |
| Texte |  in Bearbeitung  |   10.12.2022|   |   |  |
| Projektplanung   |   |   |   |   |  wir arbeiten am anfang nur mit den ersten 100 Daten und später erweitern wir uns |
| Zielsetzung  |  Vollständig | 10.12.2022  |  20.12.2022 |   | Smart ziele nennen|
|  Reccourcenpalnung |Vollständig   |  10.12.2022 | 14.2022  |   |Virtuele Maschine für später|
|  Projektablaufplan |   in Bearbeitung|  20.10.2022 |   |   ||
|  Projektausführung |   |   |   |   ||
|  Prognose |  Nicht gestartet | 10.07.2023  |  19.07.2023 |   |
| Status  |  Nicht gestartet |   10.07.2023|   19.07.2023 |  |
|  Updates |   Nicht gestartet|  10.07.2023 | 19.07.2023   |  |
|  Zielfoschung| Nicht gestartet  |  10.07.2023 | 19.07.2023 |   |
| Auswertung  |  Nicht gestartet | 10.07.2023  |  19.07.2023 |   |
<br></br>
### Ressourcen
Als Main Ressoruce wird hauptsächlich die API genutzt, die von OpenAlex bereit gestellt wird.
* https://api.openalex.org/works

* https://docs.openalex.org/download-snapshot   
* https://docs.openalex.org/download-snapshot/download-to-your-machine

Extrahierung der Daten in einer Tabelle
https://thkoelnde-my.sharepoint.com/:x:/g/personal/samaneh_ilchi_smail_th-koeln_de/ES2E0TSPY35Gq-1jtPe8EFYBAJIiaXDUq_g6RpEXrvRlWg?rtime=G2uAFdHz2kg

Beispielprojekt von Neo4j
http://my-neo4j-movies-app.herokuapp.com/

Beispiel von unserer Vorstellung des Web Interfaces
https://www.figma.com/proto/CMJOwLh9AESNhkzPg6KXir/Untitled?node-id=0%3A3&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=0%3A3


Tools :
Frontend : HTML; CSS; d3.js

Backend: Flask (funktionalität der Webapp); Neo4j Desktop

## getting started

<br></br>
## Beispiele

<br></br>
## FAQ

<br></br>
## Sicherheitserläuterungen

<br></br>


## Arbeitsweise
<br></br>
**Vorgehensweise**
1. Recherche 
2. Daten Extrahieren von Open Alex<br></br>
--> Diese Analysieren 
3. Mithilfe von Python filtern wir die Daten auf Open Alex API, Titel , Autor , Publikation, Typ und Releted Works 
4. Einarbeitung in NEO4J
-->Graphen erstellen 
5. Webinterface bauen und Graphen und Daten darstellen
 
**Vorbereitungsphase**

Die Projektinformationen werden gesammelt und erörtert, das Projektziel wird definiert und erste Vereinbarungen hinsichtlich der Projektorganisation werden getroffen. Die Vorbereitungsphase endet mit einer Projektidee und mit den verfassten SMART'en Ziele.

**Planungsphase**

Die Aufgaben werden festgelegt, ein Terminplan wird erstellt, Ressourcen und Kosten werden ermittelt. Am Ende der Planungsphase steht der Start der Umsetzungsphase.


**Umsetzungsphase**

Das Projekt wird unter Berücksichtigung von Terminen, Ressourcen und Kosten umgesetzt. Regelmäßige Sachstandsberichte werden zur Steuerung des Projekts erstellt.


**Abschlussphase**

Das Projekt wird abgeschlossen, die Arbeitsergebnisse werden abgenommen und die gesammelten Erfahrungen gesichert (Lessons Learned). Das Projekt wird vorgestellt und in einem Bericht zusammengefasst. 


Wir arbeiten klassisch, wollen jedoch zum agilen Projektmanagement wechseln soald wir unsere Projektziel erweitern.

![image](https://user-images.githubusercontent.com/92687630/228575255-c87af089-54dd-4d2d-b871-ce470b1993fb.png)

**Probleme / Fragen**

- Autoren sind vernestest in einer Liste. Müssen extrahiert werden 
- Knoten punkte sind über die URL gegeben. Ist es so in Ordung ? **Vorteil**: man wird weiter geleitet auf die URL mit den Daten / **Nachteil**: es ist unklar bis man auf den Link klickt 
- Wie man die Tabelle umänderen kann , da es mit Boostrap Schwierigkeit aufweist 
- Mit hilfe des Java Script , wissen wir nicht wie wir weiter machen soll
- Was erwarten sind von der Web app ?
- Wie stellen sie die Visualisierung vor? 
- Gibt es so welche ähnlichen Projekte an denene man sich orientieren kann. 

