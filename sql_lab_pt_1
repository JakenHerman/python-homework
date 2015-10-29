import sqlite3

createDb = sqlite3.connect(':memory:')
queryCurs = createDb.cursor()

def createTable():
    queryCurs.execute('''create table inventory
    (id int, name text, provider text, price float, quantity int)''')
    
    pass

def addProduct(product_id, name, provider, price, quantity):
    queryCurs.execute('''insert into inventory
    (id, name, provider, price, quantity) values (?, ?, ?, ?, ?)''',(product_id, name, provider, price, quantity))
    pass

def main():
    
    createTable()
    
    addProduct(3200, 'Milk', 'Borden', 3.59, 1200)
    addProduct(3201, 'Ice cream', 'Haagen Dazs', 5.29, 100)
    addProduct(5632, 'Lemon juice', 'Simply Orange', 3.49, 500)
    addProduct(23790, 'Energy drink', 'Monster Energy', 28.99, 700)
    addProduct(23791, 'Sprite', 'Coca Cola', 12.79, 2000)
    
    createDb.commit()

    #select all
    print('ALL ITEMS IN TABLE: \n')   
    queryCurs.execute('''select * from inventory''')
    for i in queryCurs:
        print('\n')
        for j in i:     
            print(j)
    print('\n END ALL ITEMS IN TABLE \n')

    #select items whose quantity is below 1000
    print('ITEMS WHOSE QUANTITY IS BELOW 1000: \n')
    queryCurs.execute('''select * from inventory where quantity < 1000''')    
    for i in queryCurs:
        print('\n')
        for j in i:     
            print(j)
    print('\n END ITEMS WHOSE QUANTITY IS BELOW 1000 \n')

    #select name, price, quantity
    print('NAME, PRICE, QUANTITY ITEMS: \n')
    queryCurs.execute('''select name, price, quantity from inventory''')    
    for i in queryCurs:
        print('\n')
        for j in i:     
            print(j)
    print('\n END NAME, PRICE, QUANTITY ITEMS \n')

    #display count of total number of items in table:
    queryCurs.execute('''select count(*) from inventory''')
    for i in queryCurs:
        print(i)
    
    pass

if __name__ == '__main__': main()
