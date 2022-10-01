# -*- coding: utf-8 -*-
import pygame
import math

"""
Created on Sun Sep 25 16:38:06 2022
1.	Create a Paint-like drawing software that allows users to:
•	Draw line segments, triangles, rectangles, ellipse/circles, and Bezier curves.
•	Zoom in and out of the drawing areas
2.	Give your software a name. Create a readme file that contains documentation on how to use the software
3.	Bonus credits (10 points): Develop a mechanism to allow the users 
to save the pictures they created by your software.

@author: liana
"""

pygame.init()
print("Initializing Programe")
black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Mid Term Piant Project")
clock = pygame.time.Clock()
    
def point(pX, pY, pWidth, pHeight, pColor):
    pygame.draw.rect(gameDisplay, pColor, [pX, pY, pWidth, pHeight])
    
def game_loop():
    gameExit = False
    
    print("Inside game_loop")
    scaleP = 3
    scale = 1                                                             
    scale_change = 0
    scaleP_change = 0
    mouse_pos = 0
    mouse_pos_point = []
    mouse_pos_line = []
    mouse_pos_circle = []
    mouse_pos_square = []
    mouse_pos_bezierCurve = []
    mouse_pos_triangle = []
    points = False
    line = False
    circle = False
    square = False
    bezierCurve = False
    triangle = False
    save = False
    
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:# Left and right
                    points = True
                    line = False
                    circle = False
                    square = False
                    bezierCurve = False
                    triangle = False
                if event.key == pygame.K_2:
                    points = False
                    line = True
                    circle = False
                    square = False
                    bezierCurve = False
                    triangle = False
                if event.key == pygame.K_3:
                    points = False
                    line = False
                    circle = True
                    square = False
                    bezierCurve = False
                    triangle = False
                if event.key == pygame.K_4:
                    points = False
                    line = False
                    circle = False
                    square = True
                    bezierCurve = False
                    triangle = False
                if event.key == pygame.K_5:
                    points = False
                    line = False
                    circle = False
                    square = False
                    bezierCurve = True
                    triangle = False
                if event.key == pygame.K_6:
                    points = False
                    line = False
                    circle = False
                    square = False
                    bezierCurve = False
                    triangle = True
                if event.key == pygame.K_s:
                    save = True
               
                if event.key == pygame.K_UP:
                    scale_change = 1
                if event.key == pygame.K_DOWN:
                    scale_change = -1
                if event.key == pygame.K_RIGHT:
                    scaleP_change = 1
                if event.key == pygame.K_LEFT:
                    scaleP_change = -1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_s:
                    scale_change = 0
                    scaleP_change = 0
                    save = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:#if there a click get the coordinates
                mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:#Once click is release stop
                mouse_pos = 0
                
        if mouse_pos != 0 and points:#this stops the mouse pos from being put into x and y when 0
            print("point")
            mouse_pos_point.append(mouse_pos) 
            mouse_pos = 0
        
        if mouse_pos != 0 and line:
            mouse_pos_line.append(mouse_pos) 
            mouse_pos = 0
        if mouse_pos != 0 and circle:
            mouse_pos_circle.append(mouse_pos) 
            mouse_pos = 0
        if mouse_pos != 0 and square:
            mouse_pos_square.append(mouse_pos) 
            mouse_pos = 0
        if mouse_pos != 0 and bezierCurve:
            mouse_pos_bezierCurve.append(mouse_pos) 
            mouse_pos = 0
        if mouse_pos != 0 and triangle:
            mouse_pos_triangle.append(mouse_pos) 
            mouse_pos = 0
                
        if scaleP + (scaleP_change *.1) > 1.99:
            scaleP = scaleP + (scaleP_change *.1)
        if scale + (scale_change *.01) > .99:
            scale = scale + (scale_change *.01)
        
            

        gameDisplay.fill(white)
        
        #Triangle
        if len(mouse_pos_triangle)%2==0 :
            pos = len(mouse_pos_triangle)/2
            i = len(mouse_pos_triangle)
            
            while pos > 0:
                x1,y1 = mouse_pos_triangle[i-2]
                x2,y2 = mouse_pos_triangle[i-1]
                d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))#this is length
                #below is how am getting the third points to complete the triangle
                x0 = (d/2) + math.cos(x1+x2) + x2/2
                y0 = d - math.sin(y1)
                x0 = x0 * scale
                y0 = y0 * scale
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                t_begin = 0
                t_end = 1
                sT_end = t_end 
                sT = t_begin
        
                while sT <= sT_end:
                    
                    #part 1 of getting the triangle
                    xQ0 = (1-sT) * x2 + sT * x1 
                    yQ0 = (1-sT) * y2 + sT * y1
            
                    point(xQ0, yQ0, scaleP, scaleP, black)
            
                    #part 2 of getting the triangle
                    xQ1 = (1-sT) * x0 + sT * x2
                    yQ1 = (1-sT) * y0 + sT * y2
            
                    point(xQ1, yQ1, scaleP, scaleP, black)
            
                    #part 3 of getting the triangle
                    xQ3 = (1-sT) * x1 + sT * x0
                    yQ3 = (1-sT) * y1 + sT * y0
            
                    point(xQ3, yQ3, scaleP, scaleP, black)
            
                    sT = sT + 0.001
                pos = pos - 1
                i = i - 2
        else:
            pos = (len(mouse_pos_triangle)/2)-1
            i = len(mouse_pos_triangle)-1
            
            while pos > 0:
                x1,y1 = mouse_pos_triangle[i-2]
                x2,y2 = mouse_pos_triangle[i-1]
                d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))#this is length
                #below is how am getting the third points to complete the triangle
                x0 = (d/2) + math.cos(x1+x2) + x2/2
                y0 = d - math.sin(y1)
                x0 = x0 * scale
                y0 = y0 * scale
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                t_begin = 0
                t_end = 1
                sT_end = t_end 
                sT = t_begin
        
                while sT <= sT_end:
                    
                    #part 1 of getting the triangle
                    xQ0 = (1-sT) * x2 + sT * x1 
                    yQ0 = (1-sT) * y2 + sT * y1
            
                    point(xQ0, yQ0, scaleP, scaleP, black)
            
                    #part 2 of getting the triangle
                    xQ1 = (1-sT) * x0 + sT * x2
                    yQ1 = (1-sT) * y0 + sT * y2
            
                    point(xQ1, yQ1, scaleP, scaleP, black)
            
                    #part 3 of getting the triangle
                    xQ3 = (1-sT) * x1 + sT * x0
                    yQ3 = (1-sT) * y1 + sT * y0
            
                    point(xQ3, yQ3, scaleP, scaleP, black)
            
                    sT = sT + 0.001
                pos = pos - 1
                i = i - 2
        
        #Bezeir curve
        if len(mouse_pos_bezierCurve)%2==0 :
            pos = len(mouse_pos_bezierCurve)/2
            i = len(mouse_pos_bezierCurve)
            
            while pos > 0:
                x1,y1 = mouse_pos_bezierCurve[i-2]
                x2,y2 = mouse_pos_bezierCurve[i-1]
                d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))#this is length
                #below is how am getting the third points to complete the triangle
                x0 = (d/2) + math.cos(x1+x2) + x2/2
                y0 = d - math.sin(y1)
                x0 = x0 * scale
                y0 = y0 * scale
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                t_begin = 0
                t_end = 1
                sT_end = t_end 
                sT = t_begin
        
                while sT <= sT_end:
                    
                    #part 1 of getting the bezeir curve
                    xQ0 = (1-sT) * x1 + sT * x0 
                    yQ0 = (1-sT) * y1 + sT * y0
            
                    #part 2 of getting the bezeir curve
                    xQ1 = (1-sT) * x0 + sT * x2
                    yQ1 = (1-sT) * y0 + sT * y2
            
                    #part 3of getting the bezeir curve
                    xC0 = (1-sT) * xQ0 + sT * xQ1
                    yC0 = (1-sT) * yQ0 + sT * yQ1
            
            
            
                    point(xC0, yC0, scaleP, scaleP, black)
            
                    sT = sT + 0.001
                pos = pos - 1
                i = i - 2
        else:
            pos = (len(mouse_pos_bezierCurve)/2)-1
            i = len(mouse_pos_bezierCurve)-1
            
            while pos > 0:
                x1,y1 = mouse_pos_bezierCurve[i-2]
                x2,y2 = mouse_pos_bezierCurve[i-1]
                d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))#this is length
                #below is how am getting the third points to complete the triangle
                x0 = (d/2) + math.cos(x1+x2) + x2/2
                y0 = d - math.sin(y1)
                x0 = x0 * scale
                y0 = y0 * scale
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                t_begin = 0
                t_end = 1
                sT_end = t_end 
                sT = t_begin
        
                while sT <= sT_end:
                    
                    #part 1 of getting the bezeir curve
                    xQ0 = (1-sT) * x1 + sT * x0 
                    yQ0 = (1-sT) * y1 + sT * y0
            
                    #part 2 of getting the bezeir curve
                    xQ1 = (1-sT) * x0 + sT * x2
                    yQ1 = (1-sT) * y0 + sT * y2
            
                    #part 3of getting the bezeir curve
                    xC0 = (1-sT) * xQ0 + sT * xQ1
                    yC0 = (1-sT) * yQ0 + sT * yQ1
            
            
            
                    point(xC0, yC0, scaleP, scaleP, black)
            
                    sT = sT + 0.001
                pos = pos - 1
                i = i - 2
        
        
        # Square
        if len(mouse_pos_square)%2==0 :
            pos = len(mouse_pos_square)/2
            i = len(mouse_pos_square)
            
            while pos > 0:
                x1,y1 = mouse_pos_square[i-2]
                x2,y2 = mouse_pos_square[i-1]
                
               
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
        
                t_begin = 0
                t_end = 1
                sT_end = t_end 
                sT = t_begin
        
                while sT <= sT_end:
                    
                    xQ1 = (1-sT) * x2 + sT * x1
                    yQ1 =  y2 
            
                    point(xQ1, yQ1, scaleP, scaleP, black)
            
                    xQ2 = (1-sT) * x2 + sT * x1
                    yQ2 =  y1
            
                    point(xQ2, yQ2, scaleP, scaleP, black)
            
                    xQ3 =  x1
                    yQ3 = (1-sT) * y2 + sT * y1
            
                    point(xQ3, yQ3, scaleP, scaleP, black)
            
                    xQ4 =  x2 
                    yQ4 = (1-sT) * y2 + sT * y1
            
                    point(xQ4, yQ4, scaleP, scaleP, black)
                    sT = sT + 0.001
                pos = pos -1
                i = i-2
                
        else:
            pos = (len(mouse_pos_square)/2)-1
            i = len(mouse_pos_square)-1
            
            while pos > 0:
                x1,y1 = mouse_pos_square[i-2]
                x2,y2 = mouse_pos_square[i-1]
                
               
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
        
                t_begin = 0
                t_end = 1
                sT_end = t_end 
                sT = t_begin
        
                while sT <= sT_end:
                    
                    xQ1 = (1-sT) * x2 + sT * x1
                    yQ1 =  y2 
            
                    point(xQ1, yQ1, scaleP, scaleP, black)
            
                    xQ2 = (1-sT) * x2 + sT * x1
                    yQ2 =  y1
            
                    point(xQ2, yQ2, scaleP, scaleP, black)
            
                    xQ3 =  x1
                    yQ3 = (1-sT) * y2 + sT * y1
            
                    point(xQ3, yQ3, scaleP, scaleP, black)
            
                    xQ4 =  x2 
                    yQ4 = (1-sT) * y2 + sT * y1
            
                    point(xQ4, yQ4, scaleP, scaleP, black)
                    sT = sT + 0.001
                pos = pos -1
                i = i-2
        
        #Circle
        if len(mouse_pos_circle)%2==0 :
            pos = len(mouse_pos_circle)/2
            i = len(mouse_pos_circle)
            while pos > 0:
                x1,y1 = mouse_pos_circle[i-2]
                x2,y2 = mouse_pos_circle[i-1]
                
                
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                
                d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
                d = d
                t_begin = 0
                t_end = 2 * math.pi
                sT_begin = t_begin 
                sT_end = t_end 
                sT = sT_begin  
                while sT <= sT_end:
                    t = sT
                    x = (d) * math.cos(t) 
                    y = (d) * math.sin(t) 
                    px = x + x2
                    py = y2-y 
                    point(px, py, scaleP, scaleP, black)
                    sT = sT + 0.001
                pos = pos -1
                i = i-2
        else:
            pos = (len(mouse_pos_circle)/2)-1
            i = len(mouse_pos_circle)-1
            while pos > 0:
                x1,y1 = mouse_pos_circle[i-2]
                x2,y2 = mouse_pos_circle[i-1]
                
                
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                
                d = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
                d = d
                t_begin = 0
                t_end = 2 * math.pi
                sT_begin = t_begin 
                sT_end = t_end 
                sT = sT_begin  
                while sT <= sT_end:
                    t = sT
                    x = (d) * math.cos(t) 
                    y = (d) * math.sin(t) 
                    px = x + x2
                    py = y2-y 
                    point(px, py, scaleP, scaleP, black)
                    sT = sT + 0.001
                pos = pos -1
                i = i-2
        
        #Line
        
        if len(mouse_pos_line)%2==0 :
            pos = len(mouse_pos_line)/2
            i = len(mouse_pos_line)
            
            while pos > 0:
                x1,y1 = mouse_pos_line[i-2]
                x2,y2 = mouse_pos_line[i-1]
                
                
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                
                t_begin = 0
                t_end = 1
                sT_begin = t_begin 
                sT_end = t_end
                sT = t_begin
                while sT <= sT_end:
                    t = sT 
                    
                    x = (1-t) * x1 + t * x2
                    y = (1-t) * y1 + t * y2
                    
                    point(x, y, scaleP, scaleP, black)
                    sT = sT + 0.001
                pos = pos - 1
                i = i - 2         
        else:
            pos = (len(mouse_pos_line)/2)-1
            i = len(mouse_pos_line)-1
            
            while pos > 0:
                x1,y1 = mouse_pos_line[i-2]
                x2,y2 = mouse_pos_line[i-1]
                
                
                x1 = x1 * scale
                x2 = x2 * scale
                y1 = y1 * scale
                y2 = y2 * scale
                
                t_begin = 0
                t_end = 1
                sT_begin = t_begin 
                sT_end = t_end
                sT = t_begin
                while sT <= sT_end:
                    t = sT 
                    
                    x = (1-t) * x1 + t * x2
                    y = (1-t) * y1 + t * y2
                    
                    point(x, y, scaleP, scaleP, black)
                    sT = sT + 0.001
                pos = pos - 1
                i = i - 2
                
        #Point
        
        for pos in range(len(mouse_pos_point)):
            x, y = mouse_pos_point[pos-1]
            
            
            x = x * scale
            y = y * scale
            
            point(x, y, scaleP, scaleP, black)# point on
            
        if save:
            pygame.image.save(gameDisplay, "Mid-Term_Dawning.png")
        
        pygame.display.update()
        clock.tick(60)
        
game_loop()
print("Program ended")
pygame.quit()