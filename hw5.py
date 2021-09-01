import time
from multiprocessing import Pool


def factorize_one_n(number):
    result_for_one = []
    for item in range(1, number+1):
        if (number % item) == 0:
            result_for_one.append(item)
    return result_for_one


def factorize(*number):
    overall_result = []
    for elem in number:
        if type(elem) is int:
            overall_result.append(factorize_one_n(elem))
        else:
            raise NotImplementedError("Wrong number!")
    return overall_result


def pool_factorize(*number):
    with Pool(2) as pool:
        results = pool.map(factorize_one_n, number)
    return results


if __name__ == "__main__":
    start = time.time()
    '''закомментированная строка для выполнения синхронного кода'''
    #a, b, c, d = factorize(128, 255, 99999, 10651060)
    a, b, c, d = pool_factorize(128, 255, 99999, 10651060)
    end = time.time() - start
    print(f'This code ran {end} seconds')

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271,
                 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
                 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
