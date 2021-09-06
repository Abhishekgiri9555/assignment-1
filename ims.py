# inventory system project

from datetime import datetime
import random
import sys

all_products = [
[1,"Chocos",20,500,"JAN 2022"],
[2,"Britania Cake",450,500,"OCT 2021"],
[3,"Parle G Biscuits",10,500,"FEB 2023"],
[4,"Oreo Biscuits",25,500,"FEB 2023"],
[5,"Bourbon Biscuits",18,500,"FEB 2023"],
[6,"Butter Bite",25,500,"FEB 2023"],
[7,"Munch",10,500,"MAR 2022"],
[8,"Dairy Milk",40,500,"MAR 2022"],
[9,"Kitkat",20,500,"MAR 2022"],
[10,"5 star",10,500,"MAR 2022"],
[11,"Aloo Bhujiya",38,500,"AUG 2022"],
[12,"Moong daal namkeen",40,500,"AUG 2022"],
[13,"Punjabi tadka",20,500,"AUG 2022"],
[14,"Mixture Namkeen",35,500,"AUG 2022"],
[15,"Khatta Meetha Namkeen",40,500,"AUG 2022"],
[16,"Dove Soap",50,500,"AUG 2023"],
[17,"Lux Soap",36,500,"AUG 2023"],
[18,"Dettol Soap",28,500,"AUG 2023"],
[19,"Cinthol Soap",45,500,"AUG 2023"],
[20,"Pears Soap",55,500,"AUG 2023"],
[21,"Eclairs toffee",70,500,"APR 2022"],
[22,"Kaccha aam toffee",65,500,"MAY 2022"],
[23,"Coffee Bite toffee",68,500,"JUN 2022"],
[24,"Pulse toffee",85,500,"FEB 2023"],
[25,"Kismi Toffee",46,500,"MAY 2024"],
[26,"Rin Detergent powder",60,500,"OCT 2025"],
[27,"Tide detergent powder",48,500,"DEC 2025"],
[28,"Surf exel detergent powder",50,500,"JUN 2025"],
[29,"Colgate Toothpaste",57,500,"NOV 2024"],
[30,"CloseUp Toothpaste", 66,500,"JAN 2024"],
[31,"Sensodyne Toothpaste",55,500,"MAY 2024"],
[32,"Maggi noodles",48,500,"FEB 2023"],
[33,"Top Ramon Noodles",45,500,"MAY 2023"],
[34,"Yippee Noodles",46,500,"JUL 2023"],
[35,"Kissan Ketchup",115,500,"DEC 2023"],
[36,"Tomato Sauce",65,500,"MAY 2023"],
[37,"Chili Sauce",65,500,"FEB 2024"],
[38,"Soya Sauce",65,500,"NOV 2023"],
[39,"Amul Ghee",450,500,"JAN 2026"],
[40,"Dawat Basmati Rice",193,500,"DEC 2028"],
[41,"Arhar Daal 1kg pkt",95,500,"FEB 2025"],
[42,"Ashirwad Aata 5kg pkt",120,500,"MAY 2024"],
[43,"Schezwan Chutney",119,500,"FEB 2022"],
[44,"Fogg Body Perfume",180,500,"OCT 2024"],
[45,"Park Avenue Deodorant",210,500,"SEP 2024"],
[46,"Almond Drop Hair Oil",132,500,"NOV 2025"],
[47,"Dettol Handwash",90,500,"FEB 2022"],
[48,"Kurkure Masala",20,500,"JUL 2022"],
[49,"Uncle Chips",20,500,"MAR 2022"],
[50,"Tea Marvel Gold 500mg",140,500,"NOV 2024"]



]


def banner():
    print("*************")
    print("\tGrofers Super Market")
    print("\t*************")
    print("\t1.Show All Products")
    print("\t2.Buy Product")
    print("\t3.Add Products")
    print("\t4.Exit")
    print("\t**************")


def display_all():
    print("Product_Id\tProdcut_Name\t\tPrice\tAvailable_Quantity\t\t\tExpiry_Date")
    for item in all_products:
        print("{0}\t{1}\t\t\t{2}\t\t\t\t{3}\t\t\t\t{4}".format(item[0], item[1], item[2], item[3],item[4]))


def order_summary(product, name):
    print("*****************")
    print("\t\tGrofers Super Market")
    print("*****************")
    print("Order Summary\tDate:{}".format(str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(item[1]))
    print("Use before: {}".format(item[4]))
    print("Price for single item: {}".format(item[-3]))
    print("*****************")


def generate_bill(product, name):
    print("*****************")
    print("\t\tGrofers Super Market")
    print("*****************")
    print("Bill:{} \tDate:{}".format(int(random.random() * 100000), str(datetime.now())))
    print("Customer Name: {}".format(name))
    print("Product Name: {}".format(item[1]))
    print("Price: {}".format(item[-3]))
    print("*****************")
    print("\t\tTotal Bill Amount: {}".format(item[-3]))


while (True):
    banner()
    choice = int(input(""))
    if choice == 1:
        display_all()
    elif choice == 2:
        display_all()
        prod_id = int(input("Enter the Product ID: "))
        prod_quant=int(input("Enter the quantity of product"))
        for item in all_products:
            if item[0] == prod_id:
                name = input("Customer Name: ")
                order_summary(item, name,)
                cnf = input("Confirm the Order(Y/N)")
                if cnf == 'Y':
                    print("-----------------------------")
                    print("Use the Product Before: ", item[4])
                    print("-----------------------------")
                    print()
                    print("Billing Amount: ",prod_quant*int(item[2]))
                    print()
                    print()
                    print()
                    print("!!!Thanks For shopping with Us!!!")
                    print()
                    print("Visit Again!!!")
                    print("-----------------------------")
                    sys.exit(0)
                else:
                    print("Continue Exploring the shop")
    elif choice == 3:
        username = input("Enter Admin UserID: ")
        password = input("Enter the Password: ")
        if username == "Admin" and password == "password":
            prod = []
            prod.append(len(all_products) + 1)
            prod.append(input("Enter the Product Name: "))
            prod.append(int(input("Available: ")))
            prod.append(int(input("Price: ")))
            all_products.append(prod)
        else:
            print("Incorrect username and password")
    else:
        print("GoodBye!!")
        break