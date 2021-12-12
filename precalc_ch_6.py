
from math import pi, sin, cos, tan

def brute_force_solve(
            alpha: float,
            beta: float, 
            omega: float, 
            chi: float,
            function: str) -> list:
    '''
    :params:
    :alpha: amplitude of function
    :beta: midline of function
    :omgega: x-coeficient
    :chi: phase shift coeficient
    '''
    print('Generating Points For: ')
    print(f'f(x) = {alpha}{ function}({omega}x - {chi}) + {beta}')
    if function == 'sin':
        period = 2*pi / omega
        x_axis = [0, period/4, period/2, 3*period/4, period]
        y_axis = []
        for point in x_axis:
            y_value = alpha*sin(omega*point - chi) + beta
            y_axis.append(round(y_value))
        points = (
            (str(x_axis[0]/pi)+ ' pi', y_axis[0]),
            (str(x_axis[1]/pi)+ ' pi', y_axis[1]),
            (str(x_axis[2]/pi)+ ' pi', y_axis[2]),
            (str(x_axis[3]/pi)+ ' pi', y_axis[3]),
            (str(x_axis[4]/pi)+ ' pi', y_axis[4]),
        )
        for point in points:
            print(point)
        return points
    
    if function == 'cos':
        period = 2*pi / omega
        x_axis = [0, period/4, period/2, 3*period/4, period]
        y_axis = []
        for point in x_axis:
            y_value = alpha*cos(omega*point - chi) + beta
            y_axis.append(round(y_value))
        points = (
            (str(x_axis[0]/pi)+ ' pi', y_axis[0]),
            (str(x_axis[1]/pi)+ ' pi', y_axis[1]),
            (str(x_axis[2]/pi)+ ' pi', y_axis[2]),
            (str(x_axis[3]/pi)+ ' pi', y_axis[3]),
            (str(x_axis[4]/pi)+ ' pi', y_axis[4]),
        )
        for point in points:
            print(point)
        return points
    
    if function == 'tan':
        period = pi / omega
        x_axis = [0, period/4, period/2, 3*period/4, period]
        y_axis = []
        for point in x_axis:
            y_value = alpha*tan(omega*point - chi) + beta
            y_axis.append(round(y_value))
        points = (
            (str(x_axis[0]/pi)+ ' pi', y_axis[0]),
            (str(x_axis[1]/pi)+ ' pi', y_axis[1]),
            (str(x_axis[2]/pi)+ ' pi', y_axis[2]),
            (str(x_axis[3]/pi)+ ' pi', y_axis[3]),
            (str(x_axis[4]/pi)+ ' pi', y_axis[4]),
        )
        for point in points:
            print(point)
        return points
    
    if function == 'csc':
        period = 2*pi / omega
        x_axis = [0, period/4, period/2, 3*period/4, period]
        y_axis = []
        for point in x_axis:
            try:
                y_value = alpha/sin(omega*point - chi) + beta
            except ZeroDivisionError:
                y_value = 'undefined'
                y_axis.append(y_value)
                continue
            if y_value > 5 * alpha or y_value < -5 * alpha: 
                y_value = 'undefined'
                y_axis.append(y_value)
                continue
            y_axis.append(round(y_value))
        points = (
            (str(x_axis[0]/pi)+ ' pi', y_axis[0]),
            (str(x_axis[1]/pi)+ ' pi', y_axis[1]),
            (str(x_axis[2]/pi)+ ' pi', y_axis[2]),
            (str(x_axis[3]/pi)+ ' pi', y_axis[3]),
            (str(x_axis[4]/pi)+ ' pi', y_axis[4]),
        )
        for point in points:
            print(point)
        return points
    
    if function == 'sec':
        period = 2*pi / omega
        x_axis = [0, period/4, period/2, 3*period/4, period]
        y_axis = []
        for point in x_axis:
            try:
                y_value = alpha/cos(omega*point - chi) + beta
            except ZeroDivisionError:
                y_value = 'undefined'
                y_axis.append(y_value)
                continue
            if y_value > 5 * alpha or y_value < -5 * alpha: 
                y_value = 'undefined'
                y_axis.append(y_value)
                continue
            y_axis.append(round(y_value))
        points = (
            (str(x_axis[0]/pi)+ ' pi', y_axis[0]),
            (str(x_axis[1]/pi)+ ' pi', y_axis[1]),
            (str(x_axis[2]/pi)+ ' pi', y_axis[2]),
            (str(x_axis[3]/pi)+ ' pi', y_axis[3]),
            (str(x_axis[4]/pi)+ ' pi', y_axis[4]),
        )
        for point in points:
            print(point)
        return points
    
    if function == 'cot':
        period = pi / omega
        x_axis = [0, period/4, period/2, 3*period/4, period]
        y_axis = []
        for point in x_axis:
            try:
                y_value = alpha/tan(omega*point - chi) + beta
            except ZeroDivisionError:
                y_value = 'undefined'
                y_axis.append(y_value)
                continue
            if (y_value > 5 * alpha or y_value < -5 * alpha): 
                y_value = 'undefined'
                y_axis.append(y_value)
                continue
            y_axis.append(round(y_value))
        points = (
            (str(x_axis[0]/pi)+ ' pi', y_axis[0]),
            (str(x_axis[1]/pi)+ ' pi', y_axis[1]),
            (str(x_axis[2]/pi)+ ' pi', y_axis[2]),
            (str(x_axis[3]/pi)+ ' pi', y_axis[3]),
            (str(x_axis[4]/pi)+ ' pi', y_axis[4]),
        )
        for point in points:
            print(point)
        return points

def omega_psi_inputs(string: str):
    '''
    unit test for converting inputs in terms of pi
    to base-64 floats
    '''

    if 'pi' in string:
        string = string.replace('pi', '')
        print(f'Adjusted Input: {round(float(string) * pi, 2)}')
        return round(float(string) * pi, 2)

    else:
        return float(string)
    

def run() -> None:
    while True:
        status = True
        if status:
            function = input('Enter func: ')
            alpha = input('Enter Alpha: ')
            beta = input('Enter Beta: ')
            omega = omega_psi_inputs(input('Enter Omega: '))
            phi = omega_psi_inputs(input('Enter Phi: '))


            brute_force_solve(
                alpha=float(alpha),
                beta=float(beta),
                omega=omega,
                chi=phi,
                function= function
            )
            status = bool(input('Enter Status(0 for quit, 1 for continue): '))

if __name__ == '__main__':
    run()