import numpy as np

def calculate(list):
    m = np.array(list)
    try:
        m.shape = (3, 3)
    except:
        raise ValueError("List must contain nine numbers.")
        
    calculations = dict()
    calculations["mean"] = [m.mean(0).tolist(), m.mean(1).tolist(), m.mean()]
    calculations["variance"] = [m.var(0).tolist(), m.var(1).tolist(), m.var()]
    calculations["standard deviation"] = [m.std(0).tolist(), m.std(1).tolist(), m.std()]
    calculations["max"] = [m.max(0).tolist(), m.max(1).tolist(), m.max()]
    calculations["min"] = [m.min(0).tolist(), m.min(1).tolist(), m.min()]
    calculations["sum"] = [m.sum(0).tolist(), m.sum(1).tolist(), m.sum()]

    return calculations
