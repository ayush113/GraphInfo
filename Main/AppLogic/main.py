from . import bonieRules
from . import plotting
import glob
import os

def run(inp):
    cwd = os.getcwd()
    os.system('rm ' + cwd +  '/static/Main/img/Plots/*.png')
    tups = bonieRules.extract_tuples(inp)
    plotting.plotter(tups)
    files = glob.glob('*.png')
    for i in files:
        print(cwd)
        os.system('mv ' + i + ' ' + cwd+'/static/Main/img/Plots/' + i)
