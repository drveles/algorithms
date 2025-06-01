import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def generate_random_data_series(size: int = 1000) -> pd.Series:
    """
    Генерирует объект pandas.Series с заданным количеством случайных целых чисел
    в диапазоне от -10000 до 10000.
    :param size: Количество элементов в массиве (по умолчанию 1000)
    :return: Объект Series с целыми случайными числами
    """
    random_data = np.random.randint(-10000, 10001, size=size)
    return pd.Series(random_data)


def remove_noise(series: pd.Series) -> pd.Series:
    """
    Удаляет синтетический шум из переданных данных:
    - Удаляет значения None и NaN, считающиеся пропущенными;
    - Удаляет нулевые значения, считающиеся цифровым шумом.
    :param series: Входной объект pandas.Series, содержащий численные данные.
    :return: Очищенный Series без пропусков и нулей.
    """
    cleaned = series.dropna()
    cleaned = cleaned[cleaned != 0]
    return cleaned


def save_series_to_csv(series: pd.Series, filename: str = './series.csv') -> None:
    """
    Сохраняет объект Series в CSV-файл.
    :param series: Объект pandas.Series для сохранения
    :param filename: Имя файла для сохранения
    """
    series.to_csv(filename, index=False, header=False)


def load_series_from_csv(filename: str = "./series.csv") -> pd.Series:
    """
    Загружает числовой объект Series из CSV-файла.
    :param filename: Имя файла
    :return: Объект pandas.Series, считанный из файла
    """
    df = pd.read_csv(filename, header=None)
    return df.squeeze("columns")


def prepare_data(filename: str = './series.csv') -> pd.Series:
    """
    Генерирует или загружает объект pandas.Series:
    - Проверяет наличие файла 'series.csv'
    - Если файл существует, загружает данные из него
    - Если файла нет, создает новую серию, удаляет шумы и сохраняет в файл
    :return: Объект Series с числовыми данными
    """
    if os.path.exists(filename):
        series = load_series_from_csv(filename)
    else:
        series = generate_random_data_series()
        series = remove_noise(series)
        save_series_to_csv(series, filename)

    return series


def print_data_params(series: pd.Series) -> None:
    """
    Выводит параметры переданной серии данных:
    минимальное и максимальное значения, количество повторов, сумму и стандартное отклонение.
    :param series: Объект pandas.Series, содержащий числовые данные
    """
    print("Минимальное значение:", series.min())
    print("Количество повторов:", series.duplicated().sum())
    print("Максимальное значение:", series.max())
    print("Сумма значений:", series.sum())
    print("Стандартное отклонение:", series.std())


def main():
    series = prepare_data()
    print_data_params(series)


if __name__ == '__main__':
    main()
