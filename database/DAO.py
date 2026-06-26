from database.DB_connect import DBConnect
from model.state import State
from model.sighting import Sighting


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYears():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct year(s.datetime) as year
                    from sighting s
                    order by year(s.datetime) desc"""
            cursor.execute(query)

            for row in cursor:
                result.append(row["year"])
            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getStatesForYear(year):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct st.id, st.Name 
                    from sighting s
                    join state st on st.id = s.state 
                    where year(s.`datetime`) = %s
                    order by st.Name"""
            cursor.execute(query, (year,))

            for row in cursor:
                result.append((
                    row["id"],
                    row["Name"]
                ))
            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getAllNodes(year, state):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select distinct s.*
                    from sighting s 
                    where year(s.`datetime`) = %s and s.state = %s"""
            cursor.execute(query, (year, state))

            for row in cursor:
                result.append(Sighting(**row))
            cursor.close()
            cnx.close()
        return result


    @staticmethod
    def getPossibleEdges(year, state, idMap):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select s1.id as s1id, s2.id as s2id
                    from (select distinct s.*
                    from sighting s 
                    where year(s.`datetime`) = %s and s.state = %s) s1
                    join (select distinct s.*
                    from sighting s 
                    where year(s.`datetime`) = %s and s.state = %s) s2 on s1.shape = s2.shape
                    where s1.id < s2.id """
            cursor.execute(query, (year, state, year, state))

            for row in cursor:
                result.append((
                    idMap[row["s1id"]],
                    idMap[row["s2id"]]
                ))
            cursor.close()
            cnx.close()
        return result