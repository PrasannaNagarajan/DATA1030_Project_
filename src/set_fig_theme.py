import matplotlib.pyplot as plt

def set_project_theme():
    """
    Sets global configuration parameters for all figures in the project.
    """ 

    #  Figure properties
    plt.rcParams['figure.figsize'] = (8, 5)     
    # figure quality
    plt.rcParams['figure.dpi'] = 150  
    # set tight layout         
    plt.rcParams['figure.autolayout'] = True 

    # Typography and fonts
    plt.rcParams['font.size'] = 11              
    plt.rcParams['axes.labelsize'] = 12          
    plt.rcParams['axes.titlesize'] = 16          
    plt.rcParams['xtick.labelsize'] = 10         
    plt.rcParams['ytick.labelsize'] = 10 

set_project_theme()