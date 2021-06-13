from skimage import io
from skimage import transform
import Utils
from skimage import img_as_ubyte

image = io.imread('images.jpg')
x,y,ch = image.shape
transf_x = transform.EuclideanTransform(translation=(0.25*x,0))
im_x_tran = transform.warp(image, transf_x.inverse)
io.imsave('./Results/image_x_transform.jpg',img_as_ubyte(im_x_tran))
print('Saved Image transformed in x direction...')

transf_y = transform.EuclideanTransform(translation=(0,0.25*y))
im_y_tran = transform.warp(image, transf_y.inverse)
io.imsave('./Results/image_y_transform.jpg',img_as_ubyte(im_y_tran))
print('Saved Image transformed in y direction...')

im_y_90 = transform.rotate(image,90)
io.imsave('./Results/image_90_transform.jpg',img_as_ubyte(im_y_90))
print('Saved Image rotated at 90...')

im_y_m90 = transform.rotate(image,-90)
io.imsave('./Results/image_m90_transform.jpg',img_as_ubyte(im_y_m90))
print('Saved Image rotated at -90...')

grad_im = Utils.add_gradient(image)
io.imsave('./Results/grad_im.jpg',grad_im)
print('Saved Image with gradients...')