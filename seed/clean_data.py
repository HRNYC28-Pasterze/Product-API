import os
import time
import pandas as pd

pwd = os.path.dirname(os.path.abspath(__file__))

start_time = time.time()

local_time = time.time()
products = pd.read_csv(os.path.join(pwd, 'data/product.csv'))
products.columns = products.columns.str.strip()
products['default_price'] = products['default_price'].apply(lambda x: x.replace('default_price:', '').strip() if isinstance(x, str) else x).astype(int)
products.to_csv(os.path.join(pwd, 'data/fixed_product.csv'), index=False)
print("--- %s seconds to clean products ---" % (time.time() - local_time))

local_time = time.time()
features = pd.read_csv(os.path.join(pwd, 'data/features.csv'))
features.columns = ['id', 'product_id', 'feature', 'value']
features.id = features.id - 1
features.value = features.value.apply(lambda x: 'null' if isinstance(x, float) else x).astype(str)
features.to_csv(os.path.join(pwd, 'data/fixed_features.csv'), index=False)
print("--- %s seconds to clean features ---" % (time.time() - local_time))

local_time = time.time()
styles = pd.read_csv(os.path.join(pwd, 'data/styles.csv'))
styles.sale_price = styles.sale_price.apply(lambda x: str(x).replace('nan', '0')).astype(float)
styles.to_csv(os.path.join(pwd, 'data/fixed_styles.csv'), index=False)
print("--- %s seconds to clean styles ---" % (time.time() - local_time))

local_time = time.time()
skus = pd.read_csv(os.path.join(pwd, 'data/skus.csv'))
skus.columns = skus.columns.str.strip()
skus.to_csv(os.path.join(pwd, 'data/fixed_skus.csv'), index=False)
print("--- %s seconds to clean skus ---" % (time.time() - local_time))

local_time = time.time()
photos = pd.read_csv(os.path.join(pwd, 'data/photos.csv'), sep='[,|\n]', error_bad_lines=False, engine='python').drop_duplicates(['id'], keep='first')
photos.columns = photos.columns.str.strip()
photos.to_csv(os.path.join(pwd, 'data/fixed_photos.csv'), index=False)
print("--- %s seconds to clean photos ---" % (time.time() - local_time))

print("--- %s seconds in total ---" % (time.time() - start_time))


# --- 10.09410572052002 seconds to clean products ---
# --- 5.389069080352783 seconds to clean features ---
# --- 14.943940162658691 seconds to clean styles ---
# --- 41.16258692741394 seconds to clean skus ---
# --- 237.38831186294556 seconds to clean photos ---
# --- 308.9781141281128 seconds in total ---