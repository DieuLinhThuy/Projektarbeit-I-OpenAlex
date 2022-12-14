# Projektarbeit-I-OpenAlex
Anmerkungen zur Vorstellung am 14.12.2022
* kleines Subset statt 300GB
* Zielgruppe definieren
* Planungsweise genauer beschreiben 
  * nächsten Schritte einplanen 
  * Deadlines genauer beschreiben (bsp: bis zu diesem Datum eine CSV)
  * explorierend --> Was brauchen wir?
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
In unserem Projekt sollen OpenAlex und Neo4j zur visuellen Darstellungen der Daten miteinander verbunden werden.
Unser Projektziel ist es einen Knowledge Graphen mithilfe der Graphdatenbank NEO4j zu erstellen. Die Daten hierzu sollen durch die API von dem Opensource Wissenschaftskatalog OpenAlex extrahiert werden, um die Zitationsdaten(?) von Artikeln in einem Web Interface darzustellen.Ein ideales Endergebnis wäre ein Minimal Viable Products, bei dem der Knowlegde Graph im Web Interface abgebildet ist.

<br></br>

### Projektplanung
https://thkoelnde-my.sharepoint.com/:x:/g/personal/memla_salarzei_smail_th-koeln_de/ES1BHrW9n61Gg_Oeo1l6ZJIBQ9dX7qpLtS2gWV-4FPxCUQ?rtime=J7RlVkLd2kg

<br></br>
### Ressourcen
"Die API ist der primäre Weg, um OpenAlex-Daten zu erhalten. Es ist auch viel einfacher, als Download snapshot herunterzuladen."
https://api.openalex.org/works?filter=cites:W2741809807 <br></br>
https://api.openalex.org/works?filter=cited_by:W2766808518

"Verwenden Sie kein Cursor-Paging, um einen sehr großen oder sogar den gesamten Datensatz herunterzuladen Es ist schlecht für Sie, weil es viele Tage dauern wird, eine lange Liste wie '/works' oder '/authors' durchzublättern. Es ist schlecht für die OpenAlex-API (und andere Benutzer!), weil es ihre Server massiv belastet. Laden Sie stattdessen alles auf einmal herunter, indem Sie den Daten-Snapshot verwenden. Es ist kostenlos, einfach, schnell und Sie erhalten alle Ergebnisse im gleichen Format wie von der API.
Auf Ihren Computer herunterladen"
https://docs.openalex.org/download-snapshot <br></br>
https://docs.openalex.org/download-snapshot/download-to-your-machine


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

 
**Vorbereitungsphase**

Die Projektinformationen werden gesammelt und erörtert, das Projektziel wird definiert und erste Vereinbarungen hinsichtlich der Projektorganisation werden getroffen. Die Vorbereitungsphase endet mit einer Projektidee und mit den verfassten SMART'en Ziele.

**Planungsphase**

Die Aufgaben werden festgelegt, ein Terminplan wird erstellt, Ressourcen und Kosten werden ermittelt. Am Ende der Planungsphase steht der Start der Umsetzungsphase.


**Umsetzungsphase**

Das Projekt wird unter Berücksichtigung von Terminen, Ressourcen und Kosten umgesetzt. Regelmäßige Sachstandsberichte werden zur Steuerung des Projekts erstellt.


**Abschlussphase**

Das Projekt wird abgeschlossen, die Arbeitsergebnisse werden abgenommen und die gesammelten Erfahrungen gesichert (Lessons Learned). Das Projekt wird vorgestellt und in einem Bericht zusammengefasst. 


Wir arbeiten klassisch, wollen jedoch zum agilen Projektmanagement wechseln soald wir unsere Projektziel erweitern.

