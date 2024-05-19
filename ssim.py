import cv2
from skimage.metrics import structural_similarity as ssim


def ssim_compare(img1_path, img2_path) :
    #Read Image
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    #Convert image to grayscale
    img1 = cv2.cvtColor(img1 , cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)

    #print("Img1 Resolution:", img1.shape)
    #print("Img2 Resolution:", img2.shape) 

    #Check Image size and ratio
    ho, wo = img1.shape
    hc, wc = img2.shape
    ratio_orig = ho/wo
    ratio_comp = hc/wc
    dim = (wc, hc)
 
    #Resize Image Size
    img1 = cv2.resize(img1 , dim)
    img2 = cv2.resize(img2 , dim)
    #print("Img1 Res :", img1.shape)
    #print("Img2 Res :", img2.shape)

    #Main function of 
    if round(ratio_orig, 2) == round(ratio_comp, 2):
        ssim_score, dif = ssim(img1, img2, full=True,)
        return ssim_score

img1 = 'img1.png'
img2 = 'img5.png'
 
ssim_val = ssim_compare( img1, img2)
print("Similarity: ", ssim_val)
