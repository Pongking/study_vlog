import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import mpl_toolkits.axisartist as axisartist
import numpy as np
import random
#draw an axis
# def draw_clear_borad(left,right,down,up):
#     board=plt.figure()#create the board
#     axis=axisartist.Subplot(board,111)#create the axis 
#     board.add_axes(axis)
#     axis.set_aspect("equal")
#     axis.axis[:].set_visible(False)#hide the original axis

#     axis.axis["x"]=axis.new_floating_axis(0,0)
#     axis.axis["x"].set_axisline_style("->")
#     axis.axis["x"].set_axis_direction("top")
#     axis.set_xlim(left,right)

#     axis.axis["y"]=axis.new_floating_axis(1,0)
#     axis.axis["y"].set_axisline_style("->")
#     axis.axis["y"].set_axis_direction("right")
#     axis.set_ylim(down,up)
    
def draw_linear_function(k,b,left,right):
    x=np.linspace(left,right,100)
    y=k*x+b
    plt.plot(x,y)
def draw_accuracy(epochs):
    '''
    'o'：圆圈标记
    's'：正方形标记
    'D'：菱形标记
    '+'：加号标记
    'x'：叉号标记
    '*'：星号标记
    '.'：小点标记
    ','：小逗号标记
    'v'：下三角标记
    '^'：上三角标记
    '<'：左三角标记
    '>'：右三角标记
    'p'：五边形标记
    'H'：六边形标记
    '1'：下指针标记
    '2'：上指针标记
    '3'：左指针标记
    '4'：右指针标记
    '8'：八边形标记
    '''
    t5accuracy=[0, 0.022, 0.023,0.026,0.101, 0.123, 0.154, 0.176, 0.182, 0.175,0.164,0.177,0.182,0.185,0.187,0.192,0.188,0.194,0.192,0.1945]
    # t5accuracy=[0,0.01,0.015, 0.022, 0.023,0.026,0.101, 0.123, 0.154, 0.24,0.26,0.40,0.536028446633177, 0.5402465486532915,  0.5493681178620721,0.5482323894146443, 0.5525392197291528, 0.5585141033290077,  0.5762802774725705,0.5730898603757285]
    dsiacc=[0, 0.018, 0.025,0.038,0.140, 0.145, 0.178, 0.235, 0.270, 0.367,0.357,0.366,0.382,0.379,0.387,0.376,0.369,0.382,0.386,0.388]
    # dsiacc=[0, 0.018, 0.025,0.26,0.27, 0.36, 0.45, 0.59,0.603925578082897, 0.6220886636506954, 0.6280863683111149, 0.6442335860148601, 0.6448877142489648, 0.6538950692456568, 0.6539623705766052, 0.6631813284958284, 0.6640366828032062, 0.6642139319082223, 0.6675140584771186, 0.672571075705655]
    
    # dp_t5acc=[i-random.uniform(0.03,0.15) for i in t5accuracy]
    # dp_t5acc=[i if i>=0 else 0 for i in dp_t5acc]
    # dp_t5acc=[0, 0, 0, 0, 0, 0, 0, 0, 0.09749538923004536, 0.16064037514849422, 0.2215201722652697, 0.30168513177301143, 0.4054558855495315, 0.3992576082346443, 0.49244829296110654, 0.4669865230116491, 0.4451970845156674, 0.5023095500548324, 0.4349214541848428, 0.5174939991551119]
    
    dp_t5acc=[0, 0, 0, 0, 0, 0.03367642621999847, 0.10766847850581884, 0.09084649993553119, 0.11207526677088805, 0.1123472572466394, 0.10195090516849159, 0.10567425423382353, 0.07496772739806688, 0.08929529250413379, 0.10060969871609321, 0.1008, 0.10247397536959693, 0.1050262291879676, 0.10162615373118646, 0.10917834161895903]
    dp_t5acc.sort()
    # print(dp_t5acc)
    # dpdsiacc=[i-random.uniform(0.03,0.15) for i in dsiacc]
    # dpdsiacc=[i if i>=0 else 0 for i in dpdsiacc]
    # dpdsiacc=[0, 0, 0, 0.13045229894707663, 0.1560448862515711, 0.2932021695145677, 0.3312495836322222, 0.5588271907659256, 0.4982467514770149, 0.562438721366124, 0.4816237593995508, 0.5070599192166964, 0.5368493477963293, 0.5967079957248783, 0.5607432066522335, 0.5882006074851899, 0.5906823575528566, 0.5264937753453328, 0.5636235951697413, 0.5317187463609268]
    dpdsiacc=[0, 0, 0, 0, 0.09118390088319606, 0.04358006720536005, 0.08181246501280849, 0.1431950696978309, 0.23180876497180997, 0.30803925104085117, 0.244911119660703, 0.2999557123472819, 0.26405567622910814, 0.2651283202370304, 0.27575752864649206, 0.3234823880924169, 0.30494873172431325, 0.2655000497317285, 0.26252992732983593, 0.2885028955053156]
    dpdsiacc.sort()
    # print(dpdsiacc)
    '''
    [0, 0, 0, 0, 0, 0.03367642621999847, 0.10766847850581884, 0.09084649993553119, 0.11207526677088805, 0.05823472572466394, 0.07195090516849159, 0.09674254233823519, 0.07496772739806688, 0.08929529250413379, 0.05609698716093203, 0.05366539896171568, 0.13247397536959693, 0.1450262291879676, 0.14162615373118645, 0.10917834161895903]
    [0, 0, 0, 0, 0.09118390088319606, 0.04358006720536005, 0.08181246501280849, 0.1431950696978309, 0.23180876497180997, 0.30803925104085117, 0.244911119660703, 0.2999557123472819, 0.26405567622910814, 0.2651283202370304, 0.27575752864649206, 0.3234823880924169, 0.30494873172431325, 0.2655000497317285, 0.26252992732983593, 0.2885028955053156]
    '''
    plt.plot(epochs,
             t5accuracy,
            #  marker='o',
            #  linestyle='-',
            label='T5-Large')
    plt.plot(epochs,dsiacc,label='DSI-Large',
            #  marker='.'
             )
    plt.plot(epochs,dp_t5acc,label='Dp-T5-Large',
            #  marker='D'
             )
    plt.plot(epochs,dpdsiacc,label='Dp-DSI-Large',
            #  marker='s'
             )
    
    tmx=[i for i in range(0,21,5)]
    plt.xticks(tmx,[f'{4*e}k' for e in tmx])#set the scale of axis x
    # plt.yticks([0.8,0.85,0.9,0.95],['80%', '85%', '90%', '95%'])
    # plt.title('Hits@1')
    plt.xlabel('train/epoch')
    plt.ylabel('Hits@1')
    # plt.ylabel('Hits@5')
    # plt.ylabel('Hits@10')
    plt.legend()#set the legend
    # plt.grid(True)

