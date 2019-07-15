import pandas as pd


def main():
    wb = pd.ExcelFile("excel_wb.xlsx")
    print(f"Workbook Sheets: {wb.sheet_names}")
    df = wb.parse(wb.sheet_names[0])
    df = df.set_index("UID")
    users_dict = df.to_dict("index")
    print(users_dict)


if __name__ == "__main__":
    main()
