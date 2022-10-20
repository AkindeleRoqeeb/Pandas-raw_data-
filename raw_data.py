import pandas as pd
raw_data = {
    'phone':['iphone', 'Samsung', 'Tecno', 'Nokia', 'itel', 'Trader money'],
    'price':[56, 76, 87, 39, 44, 70],
    'discount_price':[34, 21, 35, 24, 23, 56]
}
print(raw_data)

new_data = pd.DataFrame(raw_data, columns=['Product_name', 'Product_Amount', 'Product_help'])
print(new_data)

new_data['phone'] = new_data['price'] / new_data['discount_price']
print(new_data)

new_data.sort_values("phone", ascending=False)