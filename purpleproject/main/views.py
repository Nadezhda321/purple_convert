from django.conf.global_settings import STATIC_ROOT
from django.shortcuts import render
from .forms import FotoForm
from .models import Foto
from django.http import HttpResponse
import pytesseract
import cv2
import lzma
import argparse
import numpy
from .models import FileServ


def main(request):
    form = FotoForm()
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'img' in request.FILES:
                # photo = request.FILES['img']
                # print(photo)
                form.img = request.FILES['img']
                form.save(commit=True)
                return render(request, 'main/final.html')
                # return HttpResponse('image upload success')

                ap = argparse.ArgumentParser()
                ap.add_argument("-i", "--image", required=True, help="path to input image")
                args = vars(ap.parse_args())
                image = cv2.imread(args["image"], cv2.IMREAD_GRAYSCALE)
                ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)


                pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

                # читать изображение с помощью OpenCV
                img = cv2.imread(thresh)
                img = cv2.GaussianBlur(img, (9, 9), 0)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                # получаем строку
                string = pytesseract.image_to_string(img)
                print(string)
                # записываем текст в файл
                f = open('text.txt', 'w')
                f.write(string)
                f.close()

                lzc = lzma.LZMACompressor()

                filename_in = "text.txt"
                filename_out = "textfoto.xz"

                with open(filename_in) as fin:
                    with open(filename_out, "wb") as fout:
                        for chunk in fin.read(1024):
                            compd_chunk = lzc.compress(chunk.encode("utf-8"))
                            fout.write(compd_chunk)
                        fout.write(lzc.flush())
        else:
            print(form.errors)
    return render(request, 'main/index.html', {'form': form})

def final(request):
    return render(request, 'main/final.html')




