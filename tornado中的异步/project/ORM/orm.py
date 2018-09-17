from .sunckMysql import SunckMySQL

class ORM():
    def save(self):
        tableName = (self.__class__.__name__).lower()
        fieldStr = valuesStr = "("
        for field in self.__dict__:
            fieldStr +=(field + ",")
            if isinstance(self.__dict__[field],str):
                valuesStr += ("'",self.__dict__[field]+"',")
            else:
                valuesStr += (str(self.__dict__[field])+",")
        fieldStr = fieldStr[:len(fieldStr)-1] + ")"
        valuesStr = valuesStr[:len(valuesStr)-1] + ")"
        sql = "insert into " + tableName + " " + fieldStr + " values " + valuesStr
        db = SunckMySQL()
        db.insert(sql)

    def __delete__(self):
        pass

    def update(self):
        pass

    @classmethod
    def all(cls):
        tableName = (cls.__name__).lower()
        sql = 'select * from ' + tableName
        db = SunckMySQL()
        return db.get_all_obj(sql,tableName)

    @classmethod
    def filter(cls):
        pass
