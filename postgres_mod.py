import psycopg2
import configparser
import datetime

settings = configparser.ConfigParser()
settings.read('./parser4511/config.ini')
start_page = settings['links']['start_page']
db1 = settings['postgres']['dbname']
us1 = settings['postgres']['user']
pw1 = settings['postgres']['password']
ht1 = settings['postgres']['host']
pt1 = settings['postgres']['port']

def execute(query, ans):
    connection = psycopg2.connect(dbname=db1, user=us1, password=pw1, host=ht1, port=pt1)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        if ans: 
            result = cursor.fetchall()
            #print(result)
        cursor.close()
        connection.close()
        if ans: return result
        else: return 'ok'
    except:
        cursor.close()
        connection.close()
        return 'err'
    

def create_tProduct():
    print('create tProduct')
    query = '''CREATE TABLE IF NOT EXISTS tProduct (
                                            id SERIAL PRIMARY KEY,
                                            name TEXT,
                                            link TEXT,
                                            brand INT,
                                            season INT,
                                            adddate DATE                                                 
                                            )'''
    x = execute(query, False)                                  
    return x
    
    
def create_tPrice():
    print('create tPrice')
    query = '''CREATE TABLE IF NOT EXISTS tPrice (
                                            id SERIAL PRIMARY KEY,
                                            product INT,
                                            price INT,
                                            parsing INT
                                            )'''
    x = execute(query, False)                                  
    return x


def create_tBrand():
    print('create tBrand')
    query = '''CREATE TABLE IF NOT EXISTS tBrand(
                                            id SERIAL PRIMARY KEY,
                                            name TEXT
                                            )'''
    x = execute(query, False)                                  
    return x


def create_tSeason():
    print('create tSeason')
    query = '''CREATE TABLE IF NOT EXISTS tSeason (
                                            id SERIAL PRIMARY KEY,
                                            name TEXT
                                            )'''
    x = execute(query, False)                                  
    return x


def create_tParsing():
    print('create tParsing')
    query = '''CREATE TABLE IF NOT EXISTS tParcing (
                                            id SERIAL PRIMARY KEY,
                                            date DATE,
                                            total INT,
                                            add INT,
                                            week INT,
                                            upprice INT
                                            )'''
    x = execute(query, False)                                  
    return x


def create_tLinks():
    print('create_tLinks')
    query = '''CREATE TABLE IF NOT EXISTS tLinks (
                                            id SERIAL PRIMARY KEY,
                                            link TEXT,
                                            product_count INT   
                                            )'''
    x = execute(query, False)
    return x


def create_tSize():
    print('create_tSize')
    query = '''CREATE TABLE IF NOT EXISTS tSize (
                                            id SERIAL PRIMARY KEY,
                                            width TEXT,
                                            profile TEXT,
                                            diameter TEXT
                                            )'''
    x = execute(query, False)                                            
    return x
    

def kill_all():
    print('kill all')
    query = '''DROP TABLE IF EXISTS tProduct, tPrice, tBrand, tSeason, tPrice, tParcing, tLinks, tSize'''
    x = execute(query,False)
    return x


def create_all():
    print(create_tProduct())
    print(create_tPrice())
    print(create_tBrand())
    print(create_tSeason())
    print(create_tParsing())
    print(create_tLinks())
    print(create_tSize())


def flow_size_table(width_list, profile_list, diameter_list):
    print('flow size table')
    for wd in width_list:
        for pf in profile_list:
            for dm in diameter_list:
                query = f'''INSERT INTO tSize (width, profile, diameter) VALUES ({wd}, {pf}, {dm})'''
                x = execute(query, False)
                print(f'{datetime.datetime.now()} {query}')


def raw_flow_links_table():
    print('flow links table')
    add1 = 'search/by-size/'    #/search/by-size/-7.5-70-14---------/
    add2 = '--------/'
    query = '''SELECT MAX (id) FROM tSize'''
    x = execute(query, True)
    counter = x[0][0] #в ответе - кортеж внутри списка типа [(123,)]
    for i in range(1,counter+1):
        query = f'''SELECT * FROM tSize WHERE id = {i}'''
        x = execute(query, True)
        #print(x) #0-id,1-wd,2-pr,3-dm
        link = f'{start_page}{add1}-{x[0][1]}-{x[0][2]}-{x[0][3]}-{add2}'
        print(f'{datetime.datetime.now()} {i} from {counter} : {link}')
        query = f'''INSERT INTO tLinks (link, product_count) VALUES ('{link}', 0)'''
        x = execute(query, False)
        

def check_links():
    pass