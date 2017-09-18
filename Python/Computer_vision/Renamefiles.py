import os
import shutil


path = '.'
filenames=os.listdir('.')


for filename in filenames:
    just_filename, extension = os.path.splitext(filename)
    if filename.endswith(".jpg"):
        resize_filename = os.path.join(path, filename)
        newdir = r'C:\Users\chris\Desktop\OneDrive\GitHub\GitHub\Projects\Python\Computer_vision\Edit_Pix'
        print(resize_filename)
        i=1
        just_filename = os.path.join(newdir, "%s%d%s" %(just_filename, i, extension))
        print(just_filename)
        while os.path.isfile(just_filename):
            i += 1
            just_filename = os.pathjoin(newdir, "%s%d%s" %(just_filename, i, extension))
            for image in just_filename:
                img=cv2.imread(image,0)
                rsize=cv2.resize(img,(100,100))
                cv2.imshow("Hi There",rsize)
                cv2.waitKey(500)
                cv2.destroyAllWindows()
        shutil.copy(os.path.join(path, filename), just_filename)
