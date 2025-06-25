#da lab 12
#ha il fetchone
@staticmethod
def getConnection(retailer1, year, nation, retailer2):
    result = None
    try:
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """ 

                   select count(*) as weight
                   from (
                       select distinct (gds.Product_number ), year (gds.`Date`) as year, gr.Country
                       from go_sales.go_retailers gr,  go_sales.go_daily_sales gds
                       where gr.Retailer_code = %s and year (gds.`Date`) = %s
                       and gr.Retailer_code = gds.Retailer_code and gr.Country = %s
                       ) as t1, 
                       (select distinct (gds.Product_number ), year (gds.`Date`) as year, gr.Country
                       from go_sales.go_retailers gr,  go_sales.go_daily_sales gds
                       where gr.Retailer_code = %s and gr.Retailer_code = gds.Retailer_code 
                       ) as t2
                   where t1.Product_number = t2.Product_number and t1.Country = t2.Country and t1.year = t2.year  

                  """
        cursor.execute(query, (retailer1.Retailer_code, year, nation, retailer2.Retailer_code))
        row = cursor.fetchone()

        result = Connection(retailer1.Retailer_code, retailer2.Retailer_code, row["weight"]) if row else 0

    except Exception as e:
        print(f"Error fetching: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return result

#esempio di metodo dao fatcone da iTunes
@staticmethod
    def getEdge(AlbumId1, AlbumId2):
        cnx = DBConnect.get_connection()
        result = None
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select count(*) as cont
                        from itunes.playlisttrack p , itunes.track t  , itunes.playlisttrack p2, itunes.track t2
                        where 	t.AlbumId = %s
                                and t2.AlbumId = %s
                                and t.trackId = p.trackId
                                and t2.trackId = p2.trackId
                                and p.PlaylistId = p2.PlaylistId
                                and p.TrackId <> p2.TrackId
                                                    """
            cursor.execute(query, (AlbumId1, AlbumId2))

            row = cursor.fetchone()
            result= int(row["cont"])
            cursor.close()
            cnx.close()
        return result


#esempio di query molto complessa da Esame-del-30-06-2021-Pomeriggio-
def getEdges(self):
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """select t.l1, t.l2, count(distinct(t.type)) as weight
                    from
                        (select c.Localization as l1, c2.Localization as l2, i.`Type` as type
                        from genes_small.classification c, genes_small.interactions i, genes_small.classification c2
                        where c.GeneID = i.GeneID1
                                and c2.GeneID = i.GeneID2
                                and c.Localization > c2.Localization
                        union ALL
                        select c.Localization as l1, c2.Localization as l2, i.`Type` as type
                        from genes_small.classification c, genes_small.interactions i, genes_small.classification c2
                        where c.GeneID = i.GeneID2
                                and c2.GeneID = i.GeneID1
                                and c.Localization > c2.Localization) as t
                    group by t.l1, t.l2

                    """
        cursor.execute(query, )

        for row in cursor:
            result.append((row["l1"], row["l2"], row["weight"]))
        cursor.close()
        cnx.close()
    return result


#esempio di query difficile da Esame-del-30-06-2021-Mattino-
@staticmethod
def getEdges():
    cnx = DBConnect.get_connection()
    result = []
    if cnx is None:
        print("Connessione fallita")
    else:
        cursor = cnx.cursor(dictionary=True)
        query = """select t.c1, t.c2, sum(t.weight) as weight
                    from
                        (select g.Chromosome as c1, g2.Chromosome as c2, i.Expression_Corr as weight, i.Type
                        from genes_small.genes g, genes_small.interactions i, genes_small.genes g2 
                        where g.GeneID = i.GeneID1 
                            and g2.GeneID = i.GeneID2
                            and i.GeneID1 <> i.GeneID2
                            and g.Chromosome > 0
                            and g2.Chromosome > 0
                            and g.Chromosome <> g2.Chromosome
                        group by g.Chromosome, g2.Chromosome, i.Expression_Corr, i.Type) as t
                    group by t.c1, t.c2
                        """
        cursor.execute(query, )

        for row in cursor:
            result.append((row["c1"], row["c2"], row["weight"]))
        cursor.close()
        cnx.close()
        return result