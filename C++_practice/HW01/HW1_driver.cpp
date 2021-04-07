/* HW1. Inheritance Hierarchy of shapes. shape - two-dimensional or three-dimensional - some shapes 순으로 상속되는 클래스들 다음의 조건을 만족하도록 만들어라.
1. shape class 는 interfaces을 포함하는 abstract base class이다.
2. TwoDimensionalShape, ThreeDimnesionalShape는 shape를 derieved하여 만들어진 abstract class이다.
3. 각 class의 type과 dimensions를 output으로 갖는 virtual print function을 만들어라.
4. area, volume 을 출력하는 virtual function을 만들어라.
5. shape class hierarchy를 test할 수 있는 driver program을 만들어라. */

// Driver_program
#include<iostream>
#include<cmath>
#include "HW1_class.h"
using namespace std;
int main()
{
    // 도형에 들어갈 values
    double radius = 2.0;
    double x = 4.0;
    double y = 5.0;
    double z = 6.0;
    
    Rectangle rect(x,y);
    Circle cir(radius);
    Cuboid cub(x,y,z);
    Sphere sph(radius);

    rect.print();
    cout << "Area of Rectangle " << rect.getArea() << endl<<endl;

    cir.print();
    cout << "Area of Circle " << cir.getArea() << endl<<endl;

    cub.print();
    cout << "Volume of Cuboid " << cub.getVolume() << endl<<endl;

    sph.print();
    cout << "Volume of Sphere " << sph.getVolume() << endl<<endl;
}