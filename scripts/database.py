import os
from neo4j import GraphDatabase
from dotenv import load_dotenv
load_dotenv()

password = os.environ.get("DATABASE_PASSWORD")
username = os.environ.get("DATABASE_USERNAME")
url = os.getenv("DATABASE_URL")

# create connection to Neo4j database
driver = GraphDatabase.driver(url, auth=(username, password))

# get data from database with cypher query
def get_data(work_title):
    with driver.session() as session:
        result = session.run("""
            MATCH (w:Work)
            WHERE toLower(w.title) CONTAINS toLower($work_title)
            MATCH (w)<-[:AUTHORED]-(a:Author)-[:AUTHORED]->(relatedWork:Work)
            OPTIONAL MATCH (relatedWork)<-[:RELATED_TO]-(r:RelatedWork)
            RETURN w.title AS work_title, a.name AS author_name, relatedWork.title AS related_work_title, collect(r.id) AS related_works
        """, {"work_title": work_title})

        return [dict(row) for row in result]

