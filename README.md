# Projektarbeit-I-OpenAlex


<div align="right">

Linh Nguyen, Memla Salarzei, Samaneh Ilchi und Flora Abazi 

</div>

<br></br>

## Introduction
What is OpenAlex?
* an open system that aims to illustrate and simplify research processes. 
* based on the concept of entities that are interconnected and form a "five-entity model"
* This model includes authors, works, places (journals, repositories), institutions and concepts
* has a focus on science data, which means that it is designed specifically for processing and analyzing scientific information
* It provides its own API endpoints that allow other developers to access the data and use it in other applications

What is Neo4j?
* a database engine that focuses on storing data in graphs rather than tables
* It is an embedded, disk-based and transactional database designed to effectively process and query large amounts of data
* The graph data model allows complex relationships between data points to be represented and analyzed, which is beneficial for many applications


Overall, OpenAlex and Neo4j are two different technologies designed for different purposes. OpenAlex is a research process visualization and analysis system based on a five-unit model and focused on science data. Neo4j is a database engine that specializes in storing data in graphs and analyzing relationships between data points.

**Source:**
     **https://openalex.org/**, (20.10.2022)
     **https://datascientest.com/de/neo4j-alles-ueber-die-beste-graphorientierte-datenbank,** (20.10.2022)
<br></br>
## Project description

The OpenAlex catalog provides a good basis for finding scientific works via the API. In addition, related works to a specific scientific work are visible. **On this basis, the project goal arose to extract works related to scientific works from OpenAlex via the API and to present them visually in the graph database NEO4j**. For this purpose, a web interface is to be created, which represents the knowledge graph and illustrates it for the users of the web interface. Above all, students writing a scientific paper should have the possibility to find works on a topic that are connected to each other and in addition to that to find further connections and works. This should facilitate the research of the students in a target-oriented way and make it easier to explore the topics. An **ideal result is a Minimal Viable Product, where a Knowlegde Graph is mapped in the web interface.**

![image](https://user-images.githubusercontent.com/92934375/208732448-cff613fd-4cdd-48c2-97b5-cbe929fc9b42.png)

<br></br>
## **Our Webinterface prototype:**

![image](https://user-images.githubusercontent.com/92687630/228575255-c87af089-54dd-4d2d-b871-ce470b1993fb.png)
<br></br>
## Getting started...

**Preparation Phase**
Project information is gathered and discussed, the project goal is defined, and initial agreements regarding project organization are made. The preparation phase ends with a project idea and the writing of SMART goals.

**Planning Phase**
Tasks are defined, a schedule is created, and resources and costs are identified. The planning phase ends with the start of the implementation phase.

**Implementation Phase**
The project is carried out while considering deadlines, resources, and costs. Regular status reports are created to steer the project.

**Closing Phase**
The project is completed, the work results are accepted, and the collected experiences are secured (lessons learned). The project is presented and summarized in a report.

<br></br>
### **Proceeding**
1. Research
2. Extracting data from Open Alex
--> Analyzing this data
3. Using Python to filter the data on Open Alex API, title, author, publication, type, and related works
4. Getting familiar with NEO4J
--> Creating graphs
5. Building a web interface to display graphs and data

<br></br>
### **"SMART"** Goals 
 __S__ : A quick and straightforward way to find works on a particular subject that are related to each other, in addition to discovering other connections <br></br>
__M__ : Initially, a small subset of 100 data will be used to visually represent it in a Knowledge Graph. If this is successful, this graph will be extended. The goal is to present a visible result in the web interface at the end.<br></br>
__A__ : Training in new systems<br></br>
__R__ : For scientists or students who are writing or looking for a paper to find it quickly and accurately. <br></br>
__T__ : 12.07.2023
<br></br>

<br></br>
### **Project management**

We decided to devide our Projct in two fields. Two of the project members took care of extracting, pre-processing and analyzing the Open AI dataset. They used Python to filter the data on Open Alex API, title, author, publication, type, and related works. The remaining two team members have worked intensively with the NEO4J database system to familiarize themselves with its functionality and the creation of graphs. In parallel, they have been working on the development of an appealing and intuitive user interface that allows the graphs and analyzed data to be displayed effectively. We are currently using a traditional approach but aim to switch to agile project management as soon as we expand our project goals.
<br></br> 


### **Challenges/ Questions**

* Authors are nested in a list, must be extracted 
* Node points are given by the URL. Is it ok like this ?**Advantage:** you are redirected to the URL with the data / **Disadvantage:** it is unclear until you click on the link. 
* How to change the table , because it has difficulty with Boostrap 
* Working with java script , how to proceed ?
* What do we expect from the web app ?
* How do you imagine the visualization? 
* Are there any similar projects to follow?



<br></br>
### Project planning


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

<br></br>
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
# Stand 03.05.23


<br></br>
## FAQ
<br></br>

