import subprocess as AAY


check = AAY.call(["wget", "-O", "/root/Desktop/mibbrowser.zip", "http://ireasoning.com/download/mibpro/mibbrowser.zip"])

if check == 0:
    print("Unzipping the folder...")
    check = AAY.call(["unzip", "/root/Desktop/mibbrowser.zip", "-d", "/root/Desktop/"])

    print("Checking the java requirements")
    check = AAY.Popen(["yum", "-y", "install", "java-1.8.0-openjdk"], stdout=AAY.PIPE, stderr=AAY.PIPE)
    read, err = check.communicate()

    if "Nothing to do" in read:
        print("The Package is already installed :|")
    elif "Installed" and "Complete!" in read:
        print("Package has been installed Successfully! :)")

        print("Changing browser.sh permissions")

        AAY.call(['chmod 775 /root/Desktop/ireasoning/mibbrowser/browser.sh'])
    else:
        print(" You have problem. Please check your connectivity or permission!")
        exit(1)

print("\n\n\nAll good :) You can run the application by going to \"/root/Desktop/ireasoning/mibbrowser/\". Then running \"./browser.sh\"")

print(" Thank you for using this program :)")

