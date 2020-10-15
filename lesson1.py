from __future__ import print_function
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True,
                help='Path to the image')
args=vars(ap.parse_args())

image=cv2.imread(args['image'])
print('width: {} pixel'.format(image.shape[1]))
print('height: {} pixel'.format(image.shape[0]))
print('channels {}'.format(image.shape[2]))
print(image)


cv2.imshow('machine1', image)
cv2.waitKey(0)

cv2.imwrite('newmachine.jpg', image)
