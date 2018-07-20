//
//  LanderSim.cpp
//  LunalLanderFinal
//
//  Created by Thomas Tylek on 3/17/15.
//  Copyright (c) 2015 Thomas Tylek. All rights reserved.
//

#include "LanderSim.h"
#include <cmath>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void introduction (istream &is, ostream &os, string target, string replacement);
void updateStatus(double &velocity, double burnAmount, double &fuelRemaining, double &height);
void touchdown(double &elapsedTime, double &velocity, double &burnAmount, double &height);
void finalAnalysis(ostream &os, double velocity);

int main(void)
{
    string decision;
    string target = "$SPACECRAFT";
    string replacement = "Apollo";
    ifstream is("/Users/thomastylek/Desktop/input.txt");
    ofstream os("/Users/thomastylek/Desktop/output.txt");
    double elapsedTime = 0;
    double velocity = 50;
    double burnAmount = 0;
    double height = 1000;
    double fuelRemaining = 150;
    os << "Do you want instructions (y/n)? ";
    cout << "Do you want instructions (y/n)? ";
    cin >> decision;
    cout << decision;
    os << decision;
    if (decision == "y" || decision == "Y")
        introduction (is, os, target, replacement);
    os << endl << endl;
    os << "Moon Hack 2018 LUNAR LANDER" << endl << "Beginning landing procedure.........." << endl << "DIGBY wishes you good luck!";
    os << endl << endl;
    cout << endl << endl;
    cout << "Moon Hack 2018 LUNAR LANDER" << endl << "Beginning landing procedure.........." << endl << "DIGBY wishes you good luck!";
    cout << endl << endl;
    while (height > 0)
    {
        cout << "Status of your" << replacement << " spacecraft:" << endl;
        cout << "Time   : " << elapsedTime << " seconds" << endl;
        cout << "Height : " << height << " feet" << endl;
        cout << "Speed  : " << velocity << " feet/second" << endl;
        cout << "Fuel   : " << fuelRemaining << endl;
        cout << "Enter fuel burn amount: ";
        os << "Status of your" << replacement << " spacecraft:" << endl;
        os << "Time   : " << elapsedTime << " seconds" << endl;
        os << "Height : " << height << " feet" << endl;
        os << "Speed  : " << velocity << " feet/second" << endl;
        os << "Fuel   : " << fuelRemaining << endl;
        os << "Enter fuel burn amount: ";
        if (fuelRemaining == 0)
        {
            cout << "**** OUT OF FUEL ****" << endl;
            os << "**** OUT OF FUEL ****" << endl;
            burnAmount = 0;
        }
        else
            cin >> burnAmount;
        os << burnAmount << endl << endl;
        cout << endl << endl;
        updateStatus(velocity, burnAmount, fuelRemaining, height);
    }
    cout << "***** CONTACT *****" << endl;
    os << "***** CONTACT *****" << endl;
    touchdown(elapsedTime, velocity, burnAmount, height);
    cout << "Touchdown at " << elapsedTime << " seconds." << endl;
    os << "Touchdown at " << elapsedTime << " seconds." << endl;
    cout << "Landing velocity = " << velocity << " feet/sec." << endl;
    os << "Landing velocity = " << velocity << " feet/sec." << endl;
    cout << fuelRemaining << " units of fuel remaining." << endl << endl;
    os << fuelRemaining << " units of fuel remaining." << endl << endl;
    finalAnalysis(os, velocity);
}
void introduction(istream &is, ostream &os, string target, string replacement)
{
    string line;
    while (getline(is, line))
    {
        while (line.find(target) != -1)
        {
            line.replace(line.find(target), target.length(), replacement);
        }
        os << line <<endl;
    }
}
void updateStatus(double &velocity, double burnAmount, double &fuelRemaining, double &height)
{
    fuelRemaining = fuelRemaining - burnAmount;
    height = height - ((((velocity - burnAmount) + 5) + velocity)/2);
    velocity = velocity - burnAmount + 5;
}
void touchdown(double &elapsedTime, double &velocity, double &burnAmount, double &height)
{
    double oldvelocity = velocity + burnAmount - 5;
    double oldheight = height + ((velocity + oldvelocity)/2);
    double oldtime = elapsedTime - 1;
    double fraction = 0.0;
    if (burnAmount == 5)
        fraction = oldheight / oldvelocity;
    else
        fraction = (sqrt((oldvelocity*oldvelocity) + (oldheight*(10 - (2 * burnAmount)))) - oldvelocity) / (5 - burnAmount);
    elapsedTime = oldtime + fraction*1.0;
    velocity = oldvelocity + (5 - burnAmount)*fraction *1.0;
    height = oldheight;
}
void finalAnalysis(ostream &os, double velocity)
{
    if (velocity == 0.0)
    {
        os << ": Congratulations! A perfect landing!" << endl;
        cout << ": Congratulations! A perfect landing!" << endl;
    }
    else if (velocity > 0.0 && velocity < 2.0)
    {
        os << "A little bumpy." << endl;
        cout << "A little bumpy." << endl;
    }
    else if (velocity >= 2.0 && velocity < 5.0)
    {
        os << "You blew it!" << endl;
        cout << "You blew it!" << endl;
    }
    else if (velocity >= 5.0 && velocity < 10.0)
    {
        os << "Your ship is a heap of junk!" << endl;
        cout << "Your ship is a heap of junk!" << endl;
    }
    else if (velocity >= 10.0 && velocity < 30.0)
    {
        os << "You blasted a huge crater!" << endl;
        cout << "You blasted a huge crater!" << endl;
    }
    else if (velocity >= 30.0 && velocity < 50)
    {
        os << "Your ship is a wreck!" << endl;
        cout << "Your ship is a wreck!" << endl;
    }
    else
    {
        os << "You totaled an entire mountain!" << endl;
        cout << "You totaled an entire mountain!" << endl;
    }
}