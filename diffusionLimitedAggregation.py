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
g = _Go
smltn = _Simulation
sd = _Seed
thrshld = _Threshold
angle = _Angle

# sub functions 
def GetRandomPoint(crv):
    rndm = random.random()
    rndmPnt = crv.PointAtNormalizedLength(rndm)
    return rndmPnt
    
def GetVector(pntS, pntE):
    vctr = pntE - pntS
    vctr.Unitize()
    vctr = vctr * 2
    rndm = random.uniform(math.radians(-angle), 
                          math.radians(angle)
                          )
    vctr.Rotate(rndm, rg.Plane.WorldXY.ZAxis)
    return vctr
    
def MovePoint(pnt, trnsVctr):
    pnt = pnt + trnsVctr
    return pnt
    
def GetDistance(pntS, pntE):
    dstnc = pntS.DistanceTo(pntE)
    return dstnc
    
def GetClosestPoint(pnt, aggrgtLst):
    dstncLst = []
    for aggrgt in aggrgtLst:
        dstnc = pnt.DistanceTo(aggrgt)
        dstncLst.append(dstnc)
    mnmmDstnc = min(dstncLst)
    mnmmIndx = dstncLst.index(mnmmDstnc)
    clsstPnt = aggrgtLst[mnmmIndx]
    return clsstPnt
    
def GetClosestPointAlt(pnt, aggrgtLst):
    dstncLst = [pnt.DistanceTo(aggrgt) for aggrgt in aggrgtLst]
    mnmmDstnc = min(dstncLst)
    mnmmIndx = dstncLst.index(mnmmDstnc)
    clsstPnt = aggrgtLst.pop(mnmmIndx)
    return clsstPnt
    
def GetSegment(pntS, pntE):
    sgmnt = rg.Line(pntS, pntE)
    return sgmnt


# Execute Function
def Main():
    if g == False:
        global prtcl
        global aggrgtLst
        global sgmntLst
        prtcl = GetRandomPoint(smltn)
        aggrgtLst = []
        sgmntLst = []
        aggrgtLst.append(sd)
        
    else:
        vctr = GetVector(prtcl, sd)
        prtcl = MovePoint(prtcl, vctr)
        
        clsstPnt = GetClosestPoint(prtcl, aggrgtLst)
        dstnc = GetDistance(prtcl, clsstPnt) 
        
        if dstnc <= thrshld:
            sgmnt = GetSegment(prtcl, clsstPnt)
            sgmntLst.append(sgmnt)
            aggrgtLst.append(prtcl)
            prtcl = GetRandomPoint(smltn)            
        
    return prtcl, aggrgtLst, sgmntLst

# Execute Function
a, b, c = Main()
