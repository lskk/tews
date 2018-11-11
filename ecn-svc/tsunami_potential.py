import torch

novianty2018_model = torch.load('novianty2018.pt')

def predict(t0: float, td: float, mw: float):
    """
    Predict tsunami potential.

    :param t0: Unnormalized rupture duration variable
    :param td: Unnormalized P-wave dominant period variable
    :param mw: Unnormalized moment magnitude (M_w)
    """
    # Raw inputs
    in_bias: float = 1
    t0xtd: float = t0 * td

    # Normalization vectors
    ri_min = torch.tensor([0, 9.45, 2.7, 42.54644, 6.987921])
    ri_max = torch.tensor([1, 203.8708, 7.5, 877.4648, 8.995652])
    
    t0_norm = (t0 - ri_min[1]) / (ri_max[1] - ri_min[1])
    td_norm = (td - ri_min[2]) / (ri_max[2] - ri_min[2])
    t0xtd_norm = (t0xtd - ri_min[3]) / (ri_max[3] - ri_min[3])
    mw_norm = (mw - ri_min[4]) / (ri_max[4] - ri_min[4])
    x = torch.tensor([in_bias, t0_norm, td_norm, t0xtd_norm, mw_norm])

    y = novianty2018_model.forward(x)
    print('Tsunami potential output neurons: Yes=%s No=%s' % (float(y[0]), float(y[1])))
    print('Tsunami potential: Yes=%s No=%s' % (float(y[0]) >= 0.5, float(y[1]) >= 0.5))

    return {'tsunamiYes': float(y[0]), 'tsunamiNo': float(y[1])}
