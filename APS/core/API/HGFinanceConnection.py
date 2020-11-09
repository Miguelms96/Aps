from hgfinance import HgFinanceConnection
import json

connectionFinance = HgFinanceConnection()
connectionFinance.set_key_api('02aa172a')

def write_json(lista):
    with open('HGFinanceJson.json', 'w') as J:
        json.dump(lista, J)

def load_json(arquivo):
    with open('HGFinanceJson.json', 'r') as J:
        return json.load(J)

def quotations(moeda):
    dtaBase = connectionFinance.quotations_only_requisition()
    write_json(dtaBase['results']['currencies'][moeda])
    jsonQuotations = load_json('HGFinanceJson.json')
    return jsonQuotations

def bovespa(empresaCode):
    dtaBase = connectionFinance.symbol_requisition(empresaCode)
    write_json(dtaBase['results'][empresaCode])
    jsonSymbol = load_json('HGFinanceJson.json')
    return jsonSymbol

def taxes():
    dtaBase = connectionFinance.taxes_only_requisition()
    write_json(dtaBase['results'])
    jsonTaxes = load_json('HGFinanceJson.json')
    return jsonTaxes
