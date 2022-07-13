from bs4 import BeautifulSoup
import requests
from sqlalchemy import delete, insert, select
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


from alef_bot.settings import POSTGRES_DATABASE_URL
from alef_bot.tables import Locality

engine = create_engine(POSTGRES_DATABASE_URL)
session_local = sessionmaker(engine)

def start_operation():

    url = "https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D1%81%D0%BA%D0%B8%D0%B5_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D1%91%D0%BD%D0%BD%D1%8B%D0%B5_%D0%BF%D1%83%D0%BD%D0%BA%D1%82%D1%8B_%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9_%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D0%B8"

    res = requests.get(url)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.content, "html.parser")
                      
    locality = "\n".join(tag.get_text()
        for tag in soup.select('table[class="standard sortable"] tbody tr td a[title]')
    )
    
    link = "\n".join("https://ru.wikipedia.org" + tag.get('href')
        for tag in soup.select('table[class="standard sortable"] tbody tr td a[title]')
    )
    
    population_size = "\n".join(tag.get('data-sort-value')
        for tag in soup.select('table[class="standard sortable"] tbody tr td[data-sort-value]')
    )
    population_size = population_size.split('\n')
    locality = locality.split('\n')
    link = link.split('\n')
    
    sps_name = []
    sps_ref = []
    for i in range(len(locality)):
        if i % 2 == 0:
            sps_name.append(locality[i])
            sps_ref.append(link[i])

    sps_locality = []
    sps_link = []
    sps_population_size = []
    
    for i in range(len(sps_name)):
        # sps[i] = sps[i].split(' ')
        sps_locality.append(sps_name[i])
        sps_link.append(sps_ref[i])
        sps_population_size.append(population_size[i])
    
    # print(sps_locality)
    # print(sps_link)
    # print(sps_population_size)
    return (sps_locality, sps_link, sps_population_size)


def put_locality(xxx, yyy, zzz):
    with Session(engine)as session:
        session.begin()
        try:
            session.execute(delete(Locality))
            values =  [
            {
            'name': x, 
            'reference': y,
            'population_size': z,
            }
            for x, y, z in zip(xxx, yyy, zzz)
            ]
            session.execute(insert(Locality), values)
        except:
            session.rollback()
            raise
        session.commit()

# def put_locality(xxx, yyy, zzz):
#     with session_local.begin() as session:
#         session.delete(Locality)

def get_list_locality(mes):
    with Session(engine) as session:
        query = session.execute(select(Locality.name, Locality.reference, Locality.population_size).where(Locality.name.like (f'%{mes}%'))).fetchall()
    return query

start_operation()
