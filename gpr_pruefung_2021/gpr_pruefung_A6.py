def collect_sales_data(file_name, customer_no):
    with open(file_name) as f:
        data = [x.strip().split() for x in f]
        menge = 0
        for y in data:
            if customer_no == y[2]:
                menge += y[5]
    return menge
print(collect_sales_data("gpr_pruefung_A6_datei", 12345))


with open("gpr_pruefung_A5_datei") as f:
    x = [x.strip() for x in f]
    print(x)