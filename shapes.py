import numpy as np
from random import random
from random import uniform
from random import choice
from random import randrange
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import shutil

def paint(input,NUM_RECS,A_CONST,N_CONST,ASPECT_RANGE,MODE,DEBUG=False):
  # NUM_RECS=iterations
  # A_CONST=area_decay#0.35
  # N_CONST=number_growth
  # ASPECT_RANGE=aspect_ratio
  # DEBUG=debug_mode
  # MODE=model
  img = mpimg.imread(input)




  R_mean=[None]*NUM_RECS
  G_mean=[None]*NUM_RECS
  B_mean=[None]*NUM_RECS




  x=img.shape[0]
  y=img.shape[1]

  R=np.zeros((x,y),dtype=int)
  G=np.zeros((x,y),dtype=int)
  B=np.zeros((x,y),dtype=int)
  R[:,:]=img[:,:,0]
  G[:,:]=img[:,:,1]#100
  B[:,:]=img[:,:,2]#img[:,:,2]
  new_img=np.zeros((x,y,3),dtype=int)

  new_img[:,:,:]=0
  #new_img[:,:,1]=B
  #new_img[:,:,2]=G


  N=[None]*NUM_RECS
  AREAS=[None]*NUM_RECS
  X_S=[None]*NUM_RECS
  Y_S=[None]*NUM_RECS
  X_E=[None]*NUM_RECS
  Y_E=[None]*NUM_RECS

  X_L=[None]*NUM_RECS
  Y_L=[None]*NUM_RECS

  R_m=[None]*NUM_RECS
  G_m=[None]*NUM_RECS
  B_m=[None]*NUM_RECS

  ASPECTS=[None]*NUM_RECS

  xth=np.linspace(0,NUM_RECS,NUM_RECS+1)
  if MODE=='e':
    Nth=np.exp(N_CONST*xth)
    Ath=x*y*np.exp(-(Nth+1)*A_CONST)
  if MODE=='l':
    Nth=N_CONST*xth*10
    Ath=(-(xth)*A_CONST*1E5)+x*y

  if DEBUG==True:
    fig, (ax1, ax2) = plt.subplots(nrows=2)
    ax1.plot(xth,Nth,label='Number of rectangles')
    ax1.legend()
    ax2.plot(xth,Ath,label='Area of rectangles')
    ax2.legend()
    fig.tight_layout()

  if DEBUG==False:
    for i in range(NUM_RECS):
        #print('on',i,'th iteration')
        if MODE=='e':
          N[i]=int(np.exp(N_CONST*i))
        if MODE=='l':
          N[i]=int(N_CONST*i*100)
        AREAS[i]=np.zeros(N[i],dtype=int)
        X_S[i]=np.zeros(N[i],dtype=int)
        Y_S[i]=np.zeros(N[i],dtype=int)
        X_E[i]=np.zeros(N[i],dtype=int)
        Y_E[i]=np.zeros(N[i],dtype=int)
        X_L[i]=np.zeros(N[i],dtype=int)
        Y_L[i]=np.zeros(N[i],dtype=int)
        R_m[i]=np.zeros(N[i],dtype=int)
        G_m[i]=np.zeros(N[i],dtype=int)
        B_m[i]=np.zeros(N[i],dtype=int)
        ASPECTS[i]=np.zeros(N[i],dtype=float)
        for j in range(len(AREAS[i])):
          if MODE=='e':
            AREAS[i][j]=int(x*y*(np.exp(-(i+1)*A_CONST)))
            if AREAS[i][j]<0:
              AREAS[i][j]=10
          if MODE=='l':
            AREAS[i][j]=int((-(i)*A_CONST*1E5)+x*y)
            if AREAS[i][j]<0:
              AREAS[i][j]=10
          ASPECTS[i][j]=uniform(1,ASPECT_RANGE)
          ASPECTS[i][j]=choice((1/ASPECTS[i][j],ASPECTS[i][j]))
          Y_L[i][j]=int(np.sqrt(AREAS[i][j]/ASPECTS[i][j]))
          X_L[i][j]=int(AREAS[i][j]/Y_L[i][j])
          if X_L[i][j]>x:
            X_L[i][j]=x
          if Y_L[i][j]>y:
            Y_L[i][j]=y
          try:
            X_S[i][j]=randrange(0,(x-X_L[i][j]))
            Y_S[i][j]=randrange(0,(y-Y_L[i][j]))
          except:
            X_S[i][j]=0
            Y_S[i][j]=0
          X_E[i][j]=X_S[i][j]+X_L[i][j]
          Y_E[i][j]=Y_S[i][j]+Y_L[i][j]
          R_m[i][j]=int(np.mean(R[X_S[i][j]:X_E[i][j],Y_S[i][j]:Y_E[i][j]]))
          G_m[i][j]=int(np.mean(G[X_S[i][j]:X_E[i][j],Y_S[i][j]:Y_E[i][j]]))
          B_m[i][j]=int(np.mean(B[X_S[i][j]:X_E[i][j],Y_S[i][j]:Y_E[i][j]]))
          new_img[X_S[i][j]:X_E[i][j],Y_S[i][j]:Y_E[i][j],0]=R_m[i][j]
          new_img[X_S[i][j]:X_E[i][j],Y_S[i][j]:Y_E[i][j],1]=G_m[i][j]
          new_img[X_S[i][j]:X_E[i][j],Y_S[i][j]:Y_E[i][j],2]=B_m[i][j]
    plt.imshow(new_img)
    a=new_img
    vv=a.astype('uint8')
    plt.imsave(input[0:len(input)-4]+str(NUM_RECS)+str(int(A_CONST*100))+str(int(100*N_CONST))+str(ASPECT_RANGE)+str(MODE)+'.png',vv)






def gifproducer(input,NUM_RECS,A_CONST,N_CONST,ASPECT_RANGE,MODE,DEBUG=False):
  try:
    os.makedirs(input[0:len(input)-4])
  except:
    pass
  shutil.copy(input,input[0:len(input)-4])
  os.chdir(input[0:len(input)-4])
  for i in range(NUM_RECS):
    print(i)
    paint(input,i,A_CONST,N_CONST,ASPECT_RANGE,MODE,DEBUG=False)
  os.chdir('..')

def gifstatic(input,NUM_RECS,A_CONST,N_CONST,ASPECT_RANGE,MODE,DEBUG=False):
  try:
    os.makedirs(input[0:len(input)-4]+'steady')
  except:
    pass
  shutil.copy(input,input[0:len(input)-4]+'steady')
  os.chdir(input[0:len(input)-4]+'steady')
  li=[None]*NUM_RECS
  for i in range(7):
    print(i)
    li[i]=NUM_RECS
    paint(input,li[i],A_CONST,N_CONST,ASPECT_RANGE,MODE,DEBUG=False)
    os.rename(input[0:len(input)-4]+str(NUM_RECS)+str(int(A_CONST*100))+str(int(100*N_CONST))+str(ASPECT_RANGE)+str(MODE)+'.png',str(i)+'.png')
  os.chdir('..')