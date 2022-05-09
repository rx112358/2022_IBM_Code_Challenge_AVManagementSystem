# 2022_IBM_Code_Challenge_DroneManagementSystem

An interface to create missions and monitor an AV system without the added complexity of knowing how to operate a drone. The interface will communicate with the target device to input coordinates and receive flight path and device status.

The main features are,

### Create mission

**/mission/create-mission** - Create a mission using the passed parameter values mission name,date,time,location coordinates

### Monitor mission

**/mission/monitor-mission** - Get the list of recent missions and view the flight path

### Analytics dashboard

Monitor the sensor values

![draft_arch](https://user-images.githubusercontent.com/53977169/167410080-dd54006e-012a-46bc-964b-02d5bbd18805.jpg)


## Tech stack

![tech_stack](https://user-images.githubusercontent.com/53977169/167282962-bf53e94d-d6a6-4ce0-b4c8-f2c6e0e97903.png)


## Get started

1. Clone the repo
2. Install the required dependencies
3. Go to the directory with manage.py and run server
            python manage.py runserver
            
