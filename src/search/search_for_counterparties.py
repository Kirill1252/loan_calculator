from src.enums.all_conterparties import COUNTERPARTY


def search_counterparty(company):
    try:
        name_company = company.replace(' ', '').lower()
        search_company = {
            'name_crm': COUNTERPARTY[name_company]['name_crm'],
            'company': COUNTERPARTY[name_company]['company'],
            'requisites': COUNTERPARTY[name_company]['requisites']
        }

    except KeyError:
        search_company = {
            'name_crm': 'Контрагент не знайдено',
            'company': 'Контрагент не знайдено',
            'requisites': ''
        }
    return search_company
