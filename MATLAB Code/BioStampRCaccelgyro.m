%%Kaitlyn Ammann 2017
clc; clear;
accel = xlsread('/Users/yweiner/Desktop/accel.xlsx'); %%read in accel data from excel files
gyro = xlsread('/Users/yweiner/Desktop/gyro.xlsx'); %%read in gyro data from excel files

t = accel(1:1); %%Read first timestamp value

time = (accel(:,1)-t)/1000; %%Use first timestamp value to convert time to seconds that start @ t = 0 sec
AccelX = (accel(:,2));
AccelY = (accel(:,3));
AccelZ = (accel(:,4));
p = plot(time,AccelX,'b-',time,AccelY,'r-',time,AccelZ,'g-');axis tight; xlabel('Time (s)');ylabel('Acceleration (G)'); title({'Upper Arm';'SMWT'});
set(gca,'fontsize',18,'LineWidth',2);
set(p,'LineWidth',1)
%xlim ([355 385]);%%limits EMG axis to region of interest 
%ylim ([-0.4 1.9]);%%limits EMG axis to region of interest 
saveas(gcf,'/Users/yweiner/Desktop/right hand smwt 062617.tif')
%title({'Right Leg Accel';'SMWT'});set(gca, 'fontsize', 18,'LineWidth',2);
t2 = gyro(1:1); %%Read first timestamp value

time = (gyro(:,1)-t2)/1000; %%Use first timestamp value to convert time to seconds that start @ t = 0 sec
GyroX = gyro(:,2);
GyroY = gyro(:,3);
GyroZ = gyro(:,4);
q = plot(time,GyroX,'b-',time,GyroY,'r-',time,GyroZ,'g-');axis tight; xlabel('Time (s)');ylabel('Angular Velocity (deg/s)');
title({'Upper Arm Gyro';'SMWT'});
set(q,'LineWidth',1);
%xlim ([355 385]);%%limits EMG axis to region of interest 
%ylim ([-130 175]);%%limits EMG axis to region of interest 
saveas(gcf,'/Users/yweiner/Desktop/rt hand gyro 062617.tif')
set(gca, 'fontsize', 18,'LineWidth',2);
