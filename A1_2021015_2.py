n=(int(input("Enter the number of students: ")))
pi=3.14
for i in range (n):                             # running the loop only for n students and asking each student for 2d or 3d
    print(f'''\nWhat is your shape type for student no. {i+1}? 
    1. 2d
    2. 3d
    3. quit''')
    
    geo=input()                     #input is taken as string instead of int to give user to input in various formats
    if geo=='1' or geo=='2d' or geo=='2D':
        print('''Great! You selected 2D Geometry. Kindly select the shape from the following menu
        1. square
        2. rectangle
        3. rhombus
        4. parallelogram
        5. circle''')
        shape=input()

        if shape=='1' or shape=='square':                           #formula square
            s=float(input("Enter the side length of square:"))
            print("\n1.Perimeter of this square is", 4*s)
            print("2.Area of this square is", s*s)
        
        elif shape=='2' or shape=='rectangle':                         #formula rectangle
            l=float(input("Enter the length of rectangle:"))
            b=float(input("Enter the breadth of rectangle:"))
            print("\n1.Perimeter of this rectangle is", 2*(l+b))
            print(".Area of this rectangle is", l*b)
        
        elif shape=='3' or shape=='rhombus':                               #formula rhombus
            s=float(input("Enter the side length of rhombus:"))
            d1=float(input("Enter the 1st diagonal of rhombus(D1):"))
            d2=float(input("Enter the 2nd diagonal of rhombus(D2):"))
            print("\n1.Perimeter of this rhombus is", 4*l)
            print("2.Area of this rhombus is", (d1*d2)/2)
        
        elif shape=='4' or shape=='parallelogram':                       #formula parallelogram
            l=float(input("Enter the length of parallelogram:"))
            b=float(input("Enter the breadth of parallelogram:"))
            h=float(input("Enter the height of parallelogram:"))
            print("\n1.Perimeter of this parallelogram is", 2*(l+b))
            print("2.Area of this parallelogram is", b*h)
        
        elif shape=='5' or shape=='circle':                                #formula circle
            r=float(input("Enter the radius of circle:"))
            print("\n1.Perimeter of this circle is", 2*pi*r)
            print("2.Area of this circle is", pi*r*r)
        
        else:
            print("WRONG INPUT!! Please enter correct input")
    
    
    if geo=='2' or geo=='3d' or geo=='3D':                             #shape type
        print('''Great! You selected 2D Geometry. Kindly select the shape from the following menu
        1. cube
        2. cuboid
        3. right circular cone
        4. hemisphere
        5. sphere
        6. solid cylinder
        7. hollow cylinder''')
        shape=input()

        if shape=='1' or shape=='cube':
            s=float(input("Enter the side length of cube:"))
            print("\n1. CSA of this cube is", 6*s*s)
            print("2. TSA of this cube is", 4*s*s)
            print("3. Volume of this cube is", s*s*s)
        
        elif shape=='2' or shape=='cuboid':
            l=float(input("Enter the length of cuboid:"))
            b=float(input("Enter the breadth of cuboid:"))
            h=float(input("Enter the height of cuboid:"))
            print("\n1. CSA of this cuboid is", 2*h*(l+b))
            print("2. TSA of this cuboid is", 2*(l*b+b*h+h*l))
            print("3. Volume of this cuboid is", l*b*h)
        
        elif shape=='3' or shape=='right circular cone' or shape=='cone':
            l=float(input("Enter the slant length of cone:"))
            r=float(input("Enter the radius of cone:"))
            h=float(input("Enter the height of cone:"))
            print("\n1. CSA of this cone is", pi*r*l)
            print("2. TSA of this cone is", pi*r*(r+l))
            print("3. Volume of this cone is", (1/3)*pi*r*r*h)
        
        elif shape=='4' or shape=='hemisphere':
            r=float(input("Enter the radius of hemisphere:"))
            print("\n1. CSA of this hemisphere is", 2*pi*r*r)
            print("2. TSA of this hemisphere is", 3*pi*r*r)
            print("3. Volume of this hemisphere is", (2/3)*pi*r*r*r)
        
        elif shape=='5' or shape=='sphere':
            r=float(input("Enter the radius of sphere:"))
            print("\n1. CSA of this sphere is", 2*pi*r*r)
            print("2. TSA of this sphere is", 3*pi*r*r)
            print("3. Volume of this sphere is", (2/3)*pi*r*r*r)
        
        elif shape=='6' or shape=='solid cylinder':
            r=float(input("Enter the radius of solid cylinder:"))
            h=float(input("Enter the height of solid cylinder:"))
            print("\n1. CSA of this solid cylinder is", 2*pi*r*h)
            print("2. TSA of this solid cylinder is", 2*pi*r*(r+h))
            print("3. Volume of this solid cylinder is", pi*r*r*h)
        
        elif shape=='7' or shape=='hollow cylinder':
            r1=float(input("Enter the inner radius of hollow cylinder:"))
            r2=float(input("Enter the outer radius of hollow cylinder:"))
            h=float(input("Enter the height of hollow cylinder:"))
            print("\n1. CSA of this hollow cylinder is", 2*pi*h*(r1+r2))
            print("2. TSA of this hollow cylinder is", (2*pi*h*(r1+r2))+(2*pi*(r2*r2-r1*r1)))
            print("3. Volume of this hollow cylinder is", pi*(r2-r1)*h)
        
        else:
            print("WRONG INPUT!! Please enter correct input")


    elif geo=='3' or geo==quit:                 #exit
        break
    
    