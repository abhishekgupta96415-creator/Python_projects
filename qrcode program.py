import qrcode 
a = "upi://pay?pa=9236961246@ybl"
b = qrcode.make(a)
b.save("abhishek.png")
print("QR CODE CREATED ")