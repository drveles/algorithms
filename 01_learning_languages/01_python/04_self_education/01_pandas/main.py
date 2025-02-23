import pandas as pd

def main():
    data_frame = pd.read_csv("./data.csv")
    print(data_frame)

    filtered = data_frame[data_frame["age"] < 30]
    print(filtered)

    sorted = filtered.sort_values(by='income', ascending=False)
    print(sorted)

if __name__ == "__main__":
    main()
