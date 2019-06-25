# see :
#  https://processing.org/reference/ellipseMode_.html
add_library("sound")





g_x =400
g_y =400
g_vx = 5
g_vy = 5
g_dia = 50
count = 0
col = 255


def setup():
    size(800,600)
    global f,scrash,sbase
    
    f = createFont("Arial",36, True)
    textFont(f,36)
    scrash = SoundFile(this,"scrash.wav")
    sbase = SoundFile(this,"sbase.wav")
  
    print("chanels ",scrash.channels(), " with duration : ", scrash.duration())
    #scrash.play()
    
    
def mouseClicked():
    global f,scrash,sbase
    
    print("mouse Clicked")
    
def draw():
    global g_x,g_y,g_vx,g_vy,g_dia,count,f,col
    background(0)
    ellipseMode(CORNER)
    fill(255)
    rect(width- width*.1 , mouseY,50,50)

    if g_x+g_dia>=width or g_x<=0:
        g_vx *= -1
  
    if g_x<=0:
        sbase.play()  
        
        
    if g_x+g_dia >= width:
        count +=1
        col = 0
        scrash.play()
            
    if g_y+g_dia >= height or g_y<=0:
        g_vy *= -1
        sbase.play()
        
    if inter(width- width*.1 , mouseY,50,50,g_x,g_y,g_dia,g_dia):
        g_vx *= -1
        g_vy *= -1
        sbase.play()

    
    col +=5
    if col>255:
        col = 255   
         
    fill(255,col,col)    
    s = "Score: "+str(count)
    text(s, width- len(s)*2 -width*.2 ,height *.1)
    g_x +=g_vx
    g_y +=g_vy 

    
    fill(random(255),random(255),255)
    ellipse(g_x,g_y,g_dia,g_dia)
    

    
        

def inter(x1,y1,w1,h1,x2,y2,w2,h2):
    
    if x1+w1 >= x2 and x1 <= x2+w2:
        if y1<= y2+h2 and y1+h1 >= y2:
            return True
    
    return False
