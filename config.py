
# PROMOCODE = ["CAKE15","SWEET15","BIRTHDAY15"]

# DISCOUNT_RATE = 15

# DAY_LIFETIME_IN_SECONDS = 60

# result = 
import fpdf

data=[1,2,3,4,5,6]

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.output("testings.pdf")