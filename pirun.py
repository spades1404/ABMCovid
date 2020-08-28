import os
os.chdir("..")

from ABMC19.batchrun import batchRun
import sys
import asyncio
import openpyxl
from openpyxl import Workbook

wb = Workbook()
wb.save("output.xlsx")

## No Params
x = batchRun(100,0,0,0,0,1,False,False,range(100,150,50))
x.to_excel("output.xlsx",sheet_name="NOPARAM")
##With agent precaution only
x = batchRun(100,1,1,1,1,1,False,False,range(100,150,50))
x.to_excel("output.xlsx",sheet_name="AGENTPARAMONLY")
##Effective Lockdown + agent precaution
x = batchRun(100,1,1,1,1,1,False,True,range(100,150,50))
x.to_excel("output.xlsx",sheet_name="LOCKDOWN")
