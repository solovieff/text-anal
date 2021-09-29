import json
import os


def prepare_results(results_path='results/'):
    dicts = []
    for filename in os.listdir(results_path):
        with open(results_path + filename) as json_file:
            pure_name = filename.split(".")[0].split("_result")
            file_data = json.load(json_file)
            tuple_data = tuple(file_data)
            dist_result = dict(tuple_data)
            dist_result['meta'] = {}
            dist_result['meta']['name'] = pure_name
            print(dist_result)
            dicts.append(dist_result)
    return dicts


def compare_two_dicts(dict1, dict2):
    diff = set(dict1) - set(dict2)
    print('first has, second dont:')
    print(diff)
    diff = set(dict2) - set(dict1)
    print('second has, first dont:')
    print(diff)
    print('common words:')
    print(set(dict1.keys()).intersection(dict2.keys()))



def compare_results(name1, name2, results_path='results/'):
    print("checking " + name1 + " vs " + name2)
    with open(results_path + name1) as js_file1:
        with open(results_path + name2) as js_file2:
            file_data1 = json.load(js_file1)
            file_data2 = json.load(js_file2)

            tuple_data1 = tuple(file_data1)
            tuple_data2 = dict(file_data2)

            dist_result1 = dict(tuple_data1)
            dist_result2 = dict(tuple_data2)

            compare_two_dicts(dist_result1, dist_result2)


cname1 = 'po_faktam_result.json'
cname2 = 'soloviev_moskva_kreml_putin_result.json'
cname3 = 'soloviev_polniy_kontakt_result.json'
cname4 = 'rossiya_budushego_result.json'

compare_results(cname4, cname3)
