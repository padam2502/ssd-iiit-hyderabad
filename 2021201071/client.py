import requests
import json
import random


def pattern_1():
    """[for printing the pattern1]
    """
    print(" **** \n*    *\n*    *\n*    *\n*    *\n **** \n")


def pattern_2():
    """[for printing the pattern2]
    """
    print(" ****            **** \n|    |          |    |\n|    |          |" +
          "    |\n|    |          |    |\n ****            **** \n")
    print("          {}")
    print("    ______________\n")


def printing_bill(total, tip, disc, final_total_2, split_bill):
    """[for printing the final updated bill]
    """
    print(f"Total: {total:.2f}")
    print(f"Tip precentage : {tip:.2f}")
    print(f"Discount/Increase : {disc:.2f}")
    print(f"Final Total : {final_total_2:.2f}")
    print(f"Updated share of each person: {final_total_2/split_bill:.2f}")


def place_order(menu_item):
    """[function for placing orders]

    Args:
        menu_item ([dictionary]): [menu details]

    Returns:
        [dictionary]: [details of transactions]
    """
    print('\n\nEnter your order\n')
    print('**********************************************\n')
    id_list = {}
    h_list = {}
    f_list = {}
    half_count = {}
    full_count = {}
    counts = int(input("Enter number of order you want to place: "))
    for i in range(counts):
        print('Enter details for order number ', i+1)
        ID = int(input("Enter item ID: "))
        id_list[ID]=0
        hf = input("Enter half/full: ")
        if hf == "half":
            h_list[ID] = "half"
        else:
            f_list[ID] = "full"
        q = int(input("Enter quantity: "))
        if hf == "half":
            if ID in half_count.keys():
                half_count[ID] += q
            else:
                half_count[ID] = q
        else:
            if ID in full_count.keys():
                full_count[ID] += q
            else:
                full_count[ID] = q

    tip = int(input("Enter tip %:\n0\n10\n20\n"))
    print('\n')
    total = 0
    full_list = {}
    half_list = {}
    for key, val in menu_item.items():
        half_list[int(key)] = val["half_plate"]
        full_list[int(key)] = val["full_plate"]

    for i in id_list.keys():
        if i in half_count.keys():
            total += half_list[i]*half_count[i]
        if i in full_count.keys():
            total += full_list[i]*full_count[i]
    tip_total = total+tip*total/100
    split_bill = int(input("Enter number of people want to split bill: "))
    print("Total amount")
    print(f"{tip_total:.2f}")
    print('\n')
    print("share of each person")
    share = tip_total/split_bill
    print(f"{share:.2f}")
    print('\n')
    print("There’s a 5 percent chance to get a 50 percent discount off the " +
          "total bill\n10 percent chance to get 25 percent discount\n" +
          "15 percent chance to get 10 percent discount\n" +
          "20 percent chance to get no discount\n" +
          "50 percent chance that the total amount increases by 20 percent")
    choice = input(
        "Whether you want to partiipate in test your luck event\nYes\nNo\n")
    arr = []
    y = 0
    final_total_1 = total+total*tip/100
    final_total_2 = final_total_1*((100+y)/100)
    disc = final_total_1*(y/100)
    # Any number generation probability corresponds to its interval
    # size because of the count of integers in range of interval
    if(choice == "Yes"):
        y = random.randint(1, 100)
        if y <= 5:
            y = 50
        elif y <= 15:
            y = 25
        elif y <= 30:
            y = 10
        elif y <= 50:
            y = 0
        elif y <= 100:
            y = -20
        if y != 0:
            y = -y
        final_total_1 = total+total*tip/100
        final_total_2 = final_total_1*((100+y)/100)
        disc = final_total_1*(y/100)
        print(f"Discount value : {disc:.2f}")
        if y >= 0:
            pattern_1()
        else:
            pattern_2()
    print('\n-----------BILL-----------\n')
    s_bill = ""
    s_temp = ""
    for i in id_list.keys():
        if i in half_count.keys():
            val = half_list[i]
            s_temp = "\nItem {0} [Half] [{1}]: {2:.2f}".format(
                i, half_count[i], half_count[i]*val)
            s_bill += s_temp
            print(s_temp)
        if i in full_count.keys():
            val = full_list[i]
            s_temp = "\nItem {0} [Full] [{1}]: {2:.2f}".format(
                i, full_count[i], full_count[i]*val)
            s_bill += s_temp
            print(s_temp)
    print(f"Total: {total:.2f}")
    print(f"Tip precentage : {tip:.2f}")
    print(f"Discount/Increase : {disc:.2f}")
    print(f"Final Total : {final_total_2:.2f}")
    print(f"Updated share of each person: {final_total_2/split_bill:.2f}")
    s_bill += "\nTotal : {0:.2f}".format(
        total)
    s_bill += "\nTip precentage : {0:.2f}".format(
        tip)
    s_bill += "\nDiscount/Increase : {0:.2f}".format(
        disc)
    s_bill += "\nFinal Total : {0:.2f}".format(
        final_total_2)
    s_bill += "\nUpdated share of each person: {0:.2f}".format(
        final_total_2/split_bill)
    data = {"transaction": "{0:.2f}".format(final_total_2),
            "bill": s_bill}

    return data


