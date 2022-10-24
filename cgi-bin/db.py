import mysql.connector
import hashlib
import sys

class DB:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()


    def getNCiudad(self,id):
        sql = f'''
            SELECT nombre, pais
            FROM ciudad
            WHERE id = {id}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getNPais(self,id):
        sql = f'''
            SELECT nombre
            FROM pais
            WHERE id = {id}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getKilos(self,id):
        sql = f'''
            SELECT valor
            FROM kilos_encargo
            WHERE id = {id}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def getEspacio(self,id):
        sql = f'''
            SELECT valor
            FROM espacio_encargo
            WHERE id = {id}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def getPath(self,id):
        sql = f'''
            SELECT ruta_archivo
            FROM foto
            WHERE encargo_id = {id}
        '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def save_viaje(self, data):
        
        try:
            sql ='''
                INSERT INTO  viaje (origen, destino, fecha_ida, fecha_regreso, kilos_disponible, espacio_disponible, email_viajero, celular_viajero)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                '''
            self.cursor.execute(sql, data)  # ejecuto la consulta
            self.db.commit()                # modifico la base de datos
            
        except Exception as e:
            print(e)
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def save_encargo(self, data):
        foto1 = data[7]
        filename1 = foto1.filename
        sql = "SELECT COUNT(id) FROM foto" 
        self.cursor.execute(sql)
        total = self.cursor.fetchall()[0][0] + 1
        filename_hash1 = hashlib.sha256(filename1.encode()).hexdigest()[0:30] 
        filename_hash1 += f"_{total}" 
        if(len(data)>=9):
            foto2 = data[8]
            filename2 = foto2.filename
            filename_hash2 = hashlib.sha256(filename2.encode()).hexdigest()[0:30] 
            filename_hash2 += f"_{total+1}" 
        if(len(data)==10):
            foto3 = data[9]
            filename3 = foto3.filename
            filename_hash3 = hashlib.sha256(filename3.encode()).hexdigest()[0:30] 
            filename_hash3 += f"_{total+2}" 
        
        try:
            sql ='''
                INSERT INTO encargo (descripcion, espacio, kilos, origen, destino, email_encargador, celular_encargador) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
            self.cursor.execute(sql, data[:7])
            id_encargo = self.cursor.getlastrowid()

            open(f"../media/{filename_hash1}", "wb").write(foto1.file.read()) 
            sql_file = '''
                INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id) 
                VALUES (%s, %s, %s)
                '''
            self.cursor.execute(sql_file, (filename_hash1, filename1, id_encargo)) 

            if(len(data)>=9):
                open(f"../media/{filename_hash2}", "wb").write(foto2.file.read()) 
                sql_file = '''
                    INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id) 
                    VALUES (%s, %s, %s)
                    '''
                self.cursor.execute(sql_file, (filename_hash2, filename2, id_encargo))
            if(len(data)==10):
                open(f"../media/{filename_hash3}", "wb").write(foto3.file.read()) 
                sql_file = '''
                    INSERT INTO foto (ruta_archivo, nombre_archivo, encargo_id) 
                    VALUES (%s, %s, %s)
                    '''
                self.cursor.execute(sql_file, (filename_hash3, filename3, id_encargo))

            self.db.commit()                # modifico la base de datos
            
        except:
            print("ERROR AL GUARDAR EN LA BASE DE DATOS")
            sys.exit()

    def get_pais(self):
        
        sql = '''
            SELECT * FROM pais
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_ciudad(self):
        
        sql = '''
            SELECT * FROM ciudad
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get1Viaje(self,id):
        sql =f'''
            SELECT * FROM viaje WHERE id= {id}
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def get1Encargo(self,id):
        sql =f'''
            SELECT * FROM encargo WHERE id= {id}
            '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get5Viajes(self,id):
        limit = str(5*(int(id)-1))
        if(id=='0'):
            sql = '''
                SELECT * FROM viaje
                '''
        elif(id=='1'):
            sql = '''
                SELECT * FROM viaje ORDER BY id ASC LIMIT 5
                '''
        else:
            sql = '''
                SELECT * FROM viaje ORDER BY id ASC LIMIT '''+limit+''', 5
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get5Encargos(self,id):
        limit = str(5*(int(id)-1))
        if(id=='0'):
            sql = '''
                SELECT * FROM encargo
                '''
        elif(id=='1'):
            sql = '''
                SELECT * FROM encargo ORDER BY id ASC LIMIT 5
                '''
        else:
            sql = '''
                SELECT * FROM encargo ORDER BY id ASC LIMIT '''+limit+''', 5
                '''
        self.cursor.execute(sql)
        return self.cursor.fetchall()

        