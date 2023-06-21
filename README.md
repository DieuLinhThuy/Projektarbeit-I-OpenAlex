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


<br></br>
## **Our Webinterface prototype:**
<img width="544" alt="image" src="https://github.com/DieuLinhThuy/Projektarbeit-I-OpenAlex/assets/92934375/1265b49f-ee3a-489a-b8b5-a5fa2530644c">

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

**Did we achieve our SMART goals?**

**SMART goal achievement**: We were able to successfully achieve our specific goals by accomplishing the desired outcome, which was to create a webpage featuring authors and their relationships.
**Dataset**: We have a dataset of 100x10 data points that can be visualized in a knowledge graph.
**Web interface**: The final web interface is visually appealing and user-friendly, catering to the needs of students.

Overall, we can conclude that our SMART goals were effectively met. We successfully developed a webpage with author information and relationships, utilized a dataset in a knowledge graph format, and created a web interface suitable for student


<br></br>
### **Project management**

We decided to devide our Projct in two fields. Two of the project members took care of extracting, pre-processing and analyzing the Open AI dataset. They used Python to filter the data on Open Alex API, title, author, publication, type, and related works. The remaining two team members have worked intensively with the NEO4J database system to familiarize themselves with its functionality and the creation of graphs. In parallel, they have been working on the development of an appealing and intuitive user interface that allows the graphs and analyzed data to be displayed effectively. We are currently using a traditional approach but aim to switch to agile project management as soon as we expand our project goals.
<br></br> 


### **Challenges/ guidelines**

* Authors are nested in a list, must be extracted 
* Node points are given by the URL. Is it ok like this ?**Advantage:** you are redirected to the URL with the data / **Disadvantage:** it is unclear until you click on the link. 
* How to change the table , because it has difficulty with Boostrap 
* Working with java script , how to proceed ?
* What do we expect from the web app ?
* How do you imagine the visualization? 
* Are there any similar projects to follow?

### **Ressources**
The main ressoruce used is the API provided by OpenAlex.
* https://api.openalex.org/works

* https://docs.openalex.org/download-snapshot   
* https://docs.openalex.org/download-snapshot/download-to-your-machine

Extraction of the data in a table
https://thkoelnde-my.sharepoint.com/:x:/g/personal/samaneh_ilchi_smail_th-koeln_de/ES2E0TSPY35Gq-1jtPe8EFYBAJIiaXDUq_g6RpEXrvRlWg?rtime=G2uAFdHz2kg

Neo4j sample project
http://my-neo4j-movies-app.herokuapp.com/

Example from our presentation of the web interface
https://www.figma.com/proto/CMJOwLh9AESNhkzPg6KXir/Untitled?node-id=0%3A3&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=0%3A3

<br></br>
### **Tools**
 *Frontend:*  HTML;  CSS;  Bokeh , network x
 
 
 *Backend:* Flask (functionality of the webapp);  Neo4j Desktop

<br></br>

<br></br>
### Project planning


