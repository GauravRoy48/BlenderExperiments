from PIL import Image
import glob
import cv2
import os
import shutil

#%%
# Creating output directories 

def CheckCreatePath(path1, path2, path3):
    
    if not os.path.exists(path1):
        os.makedirs(path1)
    if not os.path.exists(path2):
        os.makedirs(path2)
    if not os.path.exists(path3):
        os.makedirs(path3)

#%%
## Rename Files

def NumPrefix(flag):
    if flag:
        for name in glob.glob(blender_out_path+'*'):
            if ".jp" in name or ".png" in name or ".mp4" in name or ".mkv" in name:
                shutil.copy(name, in_path)
        
        files_dates = []
        files_names = []

        for name in glob.glob(blender_out_path+'*'):
            if ".jp" in name or ".png" in name or ".mp4" in name or ".mkv" in name:
                files_names.append(name)
        
        
        for name in files_names:
            files_dates.append(os.path.getmtime(name))
        
        names = [x for _,x in sorted(zip(files_dates,files_names), reverse=True)]
        
        prefix = [str(x+1).zfill(len(str(len(names)))) for x in range(len(names))]
        
        for count,name in zip(prefix,names):
            path,filename = name.split('\\')
            os.rename(in_path+filename,in_path+count+"_"+filename)
    
    
        print('\n\nNumPrefix Complete.')
    else:
        print("NumPrefix disabled")


#%%
## Vids - Image

def VideoToImage(flag, frameCount, resol):
    if flag:
        vid_names = []

        for name in glob.glob(in_path+'*.m*'):
            vid_names.append(name)
        
        print('\nTotal Videos: '+str(len(vid_names))+'\n')
        
        count = 1
        for name in vid_names:
            if count%10 == 0:
                print("Working on Video "+str(count)+": "+name)
            count +=1
            vid = cv2.VideoCapture(name)
            namesplit = name.split('\\')
            out_name = namesplit[1].split('.')[0]+".png"
            curr_frame = 0
            while(True):
                ret, frame = vid.read()
                
                if ret:
                    
                    if curr_frame == frameCount:
                        cv2.imwrite(out_path2+out_name, frame)
                    elif curr_frame >frameCount:
                        break
                    
                    curr_frame+=1
                else:
                    break
            vid.release()
            cv2.destroyAllWindows()
            
            image = Image.open(out_path2+out_name)
            image.thumbnail((resol, resol))
            namesplit = name.split('\\')
            image.save(out_path2+out_name)
        print("Working on Image "+str(count-1)+": "+name)
    
        print('\n\nVideoToImage Complete.')

    else:
        print("VideoToImage disabled")

#%%
## Fulls - Images

def ChangeImgResol(flag, resol):
    if flag:
        img_names = []

        for name in glob.glob(in_path+'*'):
            if ".jp" in name or ".png" in name:
                img_names.append(name)
        
        print("Images: "+str(len(img_names)))
        
        print('\nTotal Images: '+str(len(img_names))+'\n')
        
        count = 1
        for name in img_names:
            if count%10 == 0:
                print("Working on Image "+str(count)+": "+name)
            count +=1
            image = Image.open(name)
            image.thumbnail((resol, resol))
            namesplit = name.split('\\')
            image.save(out_path2+namesplit[1])
        print("Working on Image "+str(count-1)+": "+name)
    
        print('\n\nChangeImgResol Complete.')
    else:
        print("ChangeImgResol disabled")

#%%
## Thumbnails - Images

def ImageToThumbnails(flag,resol):
    if flag:
        img_names = []
        
        for name in glob.glob(out_path2+'*'):
            if ".jp" in name or ".pn" in name:
                img_names.append(name)
        
        print("Images: "+str(len(img_names)))
        
        ## 
        
        print('\nTotal Images: '+str(len(img_names))+'\n')
        
        count = 1
        for name in img_names:
            if count%10 == 0:
                print("Working on Image "+str(count)+": "+name)
            count +=1
            image = Image.open(name)
            image.thumbnail((resol, resol))
            namesplit = name.split('\\')
            image.save(out_path1+namesplit[1])
        print("Working on Image "+str(count-1)+": "+name)
    
        print('\n\nImageToThumbnails Complete.')
    else:
        print("ImageToThumbnails disabled")

#%%
## Collect Paths
blender_out_path = "D:/Softwares/Blender/Output/"
in_path = "E:/Blender Github Repo/Orig/"
out_path1 = "E:/Blender Github Repo/thumbs/"
out_path2 = "E:/Blender Github Repo/fulls/"

full = 1080
thumb = 300
frame = 10
flag1 = True
flag2 = True


CheckCreatePath(in_path, out_path1, out_path2)
NumPrefix(flag1)
VideoToImage(flag2, frame, full)
ChangeImgResol(flag2, full)
ImageToThumbnails(flag2, thumb)

print('\a')