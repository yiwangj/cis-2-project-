#!/usr/bin/env python
# coding: utf-8

# In[11]:


def rgb_to_hex(r, g, b,alpha):
    alpha_new=(alpha / 255).round(2)
    if alpha_new==0.1 or alpha_new==0.2:
        r=255
        g=0
        b=0
    elif alpha_new == 0.3:
        r = 255
        g = 255
        b = 0
    elif alpha_new == 1:
        r = 0
        g = 255
        b = 0 
    return '#%02x%02x%02x' % (int(r), int(g), int(b))
 
print(rgb_to_hex(0,0,0,25.5))


# In[13]:


from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import h5py
import numpy as np

from mergehdf5 import DataMerger

params = {
    "legend.fontsize": "x-large",
    "figure.figsize": (9, 5),
    "axes.labelsize": "large",
    "axes.titlesize": "x-large",
    "xtick.labelsize": "medium",
    "ytick.labelsize": "medium",
}

plt.rcParams.update(params)

def rgb_to_hex(r, g, b,alpha):
    alpha_new=(alpha / 255).round(2)
    if alpha_new==0.1 or alpha_new==0.2:
        r=255
        g=0
        b=0
    elif alpha_new == 0.3:
        r = 255
        g = 255
        b = 0
    elif alpha_new == 1:
        r = 0
        g = 255
        b = 0 
    return '#%02x%02x%02x' % (int(r), int(g), int(b))
        
    
    

files = []
files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])

files.append(['C_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P0_L3_color/2023-04-13 10:51:15'])
files.append(['K_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/klobo_P0_L3_color/2023-04-06 10:24:32'])
files.append(['P_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P0_L3_color/2023-04-06 09:34:53'])
files.append(['T_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P0_L3_color_v2/2023-04-06 11:13:31'])


files.append(['C_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L2_color/2023-04-13 10:38:13'])
files.append(['K_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
# files.append(['P5', '/home/amunawa2/RedCap/Guidance/Participant_5/2022-11-10 13:14:55'])
files.append(['P_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
files.append(['T_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L2_color/2023-04-06 11:34:55'])



files.append(['C_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L2_color/2023-04-13 10:08:49'])
files.append(['K_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L2_color/2023-04-06 10:08:32'])
files.append(['P_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L2_color/2023-04-06 09:18:08'])
files.append(['T_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L2_color/2023-04-06 11:44:29'])

files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])


data_merger = DataMerger()
color_num=[]
avg=[]
for lab, f in files:
    num=0
    data = data_merger.get_merged_data(f, False)

    vcol = data['voxels_removed']['voxel_color'][()]

    colors = [None for _ in range(vcol.shape[0])]

    for i, c in enumerate(vcol):
        colors[i] = rgb_to_hex(c[1], c[2], c[3],c[4])
        if (c[4]/ 255).round(2)==0.1 or (c[4]/ 255).round(2)==0.2:
            num=num+1
            
           
    color_num.append(num)
     
for i in range(0, len(color_num), 4):
    mean = sum(color_num[i:i+4])/4
    avg.append(mean)
    
print(avg)


# In[14]:


files = []
files.append(['C_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L1_no_color/2023-04-13 10:44:15'])
files.append(['K_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L1_no_color/2023-04-06 10:21:48'])
files.append(['P_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L1_no_color_v2/2023-04-06 08:52:32'])
files.append(['T_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L1_no_color/2023-04-06 11:26:28'])

files.append(['C_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L3_no_color/2023-04-13 10:32:25'])
files.append(['K_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L3_no_color/2023-04-06 09:59:55'])
files.append(['P_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L3_no_color/2023-04-06 09:14:06'])
files.append(['T_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L3_no_color/2023-04-06 11:39:26'])

files.append(['C_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L1_no_color/2023-04-13 10:23:43'])
files.append(['K_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L1_no_color/2023-04-06 10:17:49'])
files.append(['P_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P2_L1_no_color/2023-04-06 09:22:09'])
files.append(['T_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L1_no_color/2023-04-06 11:07:07'])

files.append(['C_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L1_no_color/2023-04-13 10:19:26'])
files.append(['K_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L1_no_color/2023-04-06 09:53:16'])
files.append(['P_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L1_no_color/2023-04-06 08:57:24'])
files.append(['T_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L1_no_color/2023-04-06 11:18:42'])

files.append(['C_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L3_no_color/2023-04-13 10:28:22'])
files.append(['K_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L3_no_color/2023-04-06 10:15:10'])
files.append(['P_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L3_no_color/2023-04-06 09:31:26'])
files.append(['T_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L3_no_color/2023-04-06 11:31:01'])


data_merger = DataMerger()
color_num=[]
avg_non=[]
for lab, f in files:
    num=0
    data = data_merger.get_merged_data(f, False)

    vcol = data['voxels_removed']['voxel_color'][()]

    colors = [None for _ in range(vcol.shape[0])]

    for i, c in enumerate(vcol):
        colors[i] = rgb_to_hex(c[1], c[2], c[3],c[4])
        if (c[4]/ 255).round(2)==0.1 or (c[4]/ 255).round(2)==0.2:
            num=num+1
            
           
    color_num.append(num)
     
for i in range(0, len(color_num), 4):
    mean = sum(color_num[i:i+4])/4
    avg_non.append(mean)
    
print(avg_non)


# In[15]:


data = [avg, avg_non]

fig, ax = plt.subplots()

# Creating axes instance
bp = ax.boxplot(data)

# Adding labels to x-axis
ax.set_xticklabels(['color', 'non_color'])

# Adding title to the plot
plt.title('red voxel removed')

# Displaying the plot
plt.show()


# In[ ]:




