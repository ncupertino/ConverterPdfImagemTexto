from pdf2image import convert_from_path
import pytesseract
import cv2


#
#It is necessary to install the poppler to convert pdf into image
#

class Extrair:

  def Converter_Pdf_Imagem(path): #path of the pdf file
    pages = convert_from_path(path,500)


    out_path = '/Users/Downloads/out.jpg' #output file

    for page in pages:
        page.save(out_path, 'JPEG')


    path = Extrair.OtimizarImagemPdf(out_path)

    novo_texto = Extrair.ConverterImagemText(path)

    print(novo_texto)

    texto = Extrair.ConverterImagemText(out_path)


    return texto

  
  def OtimizarImagemPdf(path):
    img = cv2.imread(path, 0)

    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    #th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    #                     cv2.THRESH_BINARY, 11, 2)

    #ret, thresh_img = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)

    cv2.imshow('grey image', th3)
    
    
    path = '/Users/Downloads/result11.jpg'

    cv2.imwrite(path, th3)
    return path
    
    
  def ConverterImagemText(path):



    #If Windows runs the tesseract directory
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

    imagem_text = pytesseract.image_to_string(Image.open(path))

    #print(imagem_text)  # Extraindo o texto da imagem

    return imagem_text
