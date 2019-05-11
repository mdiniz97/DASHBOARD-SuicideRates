import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# print(os.listdir("../dataset"))

data = pd.read_csv('../dataset/master.csv')
data.columns = ['country', 'year', 'sex', 'age', 'suicides_no', 'population',
               'suicidesper100kpop', 'country-year', 'HDI for year',
               'gdp_for_year_dollars', 'gdp_per_capita_dollars', 'generation']

data_json = json.loads(data.to_json(orient='records'))


# FILTRO:
#   PAÍS
#   ANO


def get_countries():
    '''
    lista de países
    '''
    return sorted(set(data.country.tolist()))

def get_year():
    '''
    lista de anos
    '''
    return sorted(set(data.year.tolist()))

def get_ages():
    '''
    filtro para faixa de idades
    '''
    return data.age.tolist()

def get_gdp_for_year_dollars(year, country):
    qnt = 0
    for el in data_json:
        if el['year'] == year and el['country'] == country:
            qnt += el['gdp_for_year_dollars']
    return qnt
def get_gdp_per_capita_dollars(year, country):
    qnt = 0
    for el in data_json:
        if el['year'] == year and el['country'] == country:
            qnt += el['gdp_per_capita_dollars']
    return qnt
def get_generation(year, country):
    qnt = 0
    for el in data_json:
        if el['year'] == year and el['country'] == country:
            qnt += el['generation']
    return qnt

def get_suicidesper100kpop(year, country):
    qnt = 0
    for el in data_json:
        if el['year'] == year and el['country'] == country:
            qnt += el['suicidesper100kpop']
    return qnt

def get_population(year, country):
    qnt = 0
    for el in data_json:
        if el['year'] == year and el['country'] == country:
            qnt += el['population']
    return qnt

def get_suicides_no(year, country, sex=None):
    qnt = 0
    if sex == None:
        for el in data_json:
            if el['year'] == year and el['country'] == country:
                qnt += el['suicides_no']
    elif sex == 'male':
        for el in data_json:
            if el['year'] == year and el['country'] == country and el['sex']== 'male':
                qnt += el['suicides_no']
    elif sex == 'female':
        for el in data_json:
            if el['year'] == year and el['country'] == country and el['sex']== 'female':
                qnt += el['suicides_no']
    return qnt
# def get_suicides_no_by_sex(year, country, sex):
#     qnt = 0
#     for el in data_json:
#         if el['year'] == year and el['country'] == country:
#             qnt += el['sex']
#     return qnt



