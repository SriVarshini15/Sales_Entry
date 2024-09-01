# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:13:18 2021

@author: Hemant Vijaykumar
Module: Maintain Sales
"""
import mysql_interface
import validate_input
def input_inp_no():
    while True:
        s="select ifnull(max(order_number),0)+1 from sales"
        status,err_msg,data=mysql_interface.execute_select(s)
        if status==True:
            return data[0][0]
        else: 
            print(err_msg)
            return -1
def input_order():
    while True:
        try:
            inp_date=int(input("Enter date purchased in YYYYMMDD format:"))
            break
        except:        
            print("Enter Valid Date.")
    while True:
        inp_id=validate_input.validate_integer("Enter Product ID:",True,"Enter Product ID>0",lower_limit=1)
        sel='''select product_name, quantity_in_stock, rate from product where product_id={}'''.format(inp_id)
        status, err_msg, data=mysql_interface.execute_select(sel)
        if status==True:
            if len(data)>0:
                print(data[0][0])
                break
            else:
                print("Product id does not exist.")
                continue
        else:
            print(err_msg)
            continue
    inp_quan=validate_input.validate_integer("Enter Quantity Purchased:",True,"Enter Quantity>0 and <="+ str(data[0][1]),lower_limit=1,upper_limit=data[0][1])
    inp_rate=data[0][2]
    inp_value=data[0][2]*inp_quan
    print("rate:",inp_rate)
    print("value:",inp_value)
    return inp_date,inp_id,inp_quan,inp_rate,inp_value
def display_all_orders():
    s="select order_number,date_purchased,product_id,quantity_purchased,rate,value from sales;"
    status, err_msg, data=mysql_interface.execute_select(s)
    if status==True:
        print(data)
    else :
        print(err_msg)
def search_for_orders():
    inp_no=validate_input.validate_integer("Enter Order Number:",True,"Enter Order Number>0",lower_limit=1)
    s='''select order_number,date_purchased,product_id,quantity_purchased,rate,value from sales
    where order_number = {};'''.format(inp_no)
    status, err_msg, data=mysql_interface.execute_select(s)
    if status==True:
        if len(data)>0:
            print(data)
        else:
            print("No order exists for order number =",inp_no)
    else:
        print(err_msg)
def insert_order():
    inp_no = input_inp_no()
    inp_date, inp_id, inp_quan, inp_rate, inp_value = input_order()
    if inp_no<0:
        return
    ins2 = '''insert into sales (order_number, date_purchased, product_id, quantity_purchased, rate, value) values ({}, {}, {}, {}, {}, {});'''.format(inp_no, inp_date,inp_id, inp_quan, inp_rate, inp_value)
    ins3 = '''update product set quantity_in_stock=quantity_in_stock - {} where product_id = {}'''.format(inp_quan,inp_id) 
    lst = [ins2]
    lst.append(ins3)
    status, error_msg = mysql_interface.execute_iud(lst)
    if status == False:
        print(error_msg)
    else:
        print("Order successfully placed.")
        print("Your order number:",inp_no)
def update_order():
    while True:
        inp_no=validate_input.validate_integer("Enter Order No:",True,"Enter Order No>0",lower_limit=1)
        s='''select order_number,date_purchased,product_id,quantity_purchased,rate,value from sales where order_number = {};'''.format(inp_no)
        status, err_msg, data=mysql_interface.execute_select(s)
        if status==True:
            if len(data)!=0:
                print("The old order is --→ ",data)
                break
            else:
                x=input("Order does not exist. Enter y to try again:")
                if x== 'y' or x== 'Y':
                    continue
                else:
                    return
        else:
            print(err_msg)
    print("Enter the new order --→ ")
    inp_date, inp_id, inp_quan, inp_rate, inp_value=input_order()
    upd = ''' update sales set date_purchased='{}', product_id={}, quantity_purchased={}, rate={}, value={} where order_number={};'''.format(inp_date, inp_id, inp_quan, inp_rate, inp_value, inp_no)
    upd1= '''update product set quantity_in_stock = quantity_in_stock + {} where product_id={}'''.format(data[0][3],data[0][2])
    upd2= '''update product set quantity_in_stock = quantity_in_stock - {} where product_id={}'''.format(inp_quan,inp_id)
    lt=[upd]
    lt.append(upd1)
    lt.append(upd2)
    status, error_msg = mysql_interface.execute_iud(lt)
    if status == False:
        print(error_msg)
    else:
        print("Order successfully updated.")
def delete_order():
    while True:
        global data
        inp_no=validate_input.validate_integer("Enter Order No:",True,"Enter Order No>0",lower_limit=1)
        s='''select order_number,date_purchased,product_id,quantity_purchased,rate,value from sales where order_number = {};'''.format(inp_no)
        status, err_msg, data=mysql_interface.execute_select(s)
        if status==True:
            if len(data)!=0:
                print("The order is --→ ",data)
                break
            else:
                x=input("Order does not exist. Enter y to try again:")
                if x== 'y' or x== 'Y':
                    continue
                else:
                    return
        else:
            print(err_msg)
    delt=''' delete from sales where order_number={};'''.format(inp_no)
    updt='''update product set quantity_in_stock = quantity_in_stock + {} where product_id={}'''.format(data[0][3],data[0][2])
    lit=[delt]
    lit.append(updt)
    status, error_msg = mysql_interface.execute_iud(lit)
    if status == False:
        print(error_msg)
    else:
        print("Order sucessfully removed.")