import json
from itertools import chain
import pandas as pd

def convertCSV(json_path):
    with open(str(json_path)) as file:
        data = json.load(file)

        total_index = [z for z in range(0,len(data))]

        # CSV_1
        nested_user_txs = []
        nested_user_id = []
        
        for i in data:
            user_txs = [x['id'] for x in i['txs']]
            user_id = [ user_txs[0] for i in range(len(user_txs))]
            nested_user_txs.append(user_txs)
            nested_user_id.append(user_id) 
        
        df_1 = pd.DataFrame(list(zip(list(chain(*nested_user_id)),list(chain(*nested_user_txs)))), columns = ['user_id','tx_id'])
        df_1.to_csv(r'/Users/macbookpro/Documents/pintu_test/csv_1', index = False)

        # CSV_2
        user = [data[num_id]['user'] for num_id in total_index]

        df_2 = pd.DataFrame(user)
        df_2.sort_values(by=['id'], inplace=True)
        df_2.to_csv(r'/Users/macbookpro/Documents/pintu_test/csv_2', index = False)


        # CSV 3
        tampungan = []
        for num_id in total_index:
            tampungan.append(data[num_id]['txs'])


        df_3 = pd.DataFrame(list(chain(*tampungan)))
        df_3.sort_values(by=['id'], inplace=True)
        df_3.to_csv(r'/Users/macbookpro/Documents/pintu_test/csv_3', index = False)
