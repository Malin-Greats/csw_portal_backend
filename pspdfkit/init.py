import cv2
import numpy as np
from PIL import ImageFont,ImageDraw,Image
import os
import pandas as pd
from django.conf import settings
# DRIVER CODE FOR DELETING OLD CERRTIFICATES
# USEFUL FOR TESTING 
def clean():
       x=input("enter folder name to clean: ")
       print("Cleaning {} folder ........".format(str(x)))
       for certificates in os.listdir("result/{}/".format(str(x))):
        os.remove("result/{}/{}".format(str(x),certificates))
       print("completed.......")

# FOR READING FROM TEXT FILE
def open_textfile():
    file=open("names.txt",'r')
    name_ls=file.read().split('\n')
    return name_ls

'''
GENERATION USING PILLOW MODULE
'''
def single_certificate_gen(name):
    certificates_path = os.path.join(settings.MEDIA_ROOT, 'certificates')
    config_certificates_path = os.path.join(certificates_path, 'config')

    signatures_certificates_path = os.path.join(config_certificates_path, 'signatures')
    fonts_certificates_path = os.path.join(config_certificates_path,'fonts')

    members_certificates_path = os.path.join(settings.MEDIA_ROOT, 'certificates', 'members')
    cert_frame = os.path.join(signatures_certificates_path, 'cert frame.png')

    template=cv2.imread(cert_frame)
    certificate_name = "{}.jpg".format(name)
    '''
    When the image file is read with the OpenCV function imread(), the order of colors is BGR (blue, green, red),
    but where as in Pillow, the order of colors is assumed to be RGB (red, green, blue) (ik its bullshit)
    So..if you want to use both the Pillow function and the OpenCV function,
    you need to convert BGR and RGB.
    '''
    
    print("certificates_path cert frame.template')")
    print(cert_frame)
    print("in function 'cvtColor'")
    print(template)
    print(cv2.COLOR_BGR2RGB)
    template_conv = cv2.cvtColor(template,cv2.COLOR_BGR2RGB)
    arr_img= Image.fromarray(template_conv)
    var_draw=ImageDraw.Draw(arr_img)
    pacifico=ImageFont.truetype(os.path.join(fonts_certificates_path,"Pacifico.ttf"),90)
    sofia_regular = ImageFont.truetype(os.path.join(fonts_certificates_path,"Sofia-Regular.otf"), 20) # CAN IMPLEMENT MORE THAN ONE FONT      
    var_draw.text((650,500),name,font=pacifico,fill='grey') # DEFINING CO-ORDS NAME AND FONT-COLOR
    # var_draw.text((380,950),name,font=pacifico,fill='grey') # DEFINING CO-ORDS NAME AND FONT-COLOR
    final_res=cv2.cvtColor(np.array(arr_img),cv2.COLOR_RGB2BGR) # RE-CONVERTING IMAGE FROM ARRAY INFO
    cv2.imwrite(os.path.join(members_certificates_path, certificate_name), final_res) # TO SAVE THE FINAL OUTPUT

    #Append Signatures
    
    certificate = Image.open(os.path.join(members_certificates_path,certificate_name))
    certificatecopy = certificate.copy()
    Signature = Image.open(os.path.join(signatures_certificates_path, 'mrgreats_signature.png'))
    Signaturecopy = Signature.copy()
    
    # paste image giving dimensions
    certificatecopy.paste(Signaturecopy, (400,980))
    
    # save the image
    certificate_upload_url = 'certificates/members/'
    certificatecopy.save(os.path.join(members_certificates_path,certificate_name))
    generated_certificate = os.path.join(members_certificates_path,certificate_name)
    print("{}'s certificate generated using PILLOW".format(name))
    if generated_certificate:
        generated_certificate_path = certificate_upload_url + certificate_name
        return generated_certificate_path

def pillow(name_ls):
   # MAIN CODE FOR GENERTING CERTIFICATES
    def certificate_gen(name_ls):
        for name in name_ls:
            template=cv2.imread('cert frame.png')
            '''
            When the image file is read with the OpenCV function imread(), the order of colors is BGR (blue, green, red),
            but where as in Pillow, the order of colors is assumed to be RGB (red, green, blue) (ik its bullshit)
            So..if you want to use both the Pillow function and the OpenCV function,
            you need to convert BGR and RGB.
            '''
            print('name')
            print(name)
            name1 = name + '2'
            template_conv = cv2.cvtColor(template,cv2.COLOR_BGR2RGB)
            arr_img= Image.fromarray(template_conv)
            var_draw=ImageDraw.Draw(arr_img)
            pacifico=ImageFont.truetype("fonts/Pacifico.ttf",90)
            sofia_regular = ImageFont.truetype("fonts/Sofia-Regular.otf", 20) # CAN IMPLEMENT MORE THAN ONE FONT
            if len(name) < 25:
                var_draw.text((750,500),name,font=pacifico,fill='grey') # DEFINING CO-ORDS NAME AND FONT-COLOR
            else:
                var_draw.text((650,500),name,font=pacifico,fill='grey') # DEFINING CO-ORDS NAME AND FONT-COLOR
            # var_draw.text((380,950),name,font=pacifico,fill='grey') # DEFINING CO-ORDS NAME AND FONT-COLOR
            final_res=cv2.cvtColor(np.array(arr_img),cv2.COLOR_RGB2BGR) # RE-CONVERTING IMAGE FROM ARRAY INFO
            cv2.imwrite(os.path.join(fonts_certificates_path,"{}.jpg".format(name)), final_res) # TO SAVE THE FINAL OUTPUT

            certificate = Image.open(os.path.join(fonts_certificates_path,"{}.jpg".format(name)))
            certificatecopy = certificate.copy()
            Signature = Image.open('result/signatures/mrgreats_signature.png')
            Signaturecopy = Signature.copy()
            
            # paste image giving dimensions
            certificatecopy.paste(Signaturecopy, (400,980))
            
            # save the image
            certificatecopy.save(os.path.join(fonts_certificates_path,"{}.jpg".format(name)))
            print("{}'s certificate generated using PILLOW".format(name))
    open_textfile()
    certificate_gen(name_ls)
'''
GENERATION USING cv2 MODULE
'''
def cv_2(name_ls):
    for name in name_ls:
      template=cv2.imread('certificate.jpg')
      # Syntax: cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
      cv2.putText(template, name.strip(),(1123,795),cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 4, (128, 128, 128), 10)
      cv2.imwrite("result/cv2/{}.jpg".format(name.strip()),template)
      print("{}'s certificate generated using Open cv".format(name))
      