import numpy as np

def add_gradient(image):
    image = image.astype('float64')
    x,y,ch = image.shape
    m_x  = int(x/2)
    m_y = int(y/2)

    image[m_x,m_y] += image[m_x,m_y]*.5

    for i in range(0,50):
        for j in range(0,50):
            if ((i != 0) and (j != 0)):   
                image[m_x-i,m_y-j] += image[m_x-i,m_y-j]*(.5 - (max(i,j)/100)) 
                image[m_x+i,m_y-j] += image[m_x+i,m_y+j]*(.5 - (max(i,j)/100))  
                image[m_x-i,m_y+j] += image[m_x-i,m_y+j]*(.5 - (max(i,j)/100)) 
                image[m_x+i,m_y+j] += image[m_x+i,m_y+j]*(.5 - (max(i,j)/100)) 
            elif(i == 0):
                image[m_x+i,m_y-j] += image[m_x+i,m_y+j]*(.5 - (max(i,j)/100))  
                image[m_x+i,m_y+j] += image[m_x+i,m_y+j]*(.5 - (max(i,j)/100))
            elif(j == 0):
                image[m_x-i,m_y-j] += image[m_x-i,m_y-j]*(.5 - (max(i,j)/100)) 
                image[m_x+i,m_y-j] += image[m_x+i,m_y+j]*(.5 - (max(i,j)/100))  

    image = np.clip(image,0,255).astype('uint8')

    return image