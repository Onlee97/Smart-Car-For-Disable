# Smart Car for Severely Paralyzed Patients

## Inspiration
Patients suffering from severe paralysis are usually dependent on others for assistance to moving around. Our team creates a complete solution that enables them to see the world independently. Due to hardware limitation, we decided to build a small model of a car instead of a wheelchair. The prototype is wifi-controllable and consists of an onboard Camera. We’re using computer-vision-based eye-tracking and IMU-based head pose estimation to receive commands from the user to control the car. This system helps paralyze people to physically interact with other people and explore their surroundings.

## What it does
The car would stream the video from the front camera in almost real-time, which allows the user to see the front view when moving. The user can turn the car to the right or left and forward it by gazing to the buttons on the screen. The system also incorporates a camera to track the eyes' pupil movement and an IMU sensor to robustly estimate where the user is looking at the screen. The information is used to control the car according to the view direction.

![Smart Car with Camera onboard (left), IMU sensor capture headpose for process (right)](images/car_IMU.jpg)

## How we built it
Hardware: We modified UCTRONICS Robot Car Kit which has a Raspberry-pi and an onboard Camera. We created our own Motor Driver from Arduino and Breadboard. The IMU sensor provides the absolute orientation of the user's head pose. It is attached elegantly to a glasses and sends the orientation to an Arduino. A Python program will process this raw information and estimate the point of view of users.

Software: We have 1 Python program that handles data processing, including the data from the IMU sensor and from Camera to robustly estimate user view direction. This program will send commands to the Raspberry Pi. We have 2 other software programs embedded in the Raspberry Pi, which will stream the camera to the remote machine. For head pose estimation, the camera looking at a driver’s face in a vehicle can use head pose estimation to control the vehicle. Head pose estimation using Arduino and a spy camera

## Challenges we ran into
We didn't expect that there would some software restriction in the Robot Car Kit we purchased that made it difficult for us to implement the ideas we planned at the beginning of the hackathon. In addition, it was the first time for some of our members to use Arduino and Raspberry Pi; however, we manage to assemble the model of the car on time.

## What's next for Smart Car for Physically Handicapped Patients
Have the button layout combined with the real-time video streamed from the car model displayed on the website.
Continue to develop the speech assistance and display it on the website

