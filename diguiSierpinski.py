#sierpinski triangle
import turtle
def drawTriangle(points,color,myturtle):
	myturtle.fillcolor(color)
	myturtle.up()
	myturtle.goto(points[0][0],points[0][1])
	myturtle.down()
	myturtle.begin_fill()
	myturtle.goto(points[1][0],points[1][1])
	myturtle.goto(points[2][0],points[2][1])
	myturtle.goto(points[0][0],points[0][1])
	myturtle.end_fill()
	
def getMid(p1,p2):
	return ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
	
def sierpinski(points,degree,myturtle):
	colormap=['blue','red','green','white','yellow','violet','orange']
	drawTriangle(points,colormap[degree],myturtle)
	if degree>0:
		sierpinski([points[0],getMid(points[0],points[1]),getMid(points[0],points[2])],degree-1,myturtle)
		sierpinski([points[1],getMid(points[0],points[1]),getMid(points[1],points[2])],degree-1,myturtle)
		sierpinski([points[2],getMid(points[2],points[1]),getMid(points[0],points[2])],degree-1,myturtle)
def main():
	myturtle=turtle.Turtle()
	mywin=turtle.Screen()
	mypoints=[[-100,-50],[0,100],[100,-50]]
	sierpinski(mypoints,3,myturtle)
	mywin.exitonclick()
	
main()