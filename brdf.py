import numpy as np
import matplotlib.pyplot as plt
import  math


def ndf(x, nv, nl):
    nh = (nl + nv) / 2
    hv = nv - nh
    #calculate normal distribution value
    cos_val = np.maximum(np.cos(nh * math.pi / 180), 0)
    denom = (cos_val ** 2) * (x**2 - 1) + 1
    ndf = (x ** 2) / (math.pi * (denom**2))
    return ndf

def geometrySchlickGGX(x, nv, nl):
    # cal Geometry
    k = ((x + 1) ** 2) / 8
    cos_val = np.maximum(np.cos(nv * math.pi / 180), 0)
    G1 = cos_val / (cos_val * (1.0 - k) + k)
    cos_val = np.cos(nl * math.pi / 180)
    G2 = cos_val / (cos_val * (1.0 - k) + k)
    return G1*G2

def fresnel(x, nv, nl):
    nh = (nl + nv) / 2
    hv = nv - nh
    # calculation F value not related to the normal direction
    cos_val = np.maximum(np.cos(hv * math.pi / 180), 0)
    F0 = 0.8
    Fs = F0 + (1.0 - F0) * ((1 - cos_val) ** 5)
    return Fs

def brdf(x, nv, nl):
    return ndf(x, nv, nl)*geometrySchlickGGX(x, nv, nl)*fresnel(x, nv, nl)

def cos(x, nv, nl):
    nh = (nl + nv) / 2
    return np.cos(nh/180.0*math.pi)**(1.0/ x)

print(np.cos(math.pi/3))
func = [brdf, fresnel, geometrySchlickGGX, ndf, cos]

n_rows, n_cols = 1, len(func)
fig, axes = plt.subplots(n_rows, n_cols, figsize=(4 * n_cols, 3 * n_rows))


print(axes)
print(fig)
zip(func, axes.ravel())
theta = np.linspace(-90, 90, num= 100) #dot
X = np.linspace(0.2, 0.99,num= 5) #roughness
#print(theta)
#print(X)

for function, axe in zip(func, axes.ravel()):
    for x in X:
        y = function(x, theta,  0)
        axe.plot(theta, y, label = str(x))
        axe.set_title('function =%s' % function.__name__)
        axe.legend()

plt.show()