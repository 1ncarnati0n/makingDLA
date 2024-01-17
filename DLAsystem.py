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

# Input Variables
w = _Weight
go = _Go
crv = _Simulation
seed = _Seed
threshold = _Threshold
angle = _Angle

# Sub Functions 
def get_random_point(crv):
    # 원으로부터 임의점 얻기
    rndm = random.random()
    rndm_point = crv.PointAtNormalizedLength(rndm) # RhinoCommon API
    return rndm_point
    
def get_vector(point_s, point_e):
    # 01. 벡터방향 얻기
    vector = point_e - point_s
    # 02. 벡터 단위화 하기
    vector.Unitize() # RhinoCommon API
    # 03. 임의각도로 벡터방향 변경 
    rndm = random.uniform(math.radians(-angle), math.radians(angle)) # RhinoCommon API
    vector.Rotate(rndm, rg.Plane.WorldXY.ZAxis) # RhinoCommon API
    return vector
    
def move_point(point, vector):
    # 점 이동시키기
    point = point + vector * w # 가중치
    return point
    
def get_distance(point_s, point_e):
    # 이동거리 구하기
    dstnc = point_s.DistanceTo(point_e) # RhinoCommon API
    return dstnc
    
def get_closest_point(point, aggrgt_lst):
    dstnc_lst = [point.DistanceTo(aggrgt) for aggrgt in aggrgt_lst] # RhinoCommon API
    mnmm_dstnc = min(dstnc_lst)
    mnmm_idx = dstnc_lst.index(mnmm_dstnc)
    clsst_point = aggrgt_lst[mnmm_idx]
    return clsst_point
    
def get_segment(point_s, point_e):
    # 병합된 두점 사이 선으로 연결
    segment = rg.Line(point_s, point_e) # RhinoCommon API
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
        
        if dstnc <= threshold: # 임계값보다 거리가 작은 경우
            segment = get_segment(prtcl, clsst_point)
            seg_lst.append(segment) # 연결 선들...
            aggrgt_lst.append(prtcl) # 연결된 점들...
            prtcl = get_random_point(crv) # 초기화            
        
    return prtcl, aggrgt_lst, seg_lst

# 실행!!
a, b, c = main()
