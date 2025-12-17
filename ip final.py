import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --------- USER INTRO ----------
n = input("Enter your name: ")
print("Welcome", n)

k = int(input(
    "Would you like to know what environmental impact is?\n"
    "1. Yes\n"
    "2. No\n"
    "Choose (1/2): "
))

if k == 1:
    print(
        "\nEnvironmental impact is the effect of human activity on the environment.\n"
        "Some common environmental impacts are:\n"
        "- Air pollution\n"
        "- Water pollution\n"
        "- Soil pollution\n"
        "- Waste production\n"
        "- Noise pollution\n"
        "- Loss of biodiversity\n"
    )
else:
    print("Thank you!")
    quit()

# --------- CSV FILE LOADING ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "C:/Users/SRINIVAS/Desktop/kruthi/total csv file.csv")

df = pd.read_csv(csv_path)

print(
    "\nWhy measure environmental impact?\n"
    "Human well-being depends on biodiversity and ecosystems.\n"
    "Measuring environmental impact helps reduce pollution, conserve resources,\n"
    "and improve sustainability.\n"
    "\nDATASET: Environmental Impact (2014–2022)\n"
)

# --------- MENU ----------
a = input(
    "1. Disasters\n"
    "2. Temperature Changes\n"
    "3. Climate-driven INFORM Risk\n"
    "4. Steps to Reduce Environmental Impact\n"
    "Enter your choice (1/2/3/4): "
)

# --------- TEMPERATURE ----------
if a == "2":
    temp = df.iloc[:6]
    plt.plot(temp["Country"], temp["2015"], label="2015")
    plt.plot(temp["Country"], temp["2016"], label="2016")
    plt.plot(temp["Country"], temp["2017"], label="2017")
    plt.plot(temp["Country"], temp["2018"], label="2018")
    plt.plot(temp["Country"], temp["2020"], label="2020")
    plt.plot(temp["Country"], temp["2021"], label="2021")
    plt.plot(temp["Country"], temp["2022"], label="2022")

    plt.xlabel("Country")
    plt.ylabel("Temperature Change")
    plt.title("Temperature Changes (2015–2022)")
    plt.legend()
    plt.show()

# --------- DISASTERS ----------
elif a == "1":
    dis = int(input(
        "Choose a country:\n"
        "1. India\n2. Sri Lanka\n3. Canada\n4. Pakistan\n5. Japan\n6. Bangladesh\n"
        "Enter (1–6): "
    ))

    country_data = {
        1: df.iloc[8:13],
        2: df.iloc[13:17],
        3: df.iloc[17:22],
        4: df.iloc[22:27],
        5: df.iloc[27:32],
        6: df.iloc[32:37]
    }

    if dis in country_data:
        country_data[dis].plot(kind="line")
        plt.xlabel("Indicators")
        plt.ylabel("Number of Disasters")
        plt.title("Disaster Analysis")
        plt.show()

# --------- INFORM RISK ----------
elif a == "3":
    h = int(input(
        "Choose a country:\n"
        "1. India\n2. Sri Lanka\n3. Canada\n4. Pakistan\n5. Japan\n6. Bangladesh\n"
        "Enter (1–6): "
    ))

    risk_data = {
        1: df.iloc[38:42],
        2: df.iloc[42:46],
        3: df.iloc[46:50],
        4: df.iloc[50:54],
        5: df.iloc[54:57],
        6: df.iloc[58:]
    }

    if h in risk_data:
        risk_data[h].plot(kind="line")
        plt.xlabel("Years")
        plt.ylabel("INFORM Risk Index")
        plt.title("Climate-driven INFORM Risk")
        plt.show()

# --------- REDUCTION STEPS ----------
elif a == "4":
    print("\nSteps to Reduce Environmental Impact:")
    print("- Volunteer for clean-up drives")
    print("- Conserve water and electricity")
    print("- Reduce plastic usage")
    print("- Use energy-efficient devices")
    print("- Plant trees")
    print("- Use eco-friendly products")

# --------- FEEDBACK ----------
f = input("\nYour feedback on this project: ")
print("\nThank you for your valuable feedback!")

# --------- END ----------
print("\nSAVE OUR ENVIRONMENT 🌱")
print("Project created by:", n)
