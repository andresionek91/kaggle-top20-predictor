import requests
import json

def treat_input(input_json):
    treated = dict()
    for key, value in input_json.items():
        if key[0] == 'Q':
            treated[value] = 1
        else:
            treated[key] = 1
    return treated


input_json = {
    "Q1": "q1_other",
    "Q2": "q2_25_29",
    "Q3": "q3_united_",
    "Q4": "q4_other",
    "Q6": "q6_data_sc",
    "Q7": "q7_other2",
    "Q8": "q8_2_3",
    "Q10": "q10_we_rec",
    "q11_analyz": "on",
    "q11_run_a_": "on",
    "q11_build_": "on",
    "q15_amazon": "on",
    "other": "on",
    "q16_python": "on",
    "q16_sql": "on",
    "Q23": "q23_25_to_",
    "q31_catego": "on",
    "q31_geospa": "on",
    "q31_numeri": "on",
    "q31_tabula": "on",
    "q31_text_d": "on",
    "q31_time_s": "on",
    "q42_revenu": "on"
}

treated_input_json = treat_input(input_json)
header = {'Content-Type': 'application/x-www-form-urlencoded'}

url = 'https://tk9k0fkvyj.execute-api.us-east-2.amazonaws.com/default/top20-predictor'

requests.post(url, params=treated_input_json, headers=header).json()
