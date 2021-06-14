import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy
#load the trained model to classify sign
from tensorflow.keras.models import load_model
model = load_model('traffic_classifier.h5')

#dictionary to label all traffic signs class.

#English Dictionary is written below 

classes = { 1:'ကီလို ၂၀ထက် ပိုမမောင်းရ',
            2:'ကီလို ၃၀ထက် ပိုမမောင်းရ', 
            3:'ကီလို ၅၀ထက် ပိုမမောင်းရ', 
            4:'ကီလို ၆၀ထက် ပိုမမောင်းရ', 
            5:'ကီလို ၇၀ထက် ပိုမမောင်းရ', 
            6:'ကီလို ၈၀ထက် ပိုမမောင်းရ', 
            7:'End of speed limit (80km/h)', 
            8:'ကီလို ၁၀၀ထက် ပိုမမောင်းရ', 
            9:'ကီလို ၁၂၀ထက် ပိုမမောင်းရ', 
            10:'ကျော်မတက်ရ', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'ရှေ့တွင်ဆုံမည့် ယဉ်ကြောများကို ဦးစားပေးရန်', 
            15:'ရပ်ပါ ', 
            16:'မော်တော်ကား မဝင်ရ', 
            17:'Veh > 3.5 tons prohibited', 
            18:'မည်သည့်ယာဉ်မျှ မဝင်ရ', 
            19:'ရှေ့တွင် အန္တရာယ်ရှိသည်', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'ရှေ့တွင် လမ်းကြမ်းရှိသည်', 
            24:'ရှေ့တွင် လမ်းချော်သည်', 
            25:'Road narrows on the right', 
            26:'ရှေ့တွင်လမ်းပြင်နေသည်', 
            27:'ရှေ့တွင် မီးပွိုင့်ရှိသည်', 
            28:'Pedestrians', 
            29:'ရှေ့တွင် ကျောင်းရှိသည်', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'လက်ယာဘက်သို့ ကွေ့ရန်', 
            35:'လက်ဝဲဘက်သို့ ကွေ့ရန်', 
            36:'ရှေ့တွင်တစ်လမ်းမောင်း ရှိသည်', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'အဝိုင်းပတ်တွင် လက်ယာဘက်မှစပြီးပတ်မောင်းရမည်', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

'''classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' } '''
#initialise GUI
root=tk.Tk()
root.geometry('800x600')
root.title('Traffic sign classification')
root.configure(background='#000000')

label=Label(root,background='#000000', font=('arial',15,'bold'))
sign_image = Label(root)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    pred = model.predict_classes([image])[0]
    sign = classes[pred+1]
    print(sign)
    label.configure(foreground='#ffffff',background = '#000000', text= sign , font =  ('small fonts', 20, 'bold'),borderwidth = 10) 
#02e315
def show_classify_button(file_path):
    classify_b=Button(root,text="Classify!! ",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#000000', foreground='#ffffff',font=('fixedsys',18), borderwidth = 0)
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((root.winfo_width()),(root.winfo_height())))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im , background = '#000000',foreground = '#ffffff', borderwidth = 1)
        sign_image.image=im
        label.configure(text='',background = '#000000' )
        show_classify_button(file_path)
    except:
        pass

photo_upload = ImageTk.PhotoImage(file = 'upload.png')

upload=Button(root,image = photo_upload, padx=10,pady=5, command=upload_image)
upload.configure(background='#000000', height = 40 , width = 210, borderwidth = 0 )

upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)

photo_head = cv2.imread('tsc.png')
photo_head = ImageTk.PhotoImage(file = 'tsc.png')



label.pack(side=BOTTOM,expand=True)
heading = Label(root, image = photo_head,pady=40, background = '#000000' )
heading.configure(height = 120, width = 700 , borderwidth = 0 )
heading.pack(pady = 20)
root.mainloop()