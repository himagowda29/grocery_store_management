from sql_connection import get_sql_connection

def get_all_products(connection):

    cursor = connection .cursor()
    query = ("select products.product_id, products.name, products.uoim_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uoim_id=uom.uom_id")
    cursor.execute(query)
    response=[]
    for(product_id, name, uoim_id, price_per_unit,uom_name) in cursor:
        response.append(
        {
            'product_id' : product_id,
            'name' : name,
            'uoim_id' : uoim_id,
            'price_per_unit' : price_per_unit,
            'uom_name' : uom_name
        }
    )

    return response
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uoim_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uoim_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))
