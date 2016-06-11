
import matplotlib as M
from matplotlib.patches import Rectangle
import numpy as N
import pylab as P
import scipy as S 

M.rcParams['pdf.fonttype'] = 42
M.rcParams['ps.fonttype'] = 42



def make_symb(axi):
    """
    Helper function for plotMP. Create a symbol for scatter given axi.

    @param axi: fraction of poloidal energy in axisymmetric modes. 0<=axi<= 1.
    @type axi: float
    """

    theta = 2. * N.pi * N.arange(0, 1, 0.1)
    rx = N.zeros((11))
    ry = N.zeros((11))
    for j in N.arange(1, 11, 2.0):
        rx[j] = N.cos(theta[j])
        ry[j] = N.sin(theta[j])
    for j in N.arange(0, 10, 2.0):
        rx[j] = (0.1 + 0.9*axi) * N.cos(theta[j])
        ry[j] = (0.1 + 0.9*axi) * N.sin(theta[j])
    rx[10] = rx[0]
    ry[10] = ry[0]
    verts = zip(rx, ry)
    return verts


def visibility(vis,pol):
    """
    Helper function for plotMP. Defines the visibility/transparency of scatter
    symbols.

    @param vis: keyword among 'Visible', 'Invisible', and 'Transparent'.
    @type vis: string
    """

    if vis == "Visible":
        c = [pol]
        cmap = P.get_cmap('jet')
        v = True
        col = "0.0"
    elif vis == "Invisible": 
        c = [0.0]
        cmap = P.get_cmap('gist_yarg')
        v = False
        col = "1.0"
    elif vis == "Transparent": 
        c = [0.20]
        cmap = P.get_cmap('gist_yarg')
        v = True
        col = "0.80"
    else:
        c = None
        cmap = None
        v = None
        col = None
    
    return [c, cmap, v, col]


#####################
if __name__ == '__main__':

    plotFileName = 'confg.eps'  #save the plot to this file

    #Toupies stars ###
    #infile=open("zdi-colin.dat")
    infile=open("summary-toupies-v3-send.dat")
    massT=[]
    protT=[]
    BsqT=[]
    polT=[]
    dipT=[]
    axiT=[]
    nameT=[]
    ageT=[]
    teffT=[]
    radiusT=[]
    lumT=[]
    rossT=[]
    for line in infile:
        if (line.split()[0] != "#") & (line[0] != "#") :
            ageT+=[float(line.split()[2])]
            massT+=[float(line.split()[23])]
            protT+=[float(line.split()[4])]
            teffT+=[float(line.split()[6])]
            radiusT+=[float(line.split()[21])]
            rossT+=[float(line.split()[29])]
#            BsqT+=[float(line.split()[2])]
            BsqT+=[float(line.split()[32])]
            polT+=[float(line.split()[34])*0.01]
            dipT+=[float(line.split()[36])*0.01]
            axiT+=[float(line.split()[40])*0.01]
            nameT+=[line.split('"')[1]]            
    sigma = 5.67051E-008
    Rsun = 6.9599e8
    Lsun = 3.826e26
    lumT=(4.*N.pi*(N.array(radiusT)*Rsun)**2 *sigma*N.array(teffT)**4)/Lsun

    ##################
    #T Tauri stars from MaPP   ######
    infileTT=open("ttauri-params.dat")
    massTT=[]
    protTT=[]
    BsqTT=[]
    polTT=[]
    axiTT=[]
    nameTT=[]
    ageTT=[]
    teffTT=[]
    radiusTT=[]
    lumTT=[]
    rossTT=[]
    for line in infileTT:
        if (line.split()[0] != "#") & (line[0] != "#") :
            massTT+=[float(line.split()[1])]
            protTT+=[float(line.split()[3])]
            ageTT+=[float(line.split()[4])]
            teffTT+=[float(line.split()[7])]
            radiusTT+=[float(line.split()[2])]
            BsqTT+=[float(line.split()[8])**0.5]
            polTT+=[float(line.split()[9])]
            axiTT+=[float(line.split()[10])]
            rossTT+=[float(line.split()[11])]
            nameTT+=[line.split('"')[3]]
    sigma = 5.67051E-008
    Rsun = 6.9599e8
    Lsun = 3.826e26
    lumTT=(4.*N.pi*(N.array(radiusTT)*Rsun)**2 *sigma*N.array(teffTT)**4)/Lsun
    
    ##################

#    M.rc('text', usetex=True)
#    M.rc('font',**{'family':'serif','serif':['Computer Modern']})


#    _fig = P.figure(i, (10, 8))
    mainFig = P.figure(figsize=[12,8])

    ax = P.axes([0.075, 0.10, 0.650, 0.875], axisbg='w')
