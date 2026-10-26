print("Welcome to the Computer Parts Quiz!")

playing = input("Do you want to test your knowledge? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Try your best  ")

Score = 0

#Question 1
print("What is the main function of the CPU?")
print("a. Store files permanently")
print("b. Process instructions and perform calculations")
print("c. Display images on the monitor")
print("d. Supply power to the computer")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "b":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is b.")

# Question 2
print("Which computer component temporarily stores data while programs are running?")
print("a. SSD")
print("b. GPU")
print("c. RAM")
print("d. Power supply")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is c.")

# Question 3
print("What does a motherboard do?")
print("a. Connects and allows communication between computer components")
print("b. Prevents the computer from overheating")
print("c. Stores the operating system permanently")
print("d. Converts AC power into DC power")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "a":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is a.")

# Question 4
print("Which component is primarily responsible for rendering graphics?")
print("a. CPU cooler")
print("b. RAM")
print("c. SSD")
print("d. GPU")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "d":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is d.")

# Question 5
print("What is the purpose of the power supply unit (PSU)?")
print("a. Increase internet speed")
print("b. Convert AC electricity into DC power for computer components")
print("c. Store backup files")
print("d. Control the operating system")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "b":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is b.")

# Question 6
print("Which storage device typically has no moving mechanical parts?")
print("a. Hard Disk Drive (HDD)")
print("b. Optical Disc Drive")
print("c. Solid State Drive (SSD)")
print("d. Floppy Disk Drive")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is c.")

# Question 7
print("What is the main purpose of thermal paste between a CPU and its cooler?")
print("a. Improve heat transfer")
print("b. Increase processor clock speed")
print("c. Prevent electrical power loss")
print("d. Increase RAM capacity")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "a":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is a.")

# Question 8
print("Which expansion slot is commonly used for a modern dedicated graphics card?")
print("a. SATA")
print("b. DIMM")
print("c. M.2 Key E")
print("d. PCIe x16")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "d":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is d.")

# Question 9
print("\n9. What does the CMOS battery typically help maintain when the computer is powered off?")
print("a. Graphics processing speed")
print("b. System clock and certain firmware settings")
print("c. RAM contents")
print("d. CPU temperature")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "b":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is b.")

# Question 10
print("Which component allows a computer to connect to an Ethernet network?")
print("a. Sound card")
print("b. Graphics card")
print("c. Network Interface Card (NIC)")
print("d. Storage controller")

answer = input("Enter your answer (a/b/c/d): ")

if answer.lower() == "c":
    print("Correct!")
    Score += 1
else:
    print("Incorrect! The correct answer is c.")

print("You got " + str((Score / 10) * 100) + "%.")