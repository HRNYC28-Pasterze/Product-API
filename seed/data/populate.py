import os
import time
import pandas as pd
from sqlalchemy import create_engine

pwd = os.path.abspath(os.getcwd())

print('--- loading .csv files ---')
products = pd.read_csv(os.path.join(pwd, 'data/product.csv'))
features = pd.read_csv(os.path.join(pwd, 'data/features.csv'))
styles = pd.read_csv(os.path.join(pwd, 'data/styles.csv'))
skus = pd.read_csv(os.path.join(pwd, 'data/skus.csv'))
related = pd.read_csv(os.path.join(pwd, 'data/related.csv'))
photos = pd.read_csv(os.path.join(pwd, 'data/photos.csv'), error_bad_lines=False)

print('--- cleaning columns white space ---')
products.columns = products.columns.str.strip()
features.columns = features.columns.str.strip()
styles.columns = styles.columns.str.strip()
skus.columns = skus.columns.str.strip()
related.columns = related.columns.str.strip()
photos.columns = photos.columns.str.strip()

print('--- connecting to database ---')
engine = create_engine('postgresql://h01m3s@localhost:5432/db_test')


print('--- populating data to Postgres ---')
start_time = time.time()

local_time = time.time()
products.to_sql('products', engine)
print("--- %s seconds to populate products ---" % (time.time() - local_time))

local_time = time.time()
features.to_sql('features', engine)
print("--- %s seconds to populate features ---" % (time.time() - local_time))

local_time = time.time()
styles.to_sql('styles', engine)
print("--- %s seconds to populate styles ---" % (time.time() - local_time))

local_time = time.time()
skus.to_sql('skus', engine)
print("--- %s seconds to populate skus ---" % (time.time() - local_time))

local_time = time.time()
related.to_sql('related', engine)
print("--- %s seconds to populate related ---" % (time.time() - local_time))

local_time = time.time()
photos.to_sql('photos', engine)
print("--- %s seconds to populate photos ---" % (time.time() - local_time))

print("--- %s seconds in total ---" % (time.time() - start_time))



# --- cleaning columns white space ---
# --- connecting to database ---
# --- populating data to Postgres ---
# --- 98.59955596923828 seconds to populate products ---
# --- 184.61908507347107 seconds to populate features ---
# --- 427.861820936203 seconds to populate styles ---
# --- 2651.0119290351868 seconds to populate skus ---
# --- 351.1361041069031 seconds to populate related ---
# --- 1224.77778506279 seconds to populate photos ---
# --- 4938.007301807404 seconds in total ---