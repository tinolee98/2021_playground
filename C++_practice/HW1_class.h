// HW1_driver.cpp에 사용되는 class를 선언해놓은 헤더파일
#include<iostream>
#include<cmath>

using namespace std;

const double PI = 3.141592;

class Shape {
    public:    
        virtual ~Shape() {}
        virtual void print()
        {
            cout << "Shape" << endl;
        }
};

class TwoDimensionalShape : public Shape {
    public:
        virtual void print()
        {
            Shape::print();
            cout << "TwoDimesional" << endl;
        }
        virtual double getArea () =0;
};

class ThreeDimensionalShape : public Shape {
    public:
        virtual void print()
        {
            Shape::print();
            cout << "ThreeDimensional" << endl;
        }
        virtual double getVolume () =0;
};

class Rectangle : public TwoDimensionalShape {
    private:
        double x,y;
    public:
        void print() {
            TwoDimensionalShape::print();
            cout << "Rectangle" << endl;
        }
        Rectangle(double _x, double _y) : x(_x),y(_y) {}
        double getArea()
        {
            cout << "( x : " << x << ", y : " << y << " )"<< endl;
            return x * y;
        }
};

class Circle : public TwoDimensionalShape {
    private:
        double radius;
    public:
        void print() {
            TwoDimensionalShape::print();
            cout << "Circle" << endl;
        }
        Circle(double _radius) : radius(_radius) {}
        double getArea()
        {
            cout << "( radius : " << radius << " )" << endl;
            return radius * 2 * PI;
        }
};

class Cuboid : public ThreeDimensionalShape {
    private:
        double x,y,z;
    public:
        void print() {
            ThreeDimensionalShape::print();
            cout << "Cuboid" << endl;
        }
        Cuboid(double _x, double _y, double _z) : x(_x), y(_y), z(_z) {}
        double getVolume()
        {
            cout << "( x : " << x << ", y : " << y << ", z : " << z << " )"<< endl;
            return x * y * z;
        }  
};

class Sphere : public ThreeDimensionalShape {
    private:
        double radius;
    public:
        void print() {
            ThreeDimensionalShape::print();
            cout << "Sphere" << endl;
        }
        Sphere(double _radius) : radius(_radius) {}
        double getVolume()
        {
            cout << "( radius : " << radius << " )"<<endl;
            return 4/3 * PI * pow(radius,3);
        }
};