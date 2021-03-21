// HW1_driver에 사용되는 class를 표현해놓은 헤더파일
#include<iostream>
#include<cmath>
const double PI = 3.141592;

class Shape {
    private:
        double radius;  // for circle
        double x,y;     // for two & three dimensional shapes
        double z;       // for three dimensional shapes
    public:
        Shape(double _radius) : radius(_radius) {}                      // for circle & sphere
        Shape(double _x, double _y) : x(_x), y(_y) {}                   // for rectangle
        Shape(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {} // for cubiod     
        virtual ~Shape() {}
};

class TwoDimensionalShape : public Shape {
    public:
        TwoDimensionalShape(double _radius) : Shape(_radius) {}
        TwoDimensionalShape(double _x, double _y) : Shape(_x, _y) {}
        virtual double getArea () = 0;
};

class ThreeDimnesionalShape : public Shape {
    public:
        ThreeDimnesionalShape(double _radius) : Shape(_radius) {}
        ThreeDimnesionalShape(double _x, double _y, double _z) : Shape(_x, _y, _z) {}
        virtual double getVolume () = 0;
};

class Rectangle : public TwoDimensionalShape {
    public:
        Rectangle(double _x, double _y) : TwoDimensionalShape(_x, _y) {}
        double getArea(double x, double y)
        {
            return x * y;
        }
};

class Circle : public TwoDimensionalShape {
    public:
        Circle(double _radius) : TwoDimensionalShape(_radius) {}
        double getArea(double radius)
        {
            return radius * 2 * PI;
        }
};

class Cuboid : public ThreeDimnesionalShape {
    public:
        Cuboid(double _x, double _y, double _z) : ThreeDimnesionalShape(_x,_y,_z) {}
        double getVolume(double x, double y, double z)
        {
            return x * y * z;
        }  
};

class Sphere : public ThreeDimnesionalShape {
    public:
        Sphere(double _radius) : ThreeDimnesionalShape(_radius) {}
        double getVolume(double radius)
        {
            return 4/3 * PI * pow(radius,3)
        }
};