| Task name:  |  Status | Start  |   Target end | final end date  |  Comment  |
|---|---|---|---|---|---|
|  Project conception | In process  |  20.10.2022 |   |  21.06.2023	 | Tasks in progress a lot of research |
|   |   | 04.01.2023  | 04.01.2023  | | Group meeting for conception
|   |   | 05.01.2023  | 07.01.2023  |  | Work in groups of two
|   |   | 09.01.2023  | 09.01.2023  |   | Summary of the research results
|   |   | 10.01.2023  | 10.01.2023  |   | Interim results
| Create Github repository  |  Complete |  10.12.2022 |  14.12.2022 |  14.12.2022 |  |
| Texts |  in progress  |   10.12.2022|   |  20.06.2023  |   |
| Project planning   |   |   |   |   |  we work at the beginning only with the first 100 data and later we expand |
| Target  |  complete | 10.12.2022  |  20.12.2022 | 20.12.2022 | Name SMART goals|
|  Resource Planning |complete   |  10.12.2022 | 14.2022  |   |Virtual machine for later|
|  Project schedule |   in progress |  20.10.2022 |   |  21.06.2023  ||
| Evaluation  |  complete | 10.06.2023  |  19.06.2023 | 20.06.2023|
| Data extracted from Open Alex | complete |  01.02.2023 |  01.04.2023 | 01.04.2023  | Open-Alex ID , Titel , Releated Work , type, Published date, author, theme |
| Data connected with NEO4J | complete |  10.03.2023 |  19.04.2023 | 10.04.2023 | 1000 data uploaded |
| Classification of tasks| complete|  10.03.2023 |  19.04.2023 | 10.04.2023 | in 2 Gruppen aufgeteilt |
| Design of the web interface  | open |  01.07.2023 |  19.04.2023 | 10.04.2023 | Displaying Knowledge Graph in the Web Interface , Improving Aesthetics  |
| HTML pages were created  | complete |  10.03.2023 |  19.04.2023 | 10.04.2023 | Single Page App |
| Familiarization with FLASK  | complete |  14.03.2023 |  10.04.2023 | 20.04.2022 |
| NEO4j connected with FLASK  | complete |  17.03.2023 |  19.04.2023 |  20.04.2022 |
| Familiarization with Neovis.js  | incomplete |  26.03.2023 | 10.04.2023 |   25.04.2022 | idea was discarded |
|Familiarization with bokeh| complete |  20.04.2023 |  05.05.2023 |  20.05.2022 |
|Familiarization with network x|complete |  17.03.2023 |  19.04.2023 |  20.04.2022 |
|CSS formatting | open |  14.03.2023 |  open | 10.04.2023 |
|add Grapf |complete |  17.04.2023 |  19.04.2023 |  10.06.2022 |
|web interface optimization | open | 25.03.2023 |  19.04.2023 |  25.06.2022 | there is still room for improvement|

<br></br>

<br></br>

# Status 21.12.2022:
 *Current status:*
- API and filtering are the same

- Tasks have been divided

- Related Works are described too superficially

https://docs.openalex.org/about-the-data/work#related_works

- Interim report due on January 11th, 2023

<br></br>

# Status 19.04.2023:

Authors have been extracted from the OpenAlex database
a new CSV file was then imported into Neo4J

*In Pycharm:*

- HTML code has been created
- Flask app
Connected to Neo4J
- Created and varied CSS

*Current status:*

- Web interface with a table that displays related works and their corresponding links to OpenAlex, authors, and a search bar where the desired work can be searched for
Search function only works through title
- It is only searched in one column
**Problem:** Title must be spelled correctly, otherwise no results will be displayed
- Possible search suggestions

*next Step:*
- Display the graph next to the table
- Search: deep learning
- Improve search: do not distinguish between uppercase and lowercase letters Not only by title, but also by subject
- Fuzzy search recommended, Main Subject is the name of the property,
- Make the page fuller, graphs should be visible, build graphs into the website

<br></br>
 
# Status 17.05.2023:
*Current status:*
- We have a graph, on our web interface. 
  - but is not yet interactive and does not show a network 
- tried to use lowercase with neo4j as well as with python code

*next step*
- Beautify web interface & continue working on the Knowledge Graph

# Status 07.06.2023:
*curent status*
- repository updated
- Graph is active
  - notes are interactive
- case sensitive worked

  
![image](https://github.com/DieuLinhThuy/Projektarbeit-I-OpenAlex/assets/92687630/36776f6b-b5ad-4c04-ac10-15bad127e565)


# Conclusion #
- First independent project spanning multiple semesters.
- Improved and applied project management skills in practice.
- Acquired new knowledge throughout the project.
- Occasionally challenging and time-consuming.
- Nonetheless, enjoyable and fulfilling.
- Achieved a sense of accomplishment.
- Demonstrated effective teamwork.

<br></br>
## FAQ
<br></br>

