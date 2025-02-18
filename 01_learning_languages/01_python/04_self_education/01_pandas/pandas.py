import pandas as pd 

def main():
    data = pd.read_csv("./pandas.csv")

    print(data)

    filtered = data.filter()


if __name__ == "__main__":
    main()