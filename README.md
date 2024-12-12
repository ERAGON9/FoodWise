![FoodWise Logo](https://github.com/ERAGON9/FoodWise/blob/main/FoodWise%20Logo.png)


# Overview
FoodWise is an innovative smart refrigerator project that integrates an IoT device with a mobile app to revolutionize the way you manage your food.


# Features

* **Real-Time Inventory** - Management of food inventory through seamless item scanning.

* **Automated Shopping Lists** - Generation of a shopping list by analyzing the scanned inventory data with the user’s configuration.


* **Recipe Suggestions** - Personalized recipe suggestions based on available ingredients in the refrigerator.


* **Consumption reports** - Get detailed weekly consumption reports and statistics.


* **Personalized Notifications** - Set reminders for expiration dates, low stock, etc.

![App Screens](https://github.com/ERAGON9/FoodWise/blob/main/AppScreens.png)

# Technology Stack
* **Backend:** Python, Flask, SQLite Database
* **Frontend (Mobile app)**: React-Native
* **Embedded**: Raspberry Pi OS, Python
* **Hardware:** Raspberry Pi, Touchscreen , Scanner
* **Cloud**: GCP

# Deployment
clone the project

```bash
git clone https://github.com/ERAGON9/FoodWise
cd FoodWise
```

### Locally start the server


navigate to Server
```bash
cd server
```
Install the dependencies
```bash
pip install -r requirements.txt
```
Ensure that the docker variable at the beginning of the server.py file (line 25) is set to False.


Run server.py

```bash
python server.py
```
<br><br>

### Locally start the mobile application

navigate to Application
```bash
cd application
```
Install the dependencies
```bash
npm install
```
start the Metro Bundler:
```bash
npm start android
```
To run on a physical device, make sure USB Debugging is enabled and the device is connected.
<br><br>

### Explanation on how to deploy the Flask app to GCP (Google Cloud)
First, we need to build a Docker image containing the Flask app and then upload the image to Docker Hub and then upload the Docker to the google cloud.

In the Server directory, there is already a Dockerfile with all the necessary instructions to create the image.

Now the following steps need to be done:


1. Ensure that the docker variable at the beginning of the server.py file (line 25 at the time of writing this document) is set to True.

2. Ensure that all libraries not included in Python's standard library are listed in the requirements.txt file, located in the Server directory, in the following format: <library_name> == <version_number>.

3. Make sure Docker Engine is installed on your computer and is connect to your Dockerhub account

4. Open cmd and run the following commands:

```bash
docker build -t my-flask-app .

docker tag my-flask-app username/my-flask-app:<version_tag>

docker push username/my-flask-app:<same_version>
```

5. Now, go to Google Cloud Console, then to Cloud Run, and click on the Create Service Button.

6. In the Container image URL field, enter the following URL (after making the necessary adjustments):
```bash
docker.io/username/my-flask-app:<version_tag>
```

7. In the Service name field, enter foodwise.

8. In the Authentication section, check the box for Allow unauthenticated invocations.

9. In the Minimum number of instances section, select 1.

10. In the Container section, ensure that the Container port is set to 12345

<br><br>
### Creating a debug APK for the application

Go to the root of the application in the terminal and run
```bash
react-native bundle --platform android --dev false --entry-file index.js --bundle-output android/app/src/main/assets/index.android.bundle --assets-dest android/app/src/main/res
```

Go to android directory 
```bash
cd android
```

run this command
```bash
./gradlew assembleDebug
```
The APK will be created in
```bash
Application/android/app/build/outputs/apk/debug/app-debug.apk
```

# Technical Explanations and Important Notes for the IoT Device
The device is a Raspberry Pi 4 running the following operating system: Raspbian GNU/Linux 11 (Bullseye).

The device also has a touchscreen connected via HDMI and a scanner connected via USB.

To give the device access to Wi-Fi, you need to connect it to the local Wi-Fi network through its operating system.

To do this, you need to connect a keyboard and mouse to the device.

After that, turn on the device, and once the operating system has started, click on the Wi-Fi icon and select the Wi-Fi network you want to connect to.

After the device is connected to Wi-Fi, you can access it remotely using a program called VNC Viewer.

You'll need the local IP address that the device received from the local Wi-Fi network.     

You can find the local IP address by running the command hostname -I in the terminal of the operating system running on the device.

When connecting, you will be prompted to enter a username and password. The username is codeCrafters and the password is 12345.

On the device's operating system desktop, 
there is a file named app.py, which is the program running on the device
To ensure that the program runs automatically when the operating system starts, you need to make sure that there is a file named autorunmyfile.desktop    
in the file system at /home/codeCrafters/.config/autostart.

The file should contain the following content:
[Desktop Entry]
Exec = bash -c "cd /home/codeCrafters/Desktop && sudo python3 app.py > /home/codeCrafters/Desktop/app.log 2>&1"

This file runs automatically when the operating system starts, 
giving the operating system the instruction to navigate to the directory where the app.py file is located, 
run it with full permissions, and direct all the program's output, including logs, to a file named app.log on the desktop.