#    ax = P.axes()
    ax.set_xscale('log')
    ax.set_yscale('log')



    #Toupies points on the graph, in bold outlines
    #Bsize = lambda B: N.power(B, 0.6)*2.  #old better scaling for Toupies
    Bsize = lambda B: N.array(B)*2.  #pretty good scaling for all
    #Bsize = lambda B: (10.*N.log10(N.array(B)))**2  #linear scaling


    ###########################################
    #T Tarui star points on the graph
    Bsq_MPTT = Bsize(BsqTT)
    verts=[]
    for i in range(len(massTT)):
        print BsqTT[i]**0.5, axiTT[i], polTT[i], nameTT[i]
        _verts = make_symb(axiTT[i])
        verts.append(_verts)
        
        [c, cmap, v, col] = visibility("Visible",polTT[i])
        widthScaleM = (massTT[i]-0.5)*10.
    
        ax.scatter([ageTT[i]], [rossTT[i]], Bsq_MPTT[i],
                   c=c, marker=None, verts=verts[i], vmin=0, vmax=1, 
                   linewidths=2.0, color='b', visible=v, cmap=cmap)
    
        #label points
        ha = 'left'
        va = 'bottom'
        #P.text(ageTT[i], 1.02*rossTT[i], nameTT[i],
        #       ha=ha, va=va, color='b', visible=v, fontsize=10)
        #       #ha=ha, va=va, color='b', visible=v, fontsize=12)
    ##############################

    # Toupies Stars #
    Bsq_MPT = Bsize(BsqT)
    verts=[]
    for i in range(len(massT)):
        _verts = make_symb(axiT[i])
        #_verts = make_symb(dipT[i])
        verts.append(_verts)
        
        widthScaleM = (massT[i]-0.5)*10.
        [c, cmap, v, col] = visibility("Visible",polT[i])

        ax.scatter([ageT[i]], [rossT[i]], Bsq_MPT[i],
                   c=c, marker=None, verts=verts[i], vmin=0, vmax=1, 
                   linewidths=1.0, color='k', visible=v, cmap=cmap)
        #ax.scatter([ageT[i]], [protT[i]], Bsq_MPT[i],
        #           c=c, marker=None, verts=verts[i], vmin=0, vmax=1, 
        #           linewidths=widthScaleM, visible=v, cmap=cmap)

        #label points
        ha = 'left'
        va = 'bottom'
        #P.text(ageT[i], 1.02*(rossT[i]), nameT[i],
        #       ha=ha, va=va, color=col, visible=v, fontsize=10)
        #       #ha=ha, va=va, color=col, visible=v, fontsize=12)

    #############################

    #P.axis([0.2, 100., 0.05, 1.5])  #my attempt to fix the x and y axis ranges.
    #P.axis([1., 20000., 0.3, 50.])  #my attempt to fix the x and y axis ranges, for rotation-age
    P.axis([1e0, 2e4, 0.01, 3.])  #my attempt to fix the x and y axis ranges, for rossby-<B>


    # ticks
    #MLx = M.ticker.MultipleLocator(100.)
    #MLy = M.ticker.MultipleLocator(1.)
    #MLy = M.ticker.LogLocator(base=10.0)
    MFy = M.ticker.FormatStrFormatter('%.2f')
    MFx = M.ticker.FormatStrFormatter('%.f')
    #ax.yaxis.set_major_locator(MLx)
    #ax.yaxis.set_major_locator(MLy)
    ax.xaxis.set_major_formatter(MFx)
    ax.yaxis.set_major_formatter(MFy)
    ax.set_ylabel(r'$\rm Rossby\, number$', fontsize=20)
    ax.set_xlabel(r'$\rm Age\ (Myr)$', fontsize=20)
    ax.tick_params(axis='both', labelsize=14)


    # colorbar/scale
    #   shape <=> axisym ratio
    #   size <=> mag energy
    #if plotMP_ori == 'landscape':
    ax_leg_1 = P.axes([0.810, 0.100, 0.085, 0.875], axisbg='w') #position of ledgend
    #elif plotMP_ori == 'portrait':
    #    ax_leg_1 = P.axes([0.775,0.10,0.100,0.875], axisbg='w')
    x1 = 0.5
    y1 = N.linspace(0.1, 0.9, 6)     #vertical spacing (don't change)
    #s1 = N.logspace(3.477, 5.863, 6) #simbol size range (mag energy) #default
    #s1 = N.logspace(3., 5., 6) #simbol size range (mag energy)  #pretty good range for all
    s1 = N.logspace(1., 3., 6) #simbol size range (mag energy)  #pretty good range for all
    print s1
    ytl2 = []
    for i in range(len(s1)):
        _str = "%.f" % (s1[i])
        ytl2.append(_str)
        s1[i] = Bsize(s1[i])
    axi1 = N.linspace(0, 1, 6)  #symbol shape range (fraction axisymmetric)
    pol1 = N.linspace(0, 1, 6)  #symbol colour range (fraction poloidal)
    ytl1 = []
    for i in range(len(axi1)):
        _str = "%.1f" % (axi1[i])
        ytl1.append(_str)
    for i in range(len(y1)):
        #lineWidthMassLedgend = (1.0-0.5)*10./len(y1) #width propto M/Msun*10
        vrts1 = make_symb(axi1[i])
        ax_leg_1.scatter([x1], [y1[i]], [s1[i]], c=[pol1[i]], vmin=0, vmax=1, 
                         linewidths=0.0, 
#                         linewidths=lineWidthMassLedgend*i, 
                         marker=None, verts=vrts1)
    ax_leg_1.set_ylim((0, 1))
    ax_leg_1.set_yticks(y1)
    ax_leg_1.set_yticklabels(ytl1)
    ax_leg_1.set_yticklabels(ytl1, fontsize=16)
    ax_leg_1.set_ylabel(r'$\rm Axisymmetry\ (shape)\ /\ Poloidal\ (colour)$',
                        fontsize=20)
    ax_leg_2 = P.twinx()
    ax_leg_2.yaxis.tick_right()
    ax_leg_2.set_yticks(y1)
    ax_leg_2.set_yticklabels(ytl2)
    ax_leg_2.set_yticklabels(ytl2, fontsize=16)
    ax_leg_2.set_ylabel(r'$\rm\left\langle B\right\rangle\ (G)$', fontsize=20)
    ax_leg_2.set_xticks([])


    mainFig.savefig(plotFileName)
    P.show()