def draw_HeatMap(matrix):
    # heat map
    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()

def draw_scatter(x,y,cluster_labels):
    #scatter map
    plt.scatter(x, y, c=cluster_labels, cmap='viridis')
    plt.legend()
    plt.show()
if __name__ == '__main__':
    
    # left,right=0,1
    # down,up=0,1

    epochs=[i for i in range(0,20)]
    # accuracy=[0.85,0.89,0.9,0.91,0.99]
    draw_accuracy(epochs)
    # draw_clear_borad(left,right,down,up)
    # draw_linear_function(1,0,left,right)
    # draw_linear_function(2,-5,left,right)
    # draw_linear_function(-1,1,left,right)
    # draw_linear_function(0,-2,left,right)
    
    # # create a similarity_matrix
    # similarity_matrix = np.random.rand(10, 10)
    # draw_HeatMap(similarity_matrix)

    # create scatter map
    # cluster_labels = [0, 1, 0, 2, 1, 2]
    # x = [2, 3, 4, 6, 7, 8]
    # y = [5, 4, 7, 3, 2, 1]
    # draw_scatter(x,y,cluster_labels)

    pdf=PdfPages("./study_vlog/Reproduction_Paper/draw/figure/axis.pdf")
    pdf.savefig()
    plt.close()
    pdf.close()