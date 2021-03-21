// HW1_driver.cpp에 사용되는 class를 선언해놓은 헤더파일
// header file 과 function cpp file을 따로 짜는 건 어떨까?
#include<iostream>
#include<cmath>

using namespace std;

const double PI = 3.141592;

class Shape {
    public:
        double radius;  // for circle
        double x,y;     // for two & three dimensional shapes
        double z;       // for three dimensional shapes
        Shape(double _radius) : radius(_radius) {}                      // for circle & sphere
        Shape(double _x, double _y) : x(_x), y(_y) {}                   // for rectangle
        Shape(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {} // for cubiod     
        virtual ~Shape() {}
        virtual void print()
        {
            cout << "Shape" << endl;
        }
        virtual double getArea() { return -1; }
        virtual double getVolume() { return -1; }
};

class TwoDimensionalShape : public Shape {
    public:
        virtual void print()
        {
            Shape::print();
            cout << "TwoDimesional" << endl;
        }
        TwoDimensionalShape(double _radius) : Shape(_radius) {}
        TwoDimensionalShape(double _x, double _y) : Shape(_x, _y) {}
        virtual double getArea () { return -1; }
};

class ThreeDimensionalShape : public Shape {
    public:
        virtual void print()
        {
            Shape::print();
            cout << "ThreeDimensional" << endl;
        }
        ThreeDimensionalShape(double _radius) : Shape(_radius) {}
        ThreeDimensionalShape(double _x, double _y, double _z) : Shape(_x, _y, _z) {}
        virtual double getVolume () { return -1; }
};

class Rectangle : public TwoDimensionalShape {
    public:
        void print() {
            TwoDimensionalShape::print();
            cout << "Rectangle" << endl;
        }
        Rectangle(double _x, double _y) : TwoDimensionalShape(_x, _y) {}
        double getArea()
        {
            cout << "( x : " << x << ", y : " << y << " )"<< endl;
            return x * y;
        }
};

class Circle : public TwoDimensionalShape {
    public:
        void print() {
            TwoDimensionalShape::print();
            cout << "Circle" << endl;
        }
        Circle(double _radius) : TwoDimensionalShape(_radius) {}
        double getArea()
        {
            cout << "( radius : " << radius << " )" << endl;
            return radius * 2 * PI;
        }
};

class Cuboid : public ThreeDimensionalShape {
    public:
        void print() {
            ThreeDimensionalShape::print();
            cout << "Cuboid" << endl;
        }
        Cuboid(double _x, double _y, double _z) : ThreeDimensionalShape(_x,_y,_z) {}
        double getVolume()
        {
            cout << "( x : " << x << ", y : " << y << ", z : " << z << " )"<< endl;
            return x * y * z;
        }  
};

class Sphere : public ThreeDimensionalShape {
    public:
        void print() {
            ThreeDimensionalShape::print();
            cout << "Sphere" << endl;
        }
        Sphere(double _radius) : ThreeDimensionalShape(_radius) {}
        double getVolume()
        {
            cout << "( radius : " << radius << " )"<<endl;
            return 4/3 * PI * pow(radius,3);
        }
};