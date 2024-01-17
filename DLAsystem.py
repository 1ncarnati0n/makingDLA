"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "1ncarnati0n"

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random
import math

# input variables
w = _Weight
go = _Go
crv = _Simulation
seed = _Seed
threshold = _Threshold
angle = _Angle

# sub functions 
def get_random_point(crv):
    # get random point on the circle
    rndm = random.random()
    rndm_point = crv.PointAtNormalizedLength(rndm)
    return rndm_point
    
def get_vector(point_s, point_e):
    # get a translation vector 
    # 01. get a directional vector 
    vector = point_e - point_s
    # 02. unitize the vector
    vector.Unitize()
    # 03. 임의 각도로 벡터 방향변경 
    rndm = random.uniform(math.radians(-angle), math.radians(angle))
    vector.Rotate(rndm, rg.Plane.WorldXY.ZAxis)
    return vector
    
def move_point(point, vector):
    point = point + vector * w # 가중치
    return point
    
def get_distance(point_s, point_e):
    dstnc = point_s.DistanceTo(point_e)
    return dstnc
    
def get_closest_point(point, aggrgt_lst):
    dstnc_lst = [point.DistanceTo(aggrgt) for aggrgt in aggrgt_lst]
    mnmm_dstnc = min(dstnc_lst)
    mnmm_idx = dstnc_lst.index(mnmm_dstnc)
    clsst_point = aggrgt_lst[mnmm_idx]
    return clsst_point
    
def get_segment(point_s, point_e):
    segment = rg.Line(point_s, point_e)
    return segment


# Execute Function
def main():
    if go == False:
        global prtcl
        global aggrgt_lst
        global seg_lst

        prtcl = get_random_point(crv)
        aggrgt_lst = []
        seg_lst = []
        aggrgt_lst.append(seed)
        
    else:
        vector = get_vector(prtcl, seed)
        prtcl = move_point(prtcl, vector)
        
        clsst_point = get_closest_point(prtcl, aggrgt_lst)
        dstnc = get_distance(prtcl, clsst_point) 
        
        if dstnc <= threshold:
            segment = get_segment(prtcl, clsst_point)
            seg_lst.append(segment)
            aggrgt_lst.append(prtcl)
            prtcl = get_random_point(crv)            
        
    return prtcl, aggrgt_lst, seg_lst

# Execute Function
a, b, c = main()
