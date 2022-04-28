class Mongo:
    """
    This is seperated pipeline of databse where you can connect with MongoDb while fetching the Data from the form
    and insert into database while calling the function
    """
    def insert(self,a,b):
        """
        :param a:this parameter is pre-define as "Data"
        :param b: its is list which will take all your data and insert into it
        :return: Returns nothing
        """
        import pymongo
        from pymongo import MongoClient
        client = pymongo.MongoClient("mongodb+srv://<ConnectionName>:<Password>@cluster0.e7t1u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client["DataBase Name"]
        collection=db["collection Name"]
        collection.insert({a,b})
        return


