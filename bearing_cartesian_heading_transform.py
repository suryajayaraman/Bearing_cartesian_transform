import numpy as np

def NormalizeAngle(angle):
    '''input angle [-pi, pi] mapped to [0, 2* pi]'''
    if angle < 0.0:
        return (angle + 2*np.pi)
    if angle > (2*np.pi):
        return (angle - 2*np.pi)
    else:
        return angle

def compass_to_cart(compass_orientation):
    '''
    #input  : compass heading in radians
    #output : cartesian heading in radians
    '''
    if compass_orientation == 0.0:
        compass_orientation = 2*np.pi
    t1 = NormalizeAngle(compass_orientation - (0.5*np.pi))
    cartesian_orientation = NormalizeAngle(2*np.pi - t1)    
    return cartesian_orientation

def cart_to_compass(cartesian_orientation):
    '''
    #input  : cartesian heading in radians
    #output : compass heading in radians
    '''
    if cartesian_orientation == 0.0:
        cartesian_orientation = 2*np.pi    
    t1 = NormalizeAngle(2*np.pi - cartesian_orientation)
    compass_orientation = NormalizeAngle(t1 + (0.5*np.pi))
    return compass_orientation

if __name__ == '__main__':

    #testing sample values
    test_cart_bearing = np.arange(0.0, 360.0, 90.0).tolist()
    result = [cart_to_compass(np.radians(x)) for x in test_cart_bearing]
    name_list = ['Cartesian_orientation', 'Compass_orientation']
    row_format ="{:>25}" * (len(name_list))
    print(row_format.format(*name_list))    
    for inp, out in zip(test_cart_bearing, result):
        print row_format.format(inp, np.degrees(out))

    print('     --------------------------------------------')
    
    test_compass_bearing = np.arange(0.0, 360.0, 90.0).tolist()
    result = [compass_to_cart(np.radians(x)) for x in test_compass_bearing]
    name_list = ['Compass_orientation', 'Cartesian_orientation']
    row_format ="{:>25}" * (len(name_list))
    print(row_format.format(*name_list))    
    for inp, out in zip(test_compass_bearing, result):
        print row_format.format(inp, np.degrees(out))
