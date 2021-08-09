import numpy as np

def remove_outlier(data):   # data = list of values
    for iterable in data:
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lim_inf = q1-(iqr * 1.5)
        lim_sup = q3+(iqr * 1.5)
        if iterable < lim_inf or iterable > lim_sup:
            data.remove(iterable)
        else:
            pass
