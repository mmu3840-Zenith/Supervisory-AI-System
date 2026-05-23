import numpy as np

class FailureModel:
    def compute_risk(self, robots):
        avg = np.mean([r.energy for r in robots])
        low = sum(1 for r in robots if r.energy < 20)
        return min(100, (1-avg/100)*70 + low*10)
