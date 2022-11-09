
import numpy as np


def rotation(pos, theta):
    A = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return np.dot(pos, A.T)



def ship_coo(x, Lpp, B, Lrate=0.6, deg_flag=True, normalize_flag=True):    
    if deg_flag:
        psi = np.deg2rad(x[4])
    else:
        psi = x[4]
    
    if normalize_flag:
        B = B / Lpp
        Lpp = Lpp / Lpp

    pos_x = np.array([-0.5 * Lpp, Lrate * 0.5 * Lpp, 
                       0.5 * Lpp, Lrate * 0.5 * Lpp, -0.5 * Lpp])
    pos_y = np.array([-0.5 * B, -0.5 * B, 0.0, 0.5 * B, 0.5 * B])
    points = np.concatenate(
        [pos_x[:, np.newaxis], pos_y[:, np.newaxis]], axis=1
    )

    return rotation(points, psi) + x[[0,2]]



def rudder_p_coo(x, u, Lpp, B, deg_flag=True, normalize_flag=True):
    if normalize_flag:
        B = B / Lpp
        Lpp = Lpp / Lpp

    pos_dp1 = np.array([0, 0])
    pos_dp2 = np.array([0, -0.2*Lpp])
    
    r_pos_dp2 = rotation(pos_dp2, np.deg2rad(u[1]))

    move_pos_dp1  = pos_dp1   + np.array([-0.3*B, -0.5*Lpp])
    move_pos_dp2  = r_pos_dp2 + np.array([-0.3*B, -0.5*Lpp])

    if deg_flag:
        psi = np.deg2rad(-x[4])
    else:
        psi = -x[4]
    
    
    rud_p1 = rotation(move_pos_dp1, psi) + x[[2,0]]
    rud_p2 = rotation(move_pos_dp2, psi) + x[[2,0]]

    return rud_p1, rud_p2



def rudder_s_coo(x, u, Lpp, B, deg_flag=True, normalize_flag=True):
    if normalize_flag:
        B = B / Lpp
        Lpp = Lpp / Lpp

    pos_ds1 = np.array([0, 0])
    pos_ds2 = np.array([0, -0.2*Lpp])  
    
    r_pos_ds2 = rotation(pos_ds2, np.deg2rad(u[2]))

    move_pos_ds1  = pos_ds1   + np.array([0.3*B, -0.5*Lpp])
    move_pos_ds2  = r_pos_ds2 + np.array([0.3*B, -0.5*Lpp])

    if deg_flag:
        psi = np.deg2rad(-x[4])
    else:
        psi = -x[4]

    rud_s1 = rotation(move_pos_ds1, psi) + x[[2,0]]
    rud_s2 = rotation(move_pos_ds2, psi) + x[[2,0]]

    return rud_s1, rud_s2


def rudder_coo(x, u, Lpp, B, s_or_p, deg_flag=True, normalize_flag=True):
    if normalize_flag:
        B = B / Lpp
        Lpp = Lpp / Lpp
    
    if deg_flag:
        psi = np.deg2rad(-x[4])
    else:
        psi = -x[4]
        
    pos_front = np.array([0, 0])
    pos_rear = np.array([0, -0.2*Lpp])  
    
    if s_or_p == 's':
        r_pos_rear = rotation(pos_rear, np.deg2rad(u[0]))
        move_pos_front  = pos_front   + np.array([0.3*B, -0.5*Lpp])
        move_pos_rear   = r_pos_rear  + np.array([0.3*B, -0.5*Lpp])
    elif s_or_p == 'p':
        r_pos_rear = rotation(pos_rear, np.deg2rad(u[1]))
        move_pos_front  = pos_front   + np.array([-0.3*B, -0.5*Lpp])
        move_pos_rear   = r_pos_rear  + np.array([-0.3*B, -0.5*Lpp])

    rud_1 = rotation(move_pos_front, psi) + x[[2,0]]
    rud_2 = rotation(move_pos_rear, psi) + x[[2,0]]

    return rud_1, rud_2


