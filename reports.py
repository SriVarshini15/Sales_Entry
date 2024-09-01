import mysql_interface
def a_():
    date1=input("Enter start date in YYYYMMDD format:")
    date2=input("Enter end date in YYYYMMDD format:")
    s='''select date_purchased, product_name, a.product_id, order_number, quantity_purchased, b.rate, value from sales a, product b where a.product_id = b.product_id and date_purchased >={} and date_purchased<={} order by date_purchased, product_name;'''.format(date1,date2)
    status, err_msg,data = mysql_interface.execute_select(s)
    if status==True:
        print(data)
    else :
        print(err_msg)
def b_():
    date1=input("Enter start date in YYYYMMDD format:")
    date2=input("Enter end date in YYYYMMDD format:")
    s='''select category_name, date_purchased, product_name, a.product_id, order_number, quantity_purchased, b.rate, value from sales a, product b, category c where a.product_id = b.product_id and b.category_id = c.category_id and date_purchased >={} and date_purchased<={} order by category_name, date_purchased, product_name;'''.format(date1,date2)
    status, err_msg,data = mysql_interface.execute_select(s)
    if status==True:
        print(data)
def c_():
    date1=input("Enter start date in YYYYMMDD format:")
    date2=input("Enter end date in YYYYMMDD format:")
    s='''select DATE_FORMAT(date_purchased,'%Y%m'), product_name, sum(value) from sales a, product b, category c where a.product_id = b.product_id and b.category_id = c.category_id and date_purchased >= {} and date_purchased <= {} group by DATE_FORMAT(now(),'%Y%m'), product_name order by DATE_FORMAT(now(),'%Y%m'), product_name;'''.format(date1,date2)
    status, err_msg,data = mysql_interface.execute_select(s)
    if status==True:
        print(data)
def d_():
    date1=input("Enter start date in YYYYMMDD format:")
    date2=input("Enter end date in YYYYMMDD format:")
    s='''select DATE_FORMAT(date_purchased,'%Y%m'), category_name, product_name, sum(value) from sales a, product b, category c where a.product_id = b.product_id and b.category_id = c.category_id and date_purchased >={} and date_purchased <={} group by DATE_FORMAT(now(),'%Y%m'), category_name, product_name order by DATE_FORMAT(now(),'%Y%m'), category_name, product_name;'''.format(date1,date2)
    status, err_msg,data = mysql_interface.execute_select(s)
    if status==True:
        print(data)