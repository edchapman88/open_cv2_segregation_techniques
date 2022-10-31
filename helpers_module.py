import numpy as np
import matplotlib.path as plt_path
import cv2

def oval_mask(X:int, Y:int, XRad:int, YRad:int, img_RGB:np.ndarray):
    img_gray = cv2.cvtColor(img_RGB,cv2.COLOR_RGB2GRAY)
    # img_gray = cv2.cvtColor(img_BGR,cv2.COLOR_BGR2GRAY)

    s = np.linspace(0, 2*np.pi, 400)
    c = X + XRad*np.cos(s)
    r = Y + YRad*np.sin(s)
    points = np.array([r, c]).T 

    oval_path = plt_path.Path(points)

    coords = np.zeros((img_gray.size,2))
    for j in range(img_gray.shape[1]):
        for i in range(img_gray.shape[0]):
            coords[i+j*img_gray.shape[0]][0] = i
            coords[i+j*img_gray.shape[0]][1] = j

    bool_array = oval_path.contains_points(coords)
    masked = np.copy(img_RGB)
    for j in range(masked.shape[1]):
        for i in range(masked.shape[0]):
            if bool_array[i+j*masked.shape[0]] ==  False:
                masked[i,j,:] = 0
    
    return masked
