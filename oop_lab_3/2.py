
class PDFs:
  def set_pdf_details(self,creator,dis,size):
    self.creator = creator
    self.dis = dis
    self.size = size
  def get_pdf_details(self):
    print("Creator - ",self.creator,"\nDiscription - ",self.dis,"\nFile size - ",self.size)
 
class document(PDFs):
  def Pictures(self,creator,dis,size):
    self.creator = creator
    self.dis = dis
    self.dimension = []
    for i in range(2):
      a = int(input("Enter the dimension - "))
      self.dimension.append(a)
    self.size = size
  def pdf(self,creator,dis,size):
    PDFs.set_pdf_details(self,creator,dis,size)
  def check_size(self):
    if self.size >= 500:
      print("Please upload the document of size less than 500 KB")
    else:
      print("Document is uploaded")
  def display_pdfs(self):
    super().get_pdf_details()
  def display_pictures(self):
      print("Creator - ",self.creator,"\nDiscription - ",self.dis,"\nDimensions - ",self.dimension,"\nFile size - ",self.size)
  def checkdimension(self):
    for i in range(2):
      if self.dimension[i] >= 1000:
        print("Please upload picture with dimension 1000 X 1000 pixels or less")
        break
      else:
        print("Picture dimension is accepted")
 
d1 = document()
d1.Pictures("tushar","image",670)
d1.pdf("tushar","image",670)
d1.display_pdfs()
d1.display_pictures()
d1.check_size()
d1.checkdimension()