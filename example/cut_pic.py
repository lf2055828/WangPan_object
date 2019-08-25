import numpy as np
import os
import matplotlib.image as mpimg
from scipy import misc
from PIL import Image
def gene_cun_pic(x,y):
    k = 252
    for n in  range(1,x+1):
        file = str(n) + '.png'
        pepper_image_path = "W:\workspace\krlab_conv_segmentate/notpepper"
        p_image_path = os.path.join(pepper_image_path, file)
        p_pic = mpimg.imread(p_image_path)
        height,weight,chinal = np.asarray(p_pic).shape
        n_height = int(height/y)
        n_weight = int(weight/y)
        print(n_weight,n_height)
        for i in range(1,n_height+1):
            for j in range(1,n_weight+1):
                lena_new_sz = p_pic[28*(i-1):28*i,28*(j-1):28*j]
                k = k+1
                misc.imsave('W:\workspace\krlab_conv_segmentate\small_not_pepper_train/'+ str(k)+'.png', lena_new_sz)

# gene_cun_pic(12,28)#输入图片数量,剪裁大小

# generate notpepper lable
# k = 252
# for i in range(0,974):
#     a = np.zeros((28,28))
#     print(a)
#     k = k+1
#     misc.imsave('W:\workspace\krlab_conv_segmentate\small_not_pepper_lable/' + str(k)+'.png', a)
# generate notpepper lable

#generate test pics
pepper_image_path = "W:\workspace\krlab_conv_segmentate\originaldata.bmp"
# p_pic = Image.open(pepper_image_path)

p_pic = mpimg.imread(pepper_image_path)
height,weight,chinal = np.asarray(p_pic).shape
n_height = int(height/28)
n_weight = int(weight/28)
print(n_weight,n_height)
k = 0
for i in range(1,n_height+1):
    for j in range(1,n_weight+1):
        lena_new_sz = p_pic[28*(i-1):28*i,28*(j-1):28*j]
        # lena_new_sz[lena_new_sz<0.9]=0
        # lena_new_sz[lena_new_sz > 0.9] = 1
        k = k+1
        print(k)
        print(lena_new_sz)
        misc.imsave('W:\workspace\krlab_conv_segmentate/test_image/'+str(k)+'.png', lena_new_sz)

