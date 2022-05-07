# for reading csv
import csv
# for calculating random integer
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


if __name__ == "__main__":
    """[an interactive python code that accepts input and displays
    output via command line]
    """
    file_name = "Menu.csv"
    fields = []
    rows = []
    half_count = []
    full_count = []
    print('*****************MENU*****************\n')

    # reading csv file

    with open(file_name, 'r') as csv_file:
        # creating a csv reader object
        csv_reader = csv.reader(csv_file)

        # extracting field names through first row
        fields = next(csv_reader)

        # extracting each data row one by one
        for row in csv_reader:
            row = str(row)
            new_str = ''.join([row[i] for i in range(
                len(row)) if i not in [0, len(row)-1]])
            rows.append(new_str)

    # Menu heading
    print('      '.join(field for field in fields))

    item_half = {}
    item_full = {}
    cn = 0
    hn = 1
    fn = 1
    o = 0
    str = ""

    # displaying the Menu
    for row in rows:
        print('\n')
        str = ""
        cn = 0
        half_count.append(0)
        full_count.append(0)
        for ch in range(len(row)):
            if row[ch] == ',':
                print('\t\t', end="")
                if(cn == 4):
                    item_half[hn] = int(str)
                    hn = hn+1
                    str = ""

            elif row[ch] != '\'':
                print(row[ch], end="")
                if row[ch] != ' ':
                    str = str+row[ch]
            if row[ch] == '\'':
                cn = cn+1
                if cn == 2:
                    str = ""
            if cn == 6:
                item_full[fn] = int(str)
                fn = fn+1

    print('\n\nEnter your order\n')
    print('**********************************************\n')
    id_list = []
    hf_list = []
    q_list = []

    counts = int(input("Enter number of order you want to place: "))
    for i in range(counts):
        print('Enter details for order number ', i+1)
        ID = int(input("Enter item ID: "))
        id_list.append(ID)
        hf = input("Enter half/full: ")
        hf_list.append(hf)
        q = int(input("Enter quantity: "))
        if hf == "half":
            half_count[ID-1] += q
        else:
            full_count[ID-1] += q
        q_list.append(q)
    tip = int(input("Enter tip %:\n0\n10\n20\n"))
    print('\n')
    total = 0
    full_list = list(item_full)
    half_list = list(item_half)
    price_list = []
    for i in range(counts):
        if(hf_list[i] == "half"):
            val = list(item_half.values())[id_list[i]-1]
            price_list.append(val)
            total += val*q_list[i]
        else:
            val = list(item_full.values())[id_list[i]-1]
            price_list.append(val)
            total += val*q_list[i]
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
    x = 0
    final_total_1 = total+total*tip/100
    final_total_2 = final_total_1*((100+x)/100)
    disc = final_total_1*(x/100)
    # Any number generation probability corresponds to its interval
    # size because of the count of integers in range of interval
    if(choice == "Yes"):
        x = random.randint(1, 100)
        if x <= 5:
            x = 50
        elif x <= 15:
            x = 25
        elif x <= 30:
            x = 10
        elif x <= 50:
            x = 0
        elif i <= 100:
            x = -20
        if x != 0:
            x = -x
        final_total_1 = total+total*tip/100
        final_total_2 = final_total_1*((100+x)/100)
        disc = final_total_1*(x/100)
        print(f"Discount value : {disc:.2f}")
        if x >= 0:
            pattern_1()
        else:
            pattern_2()

    print('\n-----------BILL-----------\n')
    for i in range(len(half_count)):
        if half_count[i] != 0:
            val = list(item_half.values())[i]
            print("Item ", i+1, ' [Half] ', '[', half_count[i],
                  ']', ': ', f"{half_count[i]*val:.2f}", sep='')
        if full_count[i] != 0:
            val = list(item_full.values())[i]
            print("Item ", i+1, ' [Full] ', '[', full_count[i],
                  ']', ': ', f"{full_count[i]*val:.2f}", sep='')
    printing_bill(total, tip, disc, final_total_2, split_bill)
