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
    dataframe = pd.read_csv(filename, header=None)
    return dataframe.squeeze("columns")


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


def visualize_series_data(series: pd.Series) -> None:
    """
    Визуализирует данные из объекта Series, создавая линейный график и гистограмму.
    Линейный график показывает распределение значений по индексу,
    а гистограмма отображает частотное распределение значений, округленных до сотен.
    :param series: Объект pandas.Series для визуализации
    """
    plt.plot(series, label='Series')
    plt.title('Линейный график данных Series')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.legend()
    plt.show()

    rounded_series = series.round(-2)
    plt.hist(rounded_series, bins=50, edgecolor='black')
    plt.title('Гистограмма данных Series (округлено до сотен)')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.show()


def create_dataframe(series: pd.Series) -> pd.DataFrame:
    """
    Создает DataFrame из объекта Series и добавляет два столбца:
    один с отсортированными значениями по возрастанию и другой по убыванию.
    :param series: Объект pandas.Series для преобразования
    :return: DataFrame с оригинальными и отсортированными данными
    """
    dataframe = pd.DataFrame({
        'Original': series,
        'Ascending': series.sort_values().values,
        'Descending': series.sort_values(ascending=False).values
    })
    return dataframe


def visualize_sorted_dataframes(dataframe: pd.DataFrame) -> None:
    """
    Визуализирует данные из DataFrame, создавая два линейных графика.
    Один график отображает значения, отсортированные по возрастанию,
    а другой по убыванию, для сравнения распределения данных.
    :param dataframe: DataFrame, содержащий отсортированные и оригинальные данные
    """
    plt.plot(dataframe['Ascending'], label='Ascending')
    plt.plot(dataframe['Descending'], label='Descending')
    plt.title('Линейные графики отсортированных данных')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.legend()
    plt.show()


def main():
    series = prepare_data()
    print_data_params(series)
    visualize_series_data(series)
    dataframe = create_dataframe(series)
    visualize_sorted_dataframes(dataframe)


if __name__ == '__main__':
    main()
