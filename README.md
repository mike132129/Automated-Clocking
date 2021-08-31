# Automated-Clocking
This repo constructs a tool that helps to clock in and out every day with assigned time.

## Setup Environment

1. Setting the username and password in `Settings` 
![image](https://user-images.githubusercontent.com/48711966/130392610-501b2aa8-4147-4bc3-a3f0-182bcb9b1c03.png)

Select the "Secrets" in the left of the list

![image](https://user-images.githubusercontent.com/48711966/130392762-58eb6a31-0cc4-4945-965f-5d1d67793819.png)

Add two `Repository secrets`, `username` and `password`.

where `username` is your personal `員工編號` in <https://cloud.nueip.com/login/lawsnote>;

`password` is your `密碼`

![image](https://user-images.githubusercontent.com/48711966/130392995-f3d06669-3b85-47dd-8343-c6356ac2ef26.png)

2. Remember to enable the workflow manually in `Action`.

3. Setting the clock in-and-out time (Optional)

To change the clocking time, (default clockin: 9:58 a.m., clockout: 17:57), you need to edit the file in the `.github/workflows/clockin.yml` and `.github/workflows/clockout.yml` with crontab format.

![image](https://user-images.githubusercontent.com/48711966/130393884-3e414de5-47b9-4d46-b5d4-814b65b77f34.png)

