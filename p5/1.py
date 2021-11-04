from re import T

products=[]

def show_menu():
    print('welcome to store')
    print('1-add')
    print('2-edit')
    print('3-delete')
    print('4-show list')
    print('5-search')
    print('6-buy')
    print('7-exit')

def load_data_from_database():
    print('loading...')
    f=open('/home/sara-gh/Desktop/python/data.csv','r')
    text=f.read()
    
    rows=text.split('\n')
    
    for row in rows:
        info=row.split(',')
        new_dict={'id':info[0],'name':info[1],'price':info[2],'count':info[3]}
        products.append(new_dict)
    print('load complete.')
    
def add():
    record_str = input("Insert a record(id, #name, price, count): ")
    record_str_split =  record_str.split(',')
    products.append({'id':record_str_split[0],'name':record_str_split[1],'price':record_str_split[2],'count':record_str_split[3]})
    
def edit():
    s = input('please insert recoed id that you want to edit: ')
    for i in range(len(products)):
        if products[i]['id']==s:
            s = input("please insert recoed in this format : 'id','name','price','count' :\n")
            s = s.split(',')
            newLine={'id':s[0],'name':s[1],'price':s[2],'count':s[3]}
            products.append(newLine)
            return
            
    print("not found")
    return

def delete():
    name = input('please insert recoed id that you want to delete: ')#id
    for product in products:
        if name == product['name']:
            products.remove(product)
            print('deleted.\n')
            return
            
    print("not found")
    
def show_list():
    for product in products:
        print(product)
    
def search():
    name = input('please insert recoed id: ')
    for product in products:
        if name == product['id']:
            print (product)
            return True

    print("not found")
    return False    

def buy():

    name = input('please insert recoed id that you want to buy: ')
    for product in products:
        if name == product['id']:
            print(product)
            old = int(product['count'])
            how = int(input("How much: "))
            new = old - how
            if(new<0):
                print('The desired number is more than the inventory!!!\n')
            else:
                product['count'] = str(new)
                print('The purchase was made\n')
            return

    print("not found")

def savaFile():
    f=open('/home/sara-gh/Desktop/python/data.csv','w')
    for x in products:
        f.write('%s,%s,%s,%s\n' %(x['id'], x['name'], str(x['price']), str(x['count']))) 

load_data_from_database()
while(True):
    show_menu()
    choice=int(input('please choose from menu: '))
    if  choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        delete()
    elif choice==4:
        show_list()  
    elif choice==5:
        search()
    elif choice==6:
        buy()  
    elif choice==7:
        savaFile()
        exit()
