from database.DB_connect import DBConnect
from model.Arco import Arco
from model.Circuito import Circuito


class DAO():
    @staticmethod
    def getAllNodes():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT distinct c.*
                    from circuits c"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Circuito(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """  
                  select distinct r.`year` 
                  from races r 
                  order by r.`year` desc
                  
                  """
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res



    @staticmethod
    def getAllEges(annoMax,annoMin,idMap):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct a1.circuitId as circuito1, a2.circuitId as circuito2, a1.n+a2.n as peso
from (select distinct r.circuitId, count(*) as n
      from races r, results r2 
      where r.year BETWEEN %s and %s and r2.raceId = r.raceId 
        and r2.position is not NULL 
      group by r.circuitId 
     ) as a1,
     (select distinct r.circuitId, count(*) as n
      from races r, results r2 
      where r.year BETWEEN %s and %s and r2.raceId = r.raceId 
        and r2.position is not NULL 
      group by r.circuitId
     ) as a2
where a1.circuitId < a2.circuitId"""
        cursor.execute(query,(annoMin,annoMax,annoMin,annoMax,))

        res = []
        for row in cursor:
            res.append(Arco(idMap[row["circuito1"]],idMap[row["circuito2"]],row["peso"]))

        cursor.close()
        cnx.close()
        return res