def view_transactions(transaction_detail):
    """[function for viewing transactions]

    Args:
        transaction_detail ([dictionary]): [transactions details]
    """
    details = transaction_detail["response"]
    while True:
        for ele in range(len(details)):
            print(str(ele) + ": Transaction of Total " +
                  str(details[ele]["transaction"]))
        print(str(len(details)) + ": Exit")
        choice = int(input())
        if choice == len(details):
            return
        elif 0 <= choice < len(details):
            bill = details[choice]["bill"]
            print("\n=====================================")
            print(bill)
            print("=====================================\n")
        else:
            print("Invalid Input")


if __name__ == "__main__":
    """[an interactive python code that accepts input and displays
    output via command line]
    """
    curr_session = requests.Session()
    check_loggedin = False
    while 1:
        print("0: For Exit")
        if check_loggedin is False:
            print("1: For Login:")
        print("2: for Signup")
        if(check_loggedin is True):
            print("3: for Reading Menu")
            print("4: for Placing Order")
            print("5: for View previous bill statements")
            print("6: for Editing Menu (only for chef)")
            print("7: for Logout")

        x = int(input())
        if x == 1:
            uname = input("Enter Username: ")
            passwd = input("Enter Password: ")
            msg = {'username': uname, 'password': passwd}
            recvd = curr_session.post(
                "http://localhost:8000/do_signin", json=msg).text
            if recvd == "LOGGED in successfully":
                check_loggedin = True
            print(recvd)
        elif x == 2:
            uname = input("Enter Username: ")
            passwd = input("Enter Password: ")
            msg = {'username': uname, 'password': passwd}
            recvd = curr_session.post(
                "http://localhost:8000/do_signup", json=msg).text
            print(recvd)

        elif x == 3:
            if check_loggedin is True:
                recvd = curr_session.get("http://localhost:8000/menu").json()
                print('*****************MENU*****************\n')
                print("\nItem Id       Half Plate \t    Full Plate")

                for key, val in recvd.items():
                    print(str(key) + "      \t\t" + str(val["half_plate"]) +
                          "      \t\t" + str(val["full_plate"]))
            else:
                print("User is not currently logged In")
        elif x == 4:
            if check_loggedin is True:
                menu_list = curr_session.get(
                    "http://localhost:8000/menu").json()
                data = place_order(menu_list)
                recvd = curr_session.post(
                    "http://localhost:8000/order", json=data).text
                print(recvd)
            else:
                print("User is not currently logged In")
        elif x == 5:
            if check_loggedin is True:
                recvd = curr_session.get("http://localhost:8000/order").json()
                if len(recvd["response"]) == 0:
                    print("No transactions for this user")
                else:
                    view_transactions(recvd)

            else:
                print("User is not currently logged In")
        elif x == 6:
            if check_loggedin is True:
                recvd = curr_session.get("http://localhost:8000/is-chef").text
                if recvd == "Yes":
                    item_id = input("Enter Item Id: ")
                    half_plate = input("Enter half plate price: ")
                    full_plate = input("Enter full plate price: ")
                    data = {"id": item_id, "half_plate": half_plate,
                            "full_plate": full_plate}
                    ret_val = curr_session.post(
                        "http://localhost:8000/menu", json=data).text
                    print(ret_val)
                else:
                    print("User is not a chef")
        elif x == 7:
            if check_loggedin is True:
                recvd = curr_session.get("http://localhost:8000/signout").text
                check_loggedin = False
                print(recvd)
            else:
                print("User is not currently logged In")

        elif x == 0:
            break
        else:
            print("Invalid input")
